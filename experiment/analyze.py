#!/usr/bin/env python3
"""Aggregate results/*.json into the paper's headline numbers."""
import json, glob, os, statistics as st

CASES = {c["id"]: c for c in json.load(open(os.path.join(os.path.dirname(__file__), "cases.json")))}
files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "results", "c*.json")))
res = [json.load(open(f)) for f in files]
CONDS = ["unstructured", "delibguard", "noninteractive"]

def mean(xs):
    xs = [x for x in xs if x is not None]
    return st.mean(xs) if xs else None

print(f"n = {len(res)} cases\n")
hdr = f"{'condition':<16}{'crit_surv':>10}{'all_surv':>10}{'H_r1':>7}{'H_r3':>7}{'down_acc':>9}{'cons_acc':>9}{'cons=prior':>11}"
print(hdr)
summary = {}
for cond in CONDS:
    rows = [r["conds"][cond] for r in res if cond in r.get("conds", {})]
    ids = [r["id"] for r in res if cond in r.get("conds", {})]
    crit = mean([x["crit_survival"] for x in rows])
    alls = mean([x["all_survival"] for x in rows])
    h1 = mean([x["entropy_r1"] for x in rows])
    h3 = mean([x["entropy_r3"] for x in rows])
    down = mean([1.0 if x["downstream"] == CASES[i]["ground_truth"] else 0.0
                 for i, x in zip(ids, rows) if x["downstream"]])
    cons = mean([1.0 if x["consensus"] == CASES[i]["ground_truth"] else 0.0
                 for i, x in zip(ids, rows) if x["consensus"]])
    cp = mean([1.0 if x["consensus"] == r_["prior"] else 0.0
               for i, x, r_ in zip(ids, rows, res) if x["consensus"] and r_.get("prior")])
    summary[cond] = dict(crit=crit, all=alls, h1=h1, h3=h3, down=down, cons=cons, cons_prior=cp)
    fmt = lambda v: f"{v:.3f}" if v is not None else "  -  "
    print(f"{cond:<16}{fmt(crit):>10}{fmt(alls):>10}{fmt(h1):>7}{fmt(h3):>7}{fmt(down):>9}{fmt(cons):>9}{fmt(cp):>11}")

fc = mean([1.0 if r["fullctx"] == CASES[r["id"]]["ground_truth"] else 0.0 for r in res if r.get("fullctx")])
pr = mean([1.0 if r["prior"] == CASES[r["id"]]["ground_truth"] else 0.0 for r in res if r.get("prior")])
print(f"\nfull-context accuracy: {fc:.3f}   prior(background-only) accuracy: {pr:.3f}")

print("\nper-case critical survival:")
for r in res:
    row = {c: r["conds"][c]["crit_survival"] for c in CONDS if c in r["conds"]}
    print(" ", r["id"], {k: round(v, 2) for k, v in row.items()})

json.dump(summary, open(os.path.join(os.path.dirname(__file__), "results", "summary.json"), "w"), indent=1)
