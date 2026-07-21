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

## 이미지 처리 원칙: 자리만 잡고, 들어갈 이미지를 글로 상세 기술

초안 단계에서 이미지는 제작하지 않는다. 대신 본문의 해당 위치에 figure 블록(자리)을 잡아 두고, 그 자리에 **어떤 이미지가 들어가는지를 캡션과 별도로 상세히 기술**한다. 각 figure 자리에는 다음을 명시할 것: (a) 패널 구성과 레이아웃, (b) 축·범례·단위, (c) 어떤 데이터(어느 표/실험 조건)에서 그려지는지, (d) 독자가 이 그림에서 읽어야 할 한 가지 메시지.

현재 초고의 figure 자리별 명세:

**Figure 1 (§1, 앵커 Fig 1의 대구 — 사례 비교)**
- 레이아웃: 좌우 2패널. 각 패널은 위쪽에 3 에이전트의 라운드별 발화 요약 카드(3열 × 3행), 아래쪽에 라운드별 critical fact 생존 바 차트(x축: Pre/R1/R2/R3, y축: 생존 사실 수 0–4).
- 좌패널(Unstructured): 창고 관리자 해고 사례(부록 D.4)에서 F1–F4 중 R3에 F1만 생존, 발화 카드가 라운드가 갈수록 추상화되는 것을 색 바램(fade)으로 표현, 최종 합의가 증거와 반대(NO)임을 적색 배지로 표시.
- 우패널(DelibGuard): 동일 사례. 패널 우측에 ledger 컬럼(F1–F4 + provenance 태그)을 세로로 배치, R3 발화 카드 안의 `[F#]` 인용을 하이라이트, 바 차트는 4/4 유지, 최종 합의가 증거 지지 방향(YES)임을 녹색 배지로 표시.
- 메시지: "같은 사례, 같은 모델 — 프로토콜만 바꾸면 사실이 살고 결론이 바뀐다."

**Figure 2 (§3, 앵커 Fig 2의 대구 — DelibGuard 개요 다이어그램; 현재 초고에서 실종, 복원 필요)**
- 레이아웃: 좌→우 파이프라인 다이어그램. ① 이슈 분해(ℬ → 원자 사실 c_i, critical 라벨) → ② 에이전트 초기화(Aᵢ=(πᵢ,ℬᵢ,θᵢ), 증거 분배) → ③ 라운드 루프 박스(내부에 4개 구조 메커니즘: Ledger L / Provenance P / Citation gate C / Retrieval R을 아이콘+한줄 설명으로) → ④ 평가(DelibTrace: 생존 Jaccard, H(j)).
- 라운드 루프 박스에서 gate의 reject→re-elicit 화살표를 명시적으로 그릴 것(결정적 검증기임을 시각화).
- 색 규약: 앵커 프로토콜과 동일한 요소는 회색, DelibGuard가 추가한 요소(L/P/C/R)는 강조색 — "무엇이 새로운가"가 색만으로 읽히게.
- 메시지: "대화 바깥에 사실의 운반체를 만들고, 접촉을 의무화한다."

**Figure 3 (§4.3 — 라운드별 동역학 곡선)**
- 레이아웃: 상하 2패널, x축 공유(Pre, R1, R2, R3).
- 상단: 입장 엔트로피 H(j), y축 0–1. 하단: critical fact 생존율, y축 0–1. 조건당 1개 선(unstructured, non-interactive control, persona, heterogeneity, R-only, L, L+P, L+P+C, DelibGuard-full) — 본문 버전은 4개 선(unstructured / non-interactive / heterogeneity / DelibGuard-full)으로 줄이고 전체는 부록.
- 하단 패널에 elimination bar(비상호작용 통제 0.808)를 수평 점선으로 표시하고 라벨링 — 사전등록 기준선이 그림에서 보이게.
- 데이터: Table 1의 라운드별 전개(재설계 후), Full 토폴로지.
- 메시지: "unstructured는 엔트로피 붕괴와 사실 소실이 동시 진행; DelibGuard는 생존 곡선이 기준선 위에 평탄하고 엔트로피는 완만히만 감소."

**Figure 4 (§5.5 — 악의적 주입 방어)**
- 레이아웃: 2패널. 좌: 조건별 거짓 정보 침투율 막대(anchor 58.9% vs DelibGuard ⟨pred⟩8%), 오차막대 자리 포함. 우: 공격 하 critical fact 생존율 막대(anchor 0.193 vs ⟨pred⟩0.89).
- 우패널 위에 미니 다이어그램: 악성 주장 → ledger에 `asserted-in-round-r` 태그로 격리 → gate가 인용 거부하는 3단계 흐름.
- 메시지: "provenance 격리가 공격 표면을 닫는다."

**부록 그림 (D.4–D.6)**
- D.4: Figure 1 사례의 전체 트랜스크립트(3조건)를 라운드별로 병렬 배치한 전면 그림 + ledger 감사 추적 표.
- D.5: 악의적 주입 트랜스크립트 — 주입 발화, ledger 태그 변화, gate reject 턴을 색으로 구분한 대화 흐름도.
- D.6: 정당한 잔여 불일치 사례 — critical fact가 양쪽 판정을 지지하는 사례에서 R3에도 2-vs-1이 유지되는 발화 카드 + 양쪽이 인용한 fact ID 벤 다이어그램.

## 우선순위 수정 계획

1. 인용 감사 + 실제 서지 구축 (앵커 참고문헌 재사용, ~35곳 삽입) — 🔴1,2
2. §3 형식화: ℐ, 𝒮, L, gate, 생존 지표·엔트로피 수식 — 🔴3
3. Table 1 재설계 (모델 × 토폴로지 × 라운드 × Sys/Agent) — 🔴4
4. RQ1′–5′ 라벨, Fig 2 복원·번호 정리(위 "이미지 처리 원칙"의 명세대로 자리+상세 기술), GitHub 각주, 통계 보고 계획 — 🟡5–8
5. 부록 A 확장(서지 포함), 부록 D 구체화 — 🟡9
