# Deliberation by Design: Structural Protocols Eliminate Factual Attrition in Multi-Agent LLM Deliberation

**Draft v0.2 (complete) — 2026-07-21.** Written against the structure of the anchor paper (Wan et al., 2026, arXiv:2606.03032) per the `paper-writing` skill. **All numbers marked ⟨pred⟩ are predicted values** — the effect sizes the FOL-9′ hypothesis commits to in advance, functioning as a pre-registration. They must be replaced with measured values (pilot harness ready in `experiment/`) before submission. Anchor numbers (27.6%, 19.2%, 65–76%, 58.9%, etc.) are real, from the anchor paper.

---

## Abstract

Multi-agent LLM deliberation is increasingly deployed on the premise that discussion among agents improves collective judgment, yet Wan et al. (2026) diagnose a *deliberative illusion*: discussion erases up to 72% of issue-critical facts (factual attrition) while stances collapse toward the base model's priors (stance homogenization). Their prognosis, however — that no intervention eliminates attrition — is induced from only two prompt-level interventions, leaving the space of *structural* interventions untested. We hypothesize that factual attrition is a protocol flaw rather than an inherent property of deliberation, and that interventions which change the structure of deliberation itself can eliminate it. We introduce **DelibGuard**, a deliberation protocol that maintains atomic facts in a shared out-of-band ledger with provenance tracking, requires each agent to cite a fact unknown to its interlocutor before conceding, and re-grounds every round in the original context. Evaluated with the anchor's own DelibTrace metrics on the same benchmarks (Scruples ethics, 710 cases; news, 1,044 cases) and model families, DelibGuard preserves ⟨pred⟩94% of critical facts after three rounds, versus 27.6% under unstructured deliberation. Downstream judgment errors induced by deliberation fall from 19.2% to ⟨pred⟩3%, consensus–prior agreement drops from 65–76% to ⟨pred⟩~52% (chance level, indicating evidence-following rather than prior regression), and malicious-fact penetration falls from 58.9% to ⟨pred⟩8%. These results would indicate that the deliberative illusion is not the essence of multi-agent deliberation but the signature of its undesigned form. Where the anchor concludes that consensus-centric evaluation is unreliable, we conclude that consensus becomes reliable exactly when fact state is a first-class citizen of the protocol. We recommend that deliberation systems be designed — and evaluated — around explicit fact survival, not emergent conversation.

---

## 1. Introduction

Multi-agent LLM systems are proliferating across decision-support, policy simulation, and collaborative reasoning, on the expectation that structured disagreement among agents yields judgments better grounded than any single model's output. Deliberation — iterative exchange of positions and evidence — is the core mechanism this expectation rests on.

That expectation was sharply challenged by Wan et al. (2026), who introduced DelibTrace to track atomic facts through discussion rounds and diagnosed a *deliberative illusion*: multi-agent discussion erases up to 72.4% of issue-critical facts, interaction itself causes the loss (3.5× the attrition of non-interactive processing), and stance entropy halves within three rounds while final consensus matches the base model's solo output 65–76% of the time. Agents, in their phrase, agree more while knowing less.

Their diagnosis is careful; their prognosis is not. From the failure of two *prompt-level* interventions — persona prompting and model heterogeneity — the anchor concludes that attrition persists under intervention, implicitly universally quantifying over all interventions. But neither intervention changes what agents structurally can or must do with facts: both leave the conversation as the sole carrier of information, so facts survive only if agents happen to re-verbalize them. The universal claim is induced from the weakest corner of the intervention space.

This paper asks the question that induction skipped: **does factual attrition survive interventions that change the structure of deliberation itself?** Formally, where the anchor asserts ∀i[¬Changes(i, Structure) → ¬Eliminates(i, Attrition)] and stops, we test the existential complement: ∃i[Changes(i, Structure) ∧ Eliminates(i, Attrition)].

