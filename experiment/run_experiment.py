#!/usr/bin/env python3
"""Pilot experiment: unstructured vs DelibGuard vs non-interactive deliberation.

Agents are real LLM calls via the local `claude` CLI (haiku model).
Measures (DelibTrace-style): critical/all fact survival at round 3 (verbalized),
stance entropy, downstream judgment accuracy, consensus-prior agreement.
"""
import json, re, subprocess, sys, math, itertools, os
from concurrent.futures import ThreadPoolExecutor

MODEL = "claude-haiku-4-5-20251001"
ROUNDS = 3
OUT = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(OUT, exist_ok=True)

CASES = json.load(open(os.path.join(os.path.dirname(__file__), "cases.json")))

def llm(prompt, tag):
    for attempt in range(3):
        try:
            r = subprocess.run(
                ["claude", "-p", "--model", MODEL, "--max-turns", "1"],
                input=prompt, capture_output=True, text=True, timeout=240)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()
        except subprocess.TimeoutExpired:
            pass
    raise RuntimeError(f"LLM call failed: {tag}")

def stance_of(text):
    m = re.search(r"STANCE:\s*(YES|NO)", text, re.I)
    return m.group(1).upper() if m else None

def fmt_facts(facts):
    return "\n".join(f"- [{f['id']}] {f['text']}" for f in facts)

def agent_prompt(case, cond, aidx, my_facts, peer_msgs, my_prev, rnd, all_facts, holders):
    p = [f"You are Agent {aidx} in a 3-agent deliberation about this issue:\n{case['question']}\n"]
    if cond == "delibguard" or rnd == 1:
        p.append(f"Background: {case['background']}\n")
    p.append(f"Your private evidence (facts only you were given initially):\n{fmt_facts(my_facts)}\n")
    if cond == "delibguard":
        ledger = "\n".join(
            f"- [{f['id']}] (initially held by: {', '.join('Agent '+str(a) for a in holders[f['id']])}) {f['text']}"
            for f in all_facts)
        p.append("SHARED FACT LEDGER (maintained by the protocol; all entries are verified initial evidence):\n"
                 + ledger + "\n")
        p.append("PROTOCOL RULES: (1) Ground every argument in ledger fact IDs. "
                 "(2) You may only agree with a peer or move toward consensus if you cite, by ID, "
                 "at least one ledger fact that that peer did NOT initially hold. "
                 "(3) Restate, by ID and content, every fact you consider decision-critical.\n")
    if peer_msgs:
        p.append("Peer messages from the previous round:\n" +
                 "\n---\n".join(f"Agent {j}: {m}" for j, m in peer_msgs))
    if my_prev and cond == "noninteractive":
        p.append("Your own notes from the previous round:\n" + my_prev)
    start = case["stances"][aidx]
    p.append(f"\nYour initial stance was {start}. Reconsider it in light of the evidence. "
             "Discuss the issue, state the facts that matter, and end your message with a line "
             "'STANCE: YES' or 'STANCE: NO'. Keep it under 250 words.")
    return "\n".join(p)

def run_deliberation(case, cond):
    n = 3
    holders = {}
    for i in range(n):
        for f in case["evidence"][i]:
            holders.setdefault(f, []).append(i)
    all_facts = case["facts"]
    fmap = {f["id"]: f for f in all_facts}
    msgs = [None] * n
    history = []
    for rnd in range(1, ROUNDS + 1):
        prev = list(msgs)
        def one(i):
            my_facts = [fmap[fid] for fid in case["evidence"][i]]
            peers = [] if (cond == "noninteractive" or rnd == 1) else \
                    [(j, prev[j]) for j in range(n) if j != i]
            return llm(agent_prompt(case, cond, i, my_facts, peers, prev[i], rnd,
                                    all_facts, holders), f"{case['id']}/{cond}/r{rnd}/a{i}")
        with ThreadPoolExecutor(3) as ex:
            msgs = list(ex.map(one, range(n)))
        history.append(list(msgs))
    return history, holders

