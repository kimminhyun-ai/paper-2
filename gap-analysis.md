# Gap Analysis: paper-draft.md vs. 앵커 논문 (arXiv:2606.03032)의 실제 형식

2026-07-21. 앵커 논문 원문의 형식 관행을 재조사한 결과와, 현재 초고(v0.2)가 미달하는 지점 전수 목록. 심각도: 🔴 치명(리뷰어 즉시 지적) / 🟡 중요 / 🟢 경미.

## 1. 🔴 문장 내 인용(in-text citation) 부재

**앵커**: 저자-연도 괄호 인용을 문단당 2–3개 밀도로 사용. Introduction 첫 문단부터 주장마다 인용이 붙음:
> "Multi-agent LLM systems make interaction part of the inference process (Wu et al., 2024; Feng et al., 2025a). By exchanging partial evidence... (Chen et al., 2024; Du et al., 2024; Liang et al., 2024)"

**현재 초고**: Introduction·Related Work의 거의 모든 주장이 무인용. "debate and society-of-minds architectures report gains" 같은 문장은 앵커라면 3개 인용이 붙을 자리인데 0개. 관련 논문도 "(arXiv:2604.26561)" 같은 raw ID 표기 — 학술 논문에서 쓰지 않는 형식.

**수정 방향**: 전 문장 감사 후 저자-연도 인용 삽입. 인용 필요 문장 추정 ~35곳. 실제 서지(bib) 확보 필요 — Du et al. 2024 (multiagent debate), Liang et al. 2024 (divergent thinking), Wu et al. 2024 (AutoGen) 등 앵커의 참고문헌을 재사용할 수 있음.

## 2. 🔴 References 섹션이 논문 수준이 아님

**앵커**: 수십 개의 완전한 서지 항목. **현재**: 6개, 그중 1개는 "⟨to be filled⟩" placeholder, 나머지도 저자·연도 불완전(arXiv 번호만). Related Work·§2에서 언급한 개념들(RAG, blackboard, deliberative polling, conformity cascades)의 원전이 전부 누락.

## 3. 🔴 형식 표기(notation)의 비일관/미정의

**앵커**: 텍스트 inline이지만 기호를 체계적으로 선언 — ℐ=(ℬ,q) (deliberation object), 𝒮=(𝒜,𝒢), 원자 사실 c_i, Aᵢ=(πᵢ,ℬᵢ,θᵢ), 토폴로지 𝒢, Jaccard 기반 생존 지표와 엔트로피 H(j)를 수식으로 제시.

**현재**: §3.1에서 앵커 표기를 "채택한다"고만 말하고 ℐ, q, 𝒢, c_i를 실제로 선언하지 않음. DelibGuard 자체의 형식화도 없음 — ledger L, 검증기, citation gate를 집합/함수로 정의해야 함 (예: L ⊆ ℬ × Prov, gate: M × L → {accept, re-elicit}). 생존 지표·엔트로피 수식 미기재.

## 4. 🔴 Table 1의 구조가 앵커와 비교 불가능한 수준으로 축약됨

**앵커 Table 1**: 모델(3) × 토폴로지(Full/Tree/Chain) × 라운드(Pre/1/2/3) 전개, 각 셀에 Sys. Ret.↑ / Agent Ret.↑ 분리, 도메인별 Critical/All 분리, 라운드 간 변화량을 아래첨자(".790₋.₂₁₀")로 표기, 최종 라운드 급락은 볼드 적색.

**현재 Table 1**: 조건 × 도메인 평균 단일 수치. 모델별·라운드별·토폴로지별·agent-level 분해 전무. "직접 비교 가능"이 이 논문의 방법론적 셀링포인트인데 표 구조 자체가 비교 불가능.

**수정 방향**: 앵커 Table 1과 동일한 행렬 구조로 재설계하고 조건(개입) 축을 추가. 분량상 본문에는 Full 토폴로지 × DelibGuard-full/unstructured, 나머지는 부록.

## 5. 🟡 RQ 라벨 부재