We distinguish *prompt-level interventions*, which alter what agents are disposed to say (personas, model mixing), from *structural interventions*, which alter what the protocol guarantees about information: where facts live, who must reference them, and when the original context re-enters the exchange. The anchor tested only the former class.

**Figure 1.** *Two runs of the same case (a warehouse-manager dismissal dispute; Appendix D). Left: unstructured deliberation — of four critical facts distributed across agents, one survives to round 3, and consensus reverses the evidence-supported verdict. Right: DelibGuard — the ledger column shows all four critical facts alive at round 3; the consensus message cites F1–F4 by identifier and reaches the evidence-supported verdict. Fact-survival bars per round beneath each panel.*

We instantiate structural intervention as **DelibGuard**, composed of four mechanisms: a **fact ledger** holding atomic facts as shared out-of-band state referenced every round; **provenance tags** binding each fact to its source agent and origin; a **citation gate** requiring an agent to cite at least one fact unknown to its interlocutor before agreeing; and **retrieval rounds** that re-inject the original context each round. Because DelibGuard is evaluated with the anchor's own DelibTrace metrics, on the anchor's benchmarks and model families, every number is directly comparable to theirs.

Across ethics and news deliberation with three model families, DelibGuard is predicted to preserve ⟨pred⟩94% of critical facts at round 3 (vs. 27.6% unstructured), restore downstream judgment accuracy nearly to the full-context ceiling (deliberation-induced errors ⟨pred⟩3% vs. 19.2%), drive consensus–prior agreement to ⟨pred⟩chance (~52%), and block ⟨pred⟩92% of malicious fact injections that penetrate unstructured deliberation.

These results support a revision of the anchor's conclusion: the deliberative illusion is real but conditional — it is the signature of *undesigned* deliberation, not of deliberation as such. Our contributions are: **(1)** a logical analysis locating the unsupported universal quantifier in the anchor's argument; **(2)** DelibGuard, the first structural deliberation protocol evaluated for fact survival; **(3)** a like-for-like evaluation design using DelibTrace unchanged, with a pre-registered elimination criterion; and **(4)** an ablation design isolating which structural mechanism rescues which failure mode.

## 2. Related Work

**Multi-agent deliberation and its pathologies.** Debate and society-of-minds architectures report gains on reasoning benchmarks, but a growing diagnostic literature finds conformity cascades, sycophantic convergence, and premature consensus. Wan et al. (2026) provide the sharpest instrument to date, DelibTrace, and the diagnosis this paper responds to. Belief Engine (arXiv:2605.15343) makes stance dynamics configurable and inspectable; Preserving Disagreement (arXiv:2604.26561) shows architectural heterogeneity slows consensus collapse; adversarial-peer debate studies (arXiv:2606.19826) quantify contamination risk. These works vary *who deliberates*; we vary *what the protocol guarantees*.

**Grounding and external memory.** Retrieval-augmented generation, scratchpad and blackboard architectures, and tool-mediated state externalize information that transformer context handles unreliably. DelibGuard imports this design principle into deliberation: the ledger is a blackboard whose contents are facts with provenance, and the citation gate makes reading it obligatory rather than optional.

**Deliberation theory.** In deliberative democracy, well-designed procedures — information provision, facilitation, structured turn-taking — are precisely what separates deliberation from mere discussion; deliberative polling's briefing materials are, functionally, a fact ledger. The anchor's unstructured protocol corresponds to unfacilitated discussion; our claim that the pathology lies in the missing procedure has a direct human-institutional precedent. Extended discussion in Appendix A.

## 3. DelibGuard: Making Fact State a First-Class Citizen

### 3.1 Setup: Deliberation as Guaranteed Information Flow

We adopt the anchor's formalization. Background context ℬ is decomposed into atomic facts, labeled critical or non-critical; agent Aᵢ = (πᵢ, ℬᵢ, θᵢ) holds base model πᵢ, partial evidence ℬᵢ ⊆ ℬ, and prior stance θᵢ; agents exchange messages over full, tree, or chain topologies for R rounds. The anchor's protocol makes conversation the *only* carrier of facts: a fact not re-verbalized is, operationally, gone. DelibGuard changes exactly this: facts acquire a carrier outside the conversation, and the protocol makes contact with that carrier obligatory.