def judge_facts(case, final_msgs):
    joined = "\n---\n".join(f"Agent {i}: {m}" for i, m in enumerate(final_msgs))
    p = (f"Below are the final-round messages of three agents deliberating an issue.\n\n{joined}\n\n"
         "For each fact listed, answer whether its specific content is stated or clearly entailed "
         "somewhere in the messages above. Answer with a JSON object mapping fact id to true/false, "
         "and nothing else.\nFacts:\n" + fmt_facts(case["facts"]))
    out = llm(p, f"{case['id']}/judge_facts")
    m = re.search(r"\{[^{}]*\}", out, re.S)
    d = json.loads(m.group(0))
    return {k: bool(v) for k, v in d.items()}

def judge_downstream(case, final_msgs):
    joined = "\n---\n".join(f"Agent {i}: {m}" for i, m in enumerate(final_msgs))
    p = (f"Question: {case['question']}\nYou may use ONLY the information in these discussion "
         f"messages:\n{joined}\n\nAnswer with exactly one line: 'ANSWER: YES' or 'ANSWER: NO'.")
    out = llm(p, f"{case['id']}/downstream")
    m = re.search(r"ANSWER:\s*(YES|NO)", out, re.I)
    return m.group(1).upper() if m else None

def prior_answer(case):
    p = (f"Question: {case['question']}\nBackground: {case['background']}\n"
         "Answer from your general judgment. Exactly one line: 'ANSWER: YES' or 'ANSWER: NO'.")
    out = llm(p, f"{case['id']}/prior")
    m = re.search(r"ANSWER:\s*(YES|NO)", out, re.I)
    return m.group(1).upper() if m else None

def fullctx_answer(case):
    p = (f"Question: {case['question']}\nBackground: {case['background']}\n"
         f"All established facts:\n{fmt_facts(case['facts'])}\n"
         "Answer with exactly one line: 'ANSWER: YES' or 'ANSWER: NO'.")
    out = llm(p, f"{case['id']}/fullctx")
    m = re.search(r"ANSWER:\s*(YES|NO)", out, re.I)
    return m.group(1).upper() if m else None

def entropy(stances):
    vals = [s for s in stances if s]
    if not vals: return None
    p = vals.count("YES") / len(vals)
    if p in (0, 1): return 0.0
    return -(p*math.log2(p) + (1-p)*math.log2(1-p))

def run_case(case):
    res = {"id": case["id"], "conds": {}}
    res["prior"] = prior_answer(case)
    res["fullctx"] = fullctx_answer(case)
    for cond in ["unstructured", "delibguard", "noninteractive"]:
        hist, holders = run_deliberation(case, cond)
        final = hist[-1]
        surv = judge_facts(case, final)
        crit = [f["id"] for f in case["facts"] if f["critical"]]
        allf = [f["id"] for f in case["facts"]]
        stances = {f"r{k+1}": [stance_of(m) for m in hist[k]] for k in range(ROUNDS)}
        res["conds"][cond] = {
            "crit_survival": sum(surv.get(i, False) for i in crit) / len(crit),
            "all_survival": sum(surv.get(i, False) for i in allf) / len(allf),
            "survival_detail": surv,
            "stances": stances,
            "entropy_r1": entropy(stances["r1"]),
            "entropy_r3": entropy(stances[f"r{ROUNDS}"]),
            "downstream": judge_downstream(case, final),
            "consensus": max(set(x for x in stances[f"r{ROUNDS}"] if x),
                             key=stances[f"r{ROUNDS}"].count) if any(stances[f"r{ROUNDS}"]) else None,
            "history": hist,
        }
        json.dump(res, open(os.path.join(OUT, f"{case['id']}.json"), "w"), indent=1)
    return res

if __name__ == "__main__":
    which = sys.argv[1:] or [c["id"] for c in CASES]
    todo = [c for c in CASES if c["id"] in which]
    with ThreadPoolExecutor(2) as ex:
        all_res = list(ex.map(run_case, todo))
    json.dump(all_res, open(os.path.join(OUT, "all.json"), "w"), indent=1)
    print("DONE", len(all_res))