**앵커 §5**: "RQ1: Reconstruction Fidelity (§5.1)... RQ2: Judgment Impact..." 형태로 5개 RQ를 명시적 라벨링. **현재 §5**: 볼드 선언문만 있고 RQ 구조 없음. skill의 1:1 대구 원칙을 살리려면 RQ1′–RQ5′로 라벨링하는 것이 오히려 대구를 명시화함.

## 6. 🟡 통계 처리 부재

**앵커**: 표준편차를 부록 Table 7에 별도 보고, 핵심 주장에 p<0.005 명시, 인간 주석 κ 보고. **현재**: 예측치라 분산이 없는 건 당연하나, *측정 후 무엇을 보고할지*(SD 부록 표, 유의성 검정 계획, CI)의 자리 자체가 설계에 없음. §4.2에 10% 서브샘플 CI ±0.04 한 줄이 전부.

## 7. 🟡 코드/데이터 공개 각주 부재

**앵커**: Abstract 각주로 GitHub 링크 명시 ("Code and data are available on GitHub"). **현재**: 리포가 실제로 존재하고 public인데(github.com/kimminhyun-ai/paper-2) 논문에 링크가 없음. 가장 고치기 쉬운 항목.

## 8. 🟡 Figure 번호 불일치 및 Figure 2 실종

**현재 초고**: Figure 1 다음에 Figure 3이 등장. v0.1에 있던 Figure 2(프레임워크 개요 다이어그램)가 v0.2에서 누락됐는데 번호는 그대로 3을 사용. 앵커는 Fig 2가 DelibTrace 개요 다이어그램 — 우리도 DelibGuard 개요(ledger/gate/retrieval 파이프라인) 다이어그램이 §3에 필요.

## 9. 🟡 부록 밀도 격차

**앵커**: 부록에 Table 7(표준편차), 추가 그림 4개+, 사례 연구 전문, 프롬프트 전문. **현재**: 부록 B(프롬프트)는 실체가 있으나 A는 서지 없는 요약문, D는 "planned" 목록만. 앵커 부록 A는 관련 연구를 인용과 함께 수 페이지 전개.

## 10. 🟢 앵커가 하지 않는 것 (따라하지 않아도 되는 것)

- 형식적 Definition/Theorem 환경 없음 → 우리도 불필요 (FOL 사슬을 본문에 그대로 넣지 않은 것은 올바른 선택; 다만 §1의 ∀/∃ 문장은 앵커에 없는 장치로, 차별점으로 유지 가능)
- 수식 번호 없음, 각주 최소, 윤리 성명 없음 → 현재 초고와 동일, 문제없음

## 11. 🟢 구조적으로는 준수된 것

섹션 트리(§1–6 + App A–D), Abstract 문장 수·순서, Intro 문단 흐름, §5의 볼드 선언문 오프닝, 앵커 §5와의 1:1 대응, 사전등록/반증조건 프레임 — 이상은 앵커 관행과 일치하거나 상회.

## 근본 격차 (형식 이전의 문제)

앵커는 **측정된 논문**이고 현재 초고는 **사전등록된 예측**. 인용·표·통계를 모두 고쳐도 이 격차는 남는다. 현재 문서의 정체는 "논문"이라기보다 "registered report의 Stage-1 원고"이며, 제출 가능 상태가 되려면 (a) 실험 실행으로 ⟨pred⟩ 교체, (b) 위 1–9 수정이 모두 필요.

## 우선순위 수정 계획

1. 인용 감사 + 실제 서지 구축 (앵커 참고문헌 재사용, ~35곳 삽입) — 🔴1,2
2. §3 형식화: ℐ, 𝒮, L, gate, 생존 지표·엔트로피 수식 — 🔴3
3. Table 1 재설계 (모델 × 토폴로지 × 라운드 × Sys/Agent) — 🔴4
4. RQ1′–5′ 라벨, Fig 2 복원·번호 정리, GitHub 각주, 통계 보고 계획 — 🟡5–8
5. 부록 A 확장(서지 포함), 부록 D 구체화 — 🟡9