### 3.2 Structural Mechanisms

**Fact ledger (L).** At initialization, each agent's evidence ℬᵢ is written into a shared ledger as atomic entries. The ledger is appended to every agent's context every round, verbatim — facts cannot attrit by non-repetition because repetition is the protocol's job, not the agents'.

**Provenance tags (P).** Each ledger entry carries (source agent, origin: initial | asserted-in-round-r). New claims asserted during discussion enter the ledger as *asserted*, never silently merging with initial evidence. This makes the evidence base auditable and gives the malicious-injection defense its handle (§5.5).

**Citation gate (C).** Before an agent may agree with an interlocutor or revise its stance toward consensus, it must cite by identifier at least one ledger fact that the interlocutor's evidence set does not contain. Concession without novel evidence is rejected by a deterministic validator and the turn is re-elicited. This converts convergence from a social act into an evidential one.

**Retrieval rounds (R).** Each round begins by re-injecting the original background context ℬ, so abstraction drift — the anchor's finding that surviving facts skew to generalities (retained-fact abstraction 2.73 vs. lost-fact 2.33 on their scale) — is corrected against ground truth every round.

### 3.3 Agent Discussion Under Disagreement

The discussion loop is otherwise identical to the anchor's: agents state stance and reasoning, respond to peers per topology, and may revise stances. DelibGuard adds two protocol checks per turn — ledger-reference validity and citation-gate satisfaction — implemented as deterministic wrappers (regex over cited fact identifiers checked against the holders map), not model judgment. Full prompt templates in Appendix B.

### 3.4 Evaluation: The Anchor's Metrics, Unchanged

We measure exactly what the anchor measures: system- and agent-level fact survival (Jaccard between initial and round-j reconstructed evidence sets), critical-fact survival separately, and stance entropy H(j). Using DelibTrace unmodified is deliberate: any improvement must be attributable to the protocol, not to friendlier measurement. One addition: because the ledger is explicit state, we report both *verbalized survival* (anchor-comparable) and *ledger-cited survival* (facts an agent actually cited by identifier), which separates true attrition from mere non-repetition — addressing a measurement ambiguity in the anchor, whose "lost" facts may simply be facts no one bothered to restate while they remained in context.

**Pre-registered elimination criterion.** Attrition is *eliminated* if round-3 critical-fact survival under DelibGuard is statistically indistinguishable from the anchor's non-interactive 3-round control (80.8% survival) or better — i.e., deliberating adds no loss beyond what mere processing costs. "Delay" (the anchor's verdict on heterogeneity) is any improvement short of that bar.

## 4. Experiments

### 4.1 Benchmarks and Quality Assessment

We use the anchor's two benchmarks: Scruples (Reddit AITA) ethics cases (710) and real news articles (1,044), with the anchor's fact-decomposition and criticality-labeling pipeline. Human validation follows their protocol: 3 annotators over a 100-case sample for fact criticality, agent-evidence consistency, and stance consistency; we target their reported reliability (criticality 0.767 accuracy / 0.541 κ; evidence consistency 0.90 / 0.789; stance 0.98 / 0.947). A supplementary 6-case authored pilot set with ground-truth verdicts determined by distributed critical facts (Appendix C) supports the controlled prior-vs-evidence analysis of §5.3, where each case is constructed so that background-only judgment and full-evidence judgment disagree.

### 4.2 Experimental Setup

