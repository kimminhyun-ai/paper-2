# 기존 논문의 FOL: The Deliberative Illusion (Wan et al., 2026, arXiv:2606.03032)

논문의 논증을 단계적 연역 사슬(FOL-0 ~ FOL-10)로 형식화한다.

## FOL-0 (최종 결론)

> **∀d [ MultiAgentDeliberation(d) → ( ReachesConsensus(d) ∧ ¬GroundedInEvidence(Consensus(d)) ) ]**

모든 다중 에이전트 숙의는 합의에 도달하지만, 그 합의는 증거에 근거하지 않는다 — 숙의는 환상이다.

## 연역 사슬

**FOL-1 (관찰 전제 ①: 사실 소실)**

> ∀d ∀f [ (Deliberation(d) ∧ CriticalFact(f,d)) → P(Lost(f, FinalRound(d))) ≥ 0.22 ]

모든 숙의에서 판단에 결정적인 사실은 라운드가 진행되며 상당 비율(22–72%) 소실된다.

**FOL-2 (관찰 전제 ②: 소실의 원인은 상호작용)**

> ∀d [ Loss(Interactive(d)) > 3 · Loss(NonInteractive(d)) ]

동일 조건에서 상호작용이 있는 숙의는 없는 경우보다 3배 이상 사실을 소실시킨다.

**FOL-3 (FOL-1 ∧ FOL-2 ⊢ 구조적 내재성)**

> ∀d [ Deliberation(d) → CausallyProduces(d, FactualAttrition(d)) ]

사실 소실이 보편적으로 발생하고(FOL-1) 그 원인이 상호작용 자체이므로(FOL-2), 사실 소실은 우연이 아니라 숙의 구조가 인과적으로 만들어내는 내재적 현상이다.

**FOL-4 (FOL-3 ⊢ 정보 기반의 붕괴)**

> ∀d [ FactualAttrition(d) → ¬Represents(SurvivingFacts(d), Issue(d)) ]

사실 소실이 진행되면(FOL-3), 살아남는 것은 추상적 일반론뿐이어서 최종 라운드의 사실 집합은 원래 이슈를 대표하지 못한다(재구성 시 58–65% 오도적).

**FOL-5 (관찰 전제 ③: 입장 수렴)**

> ∀d [ Deliberation(d) → Entropy(Stances(d,r₃)) < 0.5 · Entropy(Stances(d,r₀)) ]

같은 라운드 동안 입장 분포의 엔트로피는 절반 이하로 감소한다 — 합의가 형성된다.

**FOL-6 (FOL-4 ∧ FOL-5 ⊢ 수렴과 증거의 분리)**

> ∀d [ (Converges(d) ∧ ¬Represents(SurvivingFacts(d), Issue(d))) → ¬DerivedFrom(Consensus(d), Evidence(d)) ]

합의가 형성되는 바로 그 시점에 증거 기반이 이미 붕괴해 있으므로(FOL-4, FOL-5), 그 합의는 증거로부터 도출된 것일 수 없다.

**FOL-7 (FOL-6 ⊢ 수렴의 실제 원천)**

> ∀d ∃m [ ¬DerivedFrom(Consensus(d), Evidence(d)) → Consensus(d) = Prior(m) ]

합의가 증거에서 나온 게 아니라면 다른 원천이 있어야 하는데, 실제로 합의는 65–76% 확률로 기저 모델의 단독 출력과 일치한다 — 수렴의 원천은 모델의 사전 선호다.

**FOL-8 (FOL-7 ⊢ 실질적 해악)**

> ∀d ∀q [ (Consensus(d)=Prior(m) ∧ RequiresEvidence(q)) → P(Incorrect(Consensus(d), q)) ≈ 0.19 ]

합의가 prior의 재표출이므로(FOL-7), 증거가 답을 좌우하는 문제에서는 완전한 맥락이면 맞혔을 모델도 숙의 후 19% 확률로 오답을 낸다.

**FOL-9 (FOL-3 ⊢ 완화 불가능성)**

> ∀i [ (Intervention(i) ∧ ¬Changes(i, Structure(Deliberation))) → ¬Eliminates(i, FactualAttrition) ]

소실이 구조에 내재적이므로(FOL-3), 구조를 바꾸지 않는 개입(페르소나, 모델 이질성)은 소실을 지연시킬 뿐 제거하지 못한다.

**FOL-10 (FOL-4 ∧ FOL-9 ⊢ 취약성이라는 귀결)**

> ∀d ∀a [ (Shrinks(EvidenceBase(d)) ∧ ¬Preventable(FactualAttrition) ∧ Malicious(a,d)) → P(Contains(Output(d), Falsehood(a))) ≥ 0.59 ]

증거 기반이 축소되고(FOL-4) 이를 막을 수도 없으므로(FOL-9), 악의적 에이전트의 거짓 정보는 59% 확률로 시스템 출력에 침투한다 — 근거 없는 합의는 검증력도 없다.

## 사슬 구조

```
FOL-1, FOL-2 (관찰)
   ⊢ FOL-3  소실은 구조에 내재적
   ⊢ FOL-4  → 증거 기반 붕괴
FOL-5 (관찰: 그 와중에 합의 형성)
   ⊢ FOL-6  → 합의는 증거에서 나온 것이 아님
   ⊢ FOL-7  → 합의의 정체 = 모델 prior
   ⊢ FOL-8  → 그래서 실제로 틀린다
FOL-3 ⊢ FOL-9  → 고칠 수도 없다
FOL-4 ∧ FOL-9 ⊢ FOL-10 → 오염에도 무방비다
   ∴ FOL-0  합의는 도달하되 증거에 근거하지 않는다 — 숙의는 환상이다
```

---

*원본 논문 PDF: `deliberative-illusion-2606.03032.pdf` / [arXiv:2606.03032](https://arxiv.org/abs/2606.03032)*
*이 사슬에 대한 반박과 후속 논문의 논증: `FOL-new-paper.md`*