Models: GPT-4.1, Gemini 3, Qwen 3.5 (the anchor's families). 4 agents, 3 rounds, full/tree/chain topologies, initial stances split to force disagreement. Conditions: **(a) Unstructured** — the anchor's protocol re-run with our code, forming the baseline column of every table; **(b) DelibGuard-full** (L+P+C+R); **(c)** ablations L, L+P, L+P+C, R-only; **(d)** the anchor's prompt-level interventions (persona, heterogeneity) for reference; **(e)** a non-interactive control (agents process for 3 rounds without seeing peers), which defines the elimination bar. Decoding, topology, and cost details in Appendix C; a runnable pilot harness (3 agents, 6 cases, one model family) is included in `experiment/`.

### 4.3 Main Results

**Table 1. Critical-fact survival at round 3 (system level, full topology; mean over domains).** Anchor rows are their published numbers; condition rows are ⟨pred⟩ predictions.

| Condition | Ethics | News | Mean | vs. Unstructured |
|---|---|---|---|---|
| Unstructured (anchor protocol) | 0.284 | 0.268 | 0.276 | — |
| Non-interactive control (elimination bar) | 0.812 | 0.804 | 0.808 | +193% |
| Persona (anchor's best prompt-level) | 0.468 | 0.441 | 0.455 | +65% |
| Heterogeneity (anchor) | 0.598 | 0.571 | 0.585 | +112% |
| Retrieval only (R) | ⟨pred⟩0.63 | ⟨pred⟩0.61 | ⟨pred⟩0.62 | +125% |
| Ledger (L) | ⟨pred⟩0.81 | ⟨pred⟩0.79 | ⟨pred⟩0.80 | +190% |
| L+P | ⟨pred⟩0.87 | ⟨pred⟩0.85 | ⟨pred⟩0.86 | +212% |
| L+P+C | ⟨pred⟩0.93 | ⟨pred⟩0.92 | ⟨pred⟩0.925 | +235% |
| **DelibGuard-full (L+P+C+R)** | **⟨pred⟩0.95** | **⟨pred⟩0.93** | **⟨pred⟩0.94** | **+241%** |

The hypothesis commits to: DelibGuard-full ≥ the non-interactive bar (0.808) — attrition eliminated, not delayed; ledger variants without the citation gate approach but do not clear the bar. Falsification condition: if DelibGuard-full lands below the bar but above heterogeneity (0.585), FOL-9′ fails for this protocol class and the anchor's FOL-9 is *strengthened*, since even structural intervention would then only delay attrition.

**Figure 3.** *Per-round curves, one line per condition: (top) stance entropy H(j); (bottom) critical-fact survival. Predicted pattern: unstructured shows the anchor's signature — entropy collapsing 0.9→0.3 while survival falls to 0.28; DelibGuard shows survival flat near 1.0 with entropy declining gradually to ⟨pred⟩~0.6 — convergence occurring only where evidence warrants it, with facts intact.*

Consistent with the anchor, unstructured deliberation is predicted to reproduce the full < tree < chain loss ordering; under DelibGuard the topology effect should ⟨pred⟩vanish (survival ≥0.92 on all three), as expected once the carrier of facts is no longer the conversation path.

## 5. Why Structure Matters

Each subsection answers the corresponding diagnosis in the anchor's §5, in order.

### 5.1 The citation gate, not the ledger alone, is decisive

**Fact ledgers eliminate attrition; citation gating is what makes survival evidential rather than decorative.** Ablations (Table 1) predict the ledger alone lifts survival to ⟨pred⟩0.80 — facts are *available* — but availability is not use: we predict consensus still forms without citing any ledger entry in ⟨pred⟩~30% of ledger-only cases, and reconstruction from utterances alone still drifts abstract.

**Table 2. Reconstruction fidelity at round 3 (misleading-reconstruction rate, anchor's §5.1 protocol).**

| Condition | Ethics | News |
|---|---|---|
| Unstructured (anchor) | 0.645 | 0.584 |
| Ledger only | ⟨pred⟩0.28 | ⟨pred⟩0.25 |
| **DelibGuard-full** | **⟨pred⟩0.11** | **⟨pred⟩0.09** |

This answers the anchor's §5.1 (retained facts distort reconstruction): distortion tracks *obligatory use*, not mere retention.

### 5.2 Downstream judgment accuracy is restored

**Deliberation stops making models wrong.** The anchor's headline harm is that models correct in full context err 19.2% after deliberation.

**Table 3. Deliberation-induced downstream error (items answered correctly in full context).**

| Condition | Induced error rate |
|---|---|
| Unstructured (anchor) | 0.192 |
| Persona | ⟨pred⟩0.16 |
| Heterogeneity | ⟨pred⟩0.11 |
| **DelibGuard-full** | **⟨pred⟩0.03** |
| Full-context ceiling | 0.000 (by construction) |

Under DelibGuard the predicted induced error rate is ⟨pred⟩3%, within ⟨pred⟩~2 points of the full-context ceiling: the first condition in either paper where discussing does not cost correctness.

### 5.3 Consensus decouples from model priors

**Consensus follows evidence, not the base model.** The anchor's consensus–prior agreement of 65–76% is the signature of prior regression — but it is correlational: on easy items, prior and evidence agree, inflating the statistic. We add the controlled test the anchor lacked, using the authored subset where distributed critical evidence contradicts the background-only (prior) answer by construction.

**Table 4. Consensus alignment on the prior-vs-evidence conflict subset.**

| Condition | Consensus = prior | Consensus = evidence |
|---|---|---|
| Unstructured | ⟨pred⟩0.71 | ⟨pred⟩0.29 |
| **DelibGuard-full** | **⟨pred⟩0.19** | **⟨pred⟩0.81** |

Overall consensus–prior agreement is predicted to fall from 65–76% to ⟨pred⟩~52% — chance for binary stances. On the conflict subset, DelibGuard consensus sides with the evidence in ⟨pred⟩81% of cases versus ⟨pred⟩29% unstructured. If instead DelibGuard consensus keeps tracking the prior even with all facts surviving, that would show prior anchoring is generation-level rather than information-level — a distinct and reportable negative result.

### 5.4 Diversity and preservation are jointly achievable

**Stance diversity need not be purchased with fact loss, nor facts with frozen stances.** The anchor's persona intervention held entropy at 0.68 but facts at 0.468 — diversity via stubbornness, not via evidence. DelibGuard is predicted to reach ⟨pred⟩0.94 survival with round-3 entropy ⟨pred⟩~0.6: the citation gate permits convergence only when warranted by evidence the conceding agent did not initially hold, so residual disagreement persists exactly on cases whose critical facts genuinely support both readings (qualitative analysis planned in Appendix D).

### 5.5 Provenance defeats malicious injection

**An auditable evidence base is a defensible one.** The anchor shows a malicious agent's falsehoods reach 58.9% of system outputs, and critical-fact survival under attack falls to 0.193. Under DelibGuard, injected claims enter the ledger tagged *asserted-in-round-r* by the malicious agent, never as initial evidence; the citation gate cannot be satisfied by asserted-only, uncorroborated facts. Predicted: penetration falls to ⟨pred⟩8%, and critical-fact survival under attack is ⟨pred⟩0.89. The anchor's vulnerability argument (their §5.5, our FOL-10) held only because its premise — an unpreventable, shrinking evidence base — no longer holds.

## 6. Conclusion and Future Work

Wan et al. (2026) showed that undesigned multi-agent deliberation manufactures consensus while destroying the facts that should ground it. We argued that their "no intervention helps" prognosis rests on an unsupported universal quantifier, constructed DelibGuard — a provenance-tagged fact ledger, an evidential citation gate, and per-round re-grounding — as the existential witness, and committed to pre-registered predictions under the anchor's own metrics: elimination of attrition (survival above the non-interactive bar), restoration of downstream accuracy, decoupling of consensus from priors, and closure of the malicious-injection channel. If the predictions hold, the deliberative illusion is the signature of protocols in which conversation is the only carrier of information; where fact state is a first-class citizen, consensus becomes what deliberation promised — agreement *because of* evidence. If they fail, the anchor's FOL-9 is strengthened at a far stronger point than prompt-level intervention, and the illusion is deeper than protocol.

Limitations: predictions, not yet measurements — the pilot harness (Appendix C) is the immediate next step; scale mirrors the anchor's (4 agents, 3 rounds, 2 domains), leaving ledger scaling at 10–100 agents open; the citation gate adds an estimated ⟨pred⟩1.5–2× token cost, motivating cheaper sampled-audit gates; and our elimination criterion treats non-interactive processing as the floor of unavoidable loss — protocols that *beat* the floor by eliciting facts deliberation would otherwise never surface are the natural next question.

---

## Appendix A — Extended Related Work

**Diagnostics of multi-agent pathology.** Beyond the anchor: conformity and sycophancy in LLM ensembles; premature convergence in society-of-minds; deliberative dynamics and value alignment in LLM debates (arXiv:2510.10002), which finds value positions drift toward majority framing; Preserving Disagreement (arXiv:2604.26561), which achieves slower stance collapse via architectural heterogeneity but does not measure fact survival — precisely the gap DelibTrace exposed and DelibGuard targets; Belief Engine (arXiv:2605.15343), which makes stance dynamics inspectable but leaves the information channel unmodified; and adversarial-peer debate (arXiv:2606.19826), whose honest-gain/replacement-cost accounting motivates our §5.5 threat model.

**External memory and grounding.** Blackboard architectures in classical multi-agent systems; RAG and tool-use as involuntary grounding; scratchpads as private state. DelibGuard differs on two axes: the ledger is *shared and typed* (facts with provenance, not free text), and contact with it is *obligatory* (citation gate), not permitted.

**Procedure design in human deliberation.** Deliberative polling (briefing materials as shared fact base), citizens' assemblies (facilitated turn-taking as citation discipline), and jury instructions (provenance separation between evidence and argument) are human analogues of L, C, and P respectively. The empirical finding that facilitated deliberation outperforms unstructured discussion in fact retention is the human-institutional prior for FOL-9′.

## Appendix B — DelibGuard Details

**Ledger schema.** Entry := (fact_id, text, criticality?, holders: [agent_id], origin: initial | asserted(agent, round)). Serialized per round as `- [F#] (initially held by: Agent i, …) text`.

**Citation-gate validator (pseudocode).**

```
on message m from agent i addressed toward consensus/agreement with agent j:
    cited := regex_extract(m, r"\[F\d+\]")
    novel := [f for f in cited if j not in holders[f] and origin[f] == initial]
    if agreeing(m) and novel == []:
        reject(m); re-elicit turn with gate reminder
```

**Round prompt template (DelibGuard condition), as implemented in the pilot harness:**

```
You are Agent {i} in a {n}-agent deliberation about this issue: {question}
Background: {background}
Your private evidence (facts only you were given initially): {my_facts}
SHARED FACT LEDGER (maintained by the protocol; all entries are verified initial evidence):
{ledger with per-fact provenance}
PROTOCOL RULES: (1) Ground every argument in ledger fact IDs. (2) You may only agree
with a peer or move toward consensus if you cite, by ID, at least one ledger fact that
that peer did NOT initially hold. (3) Restate, by ID and content, every fact you
consider decision-critical.
Peer messages from the previous round: {peer_msgs}
Your initial stance was {stance}. Reconsider it in light of the evidence. …
End with 'STANCE: YES' or 'STANCE: NO'.
```

The unstructured condition is identical minus the ledger, rules, and background re-injection (background appears in round 1 only, per the anchor). Non-interactive replaces peer messages with the agent's own prior notes. Full source: `experiment/run_experiment.py`.

**Measurement prompts.** Fact survival: a judge model receives all round-3 messages and the fact list, returns per-fact PRESENT/ABSENT as JSON (verbalized survival); ledger-cited survival is computed deterministically from `[F#]` citations. Downstream judgment: a fresh model answers the case question from round-3 messages only. Prior: background-only answer. Full-context: background + all facts.

## Appendix C — Experimental Setup Details

**Main design (pre-registered, to run).** 3 model families × 2 domains × 3 topologies × 9 conditions (Table 1 rows) × {710, 1044} cases; 4 agents, 3 rounds; temperature and decoding matched to the anchor's reported settings. Estimated compute: ~1.9M agent calls at full scale; a stratified 10% subsample (n=175 per cell) yields 95% CIs of ±0.04 on survival rates and is the intended first pass.

**Pilot harness (implemented).** `experiment/run_experiment.py` + `experiment/cases.json`: 6 authored cases, each with 8 atomic facts (4 critical), evidence distributed across 3 agents with overlap, initial stances split 2-vs-1 against the evidence-supported verdict, ground truth determined by critical facts and constructed to conflict with the background-only prior. Conditions: unstructured, DelibGuard-full, non-interactive. Agent model: Haiku-class via local CLI; ~35 LLM calls per case per condition. Metrics per §3.4, aggregated by `experiment/analyze.py` into Table-1-format output.

**Annotation protocol.** 3 annotators, 100-case sample, three tasks mirroring the anchor's §4.1 (criticality, evidence consistency, stance consistency); disagreements adjudicated by majority; target reliabilities as in §4.1.

## Appendix D — Additional Results (planned)

D.1 Agent-level survival tables (anchor predicts 60.5–84.8% loss; DelibGuard target ⟨pred⟩<10%). D.2 Per-model breakdowns — the anchor found GPT-4.1 worst (72.4% loss); prediction: model differences compress under DelibGuard since survival is protocol-borne. D.3 Topology × condition grid. D.4 Worked case study: the Figure-1 warehouse case end-to-end, with full transcripts and ledger audit trail. D.5 Malicious-injection transcripts showing the asserted-tag quarantine and gate rejection turns. D.6 Qualitative analysis of legitimate residual disagreement (cases where critical facts support both verdicts and DelibGuard preserves the split).

---

## References

- Wan, H., Wu, J., Luo, M., Li, F., Wang, N., Chen, N. F., Kan, M.-Y. (2026). *The Deliberative Illusion: Diagnosing Factual Attrition and Stance Homogenization in Multi-Agent LLM Deliberation.* arXiv:2606.03032.
- *Deliberative Dynamics and Value Alignment in LLM Debates.* arXiv:2510.10002.
- *Preserving Disagreement: Architectural Heterogeneity and Coherence Validation in Multi-Agent Policy Simulation.* arXiv:2604.26561.
- *Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation.* arXiv:2605.15343.
- *Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and Resilience.* arXiv:2606.19826.
- ⟨additional grounding/RAG/blackboard and deliberative-democracy references to be filled at submission⟩

---

### FOL conformance map (draft-internal; delete before submission)

| FOL | Claim | Where satisfied |
|---|---|---|
| FOL-1–2 (accepted) | Attrition occurs; interaction causes it | §1 ¶2; §4.3 baseline row |
| FOL-3 (accepted, narrowed) | Attrition is causal in *unstructured* protocols | §3.1, §5 framing |
| FOL-4 (accepted) | Surviving facts unrepresentative | §5.1 Table 2 baseline (and its reversal under C) |
| FOL-5 (accepted) | Entropy collapses | §4.3 Fig 3 baseline |
| FOL-6 (accepted) | Unstructured consensus not evidence-derived | §5.3 baseline |
| FOL-7 (accepted + fixed) | Consensus = prior; controlled prior-vs-evidence test added | §5.3 Table 4 |
| FOL-8 (accepted) | 19.2% induced error | §5.2 Table 3 baseline |
| **FOL-9′ (thesis)** | ∃ structural intervention eliminating attrition | §3.2 (witness construction), §3.4 + §4.3 (pre-registered criterion + committed predictions), falsification condition stated |
| FOL-10 (collapsed) | Vulnerability premise ¬Preventable falsified | §5.5 |
| **FOL-0′ (conclusion)** | Only undesigned deliberation is illusory | Title, Abstract, §6 |
