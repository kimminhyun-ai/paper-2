---
name: paper-writing
description: 앵커 논문(The Deliberative Illusion, arXiv:2606.03032)의 구조를 따라 후속 논문(FOL-9′ 반박 논문)을 작성한다. 논문 섹션 작성, abstract/intro 작성, 구조 설계 요청 시 사용.
---

# Paper Writing Skill — Anchor: "The Deliberative Illusion" (arXiv:2606.03032)

이 skill은 앵커 논문의 구조·문체·밀도를 그대로 재현하여 후속 논문을 작성하기 위한 템플릿이다.
논증 내용은 `FOL-new-paper.md`(핵심 가설 FOL-9′, 결론 FOL-0′)를 따르고, 형식은 아래를 따른다.

## 0. 논문의 정체성

- **앵커 논문**: 진단 논문 — "숙의는 환상이다" (문제 발견형)
- **새 논문**: 반박+구성 논문 — "환상은 프로토콜 부재다" (해결 제안형)
- 앵커의 구조를 미러링하되, Section 5의 "진단"을 "개입 효과 분해"로 치환한다.
- 한 줄 thesis: *설계되지 않은 숙의만이 환상이다 (FOL-0′)*. 모든 섹션은 이 문장을 지지해야 한다.

## 1. 전체 섹션 구조 (앵커 미러링)

```
1  Introduction
2  Related Work                       (3–4문단, 핵심 문헌만; 상세는 Appendix A)
3  <FrameworkName>: <부제>            (방법론, 4개 서브섹션)
   3.1  Setup: 문제의 형식화
   3.2  구조적 개입의 정의 (fact ledger / provenance / 인용 강제 / retrieval 라운드)
   3.3  개입 하의 숙의 프로토콜
   3.4  Evaluation: DelibTrace 지표 재사용 (사실 생존 Jaccard, 입장 엔트로피)
4  Experiments
   4.1  Benchmarks and Quality Assessment   (앵커와 동일 데이터: Scruples 710, News 1,044)
   4.2  Experimental Setup                  (모델 3계열, 4 에이전트, 3 라운드, 토폴로지 3종)
   4.3  Main Results                        (개입별 attrition 제거율 — Table 1)
5  <Diagnosing 대응 섹션>: Why Structure Matters
   5.1  어떤 개입이 무엇을 구하는가 (ablation: ledger vs provenance vs 인용 강제)
   5.2  Downstream 판단 정확도 회복 (앵커의 19% 오답 → 얼마나 복구되는가)
   5.3  합의-prior 일치율 변화 (앵커의 65–76% → 증거 추종으로 전환되는가)
   5.4  입장 다양성과 사실 보존의 동시 달성 여부
   5.5  악의적 주입 하 강건성 (앵커의 58.9% 침투 → 방어되는가)
6  Conclusion and Future Work         (2–3문단)
Appendix A  Related Work 상세
Appendix B  프로토콜/프레임워크 상세 (프롬프트 전문 포함)
Appendix C  실험 설정 상세
Appendix D  추가 정량·정성 결과 (사례 연구 포함)
```

핵심 대응 원칙: **앵커의 Section 5 각 서브섹션(5.1–5.5)이 제기한 문제를 새 논문의 5.1–5.5가 1:1로 응답한다.** 리뷰어가 두 논문을 나란히 놓고 읽을 수 있는 구조가 목표.

## 2. Abstract 공식 (8–9문장, 앵커 미러링)

1. 배경: 다중 에이전트 숙의와 앵커 논문의 deliberative illusion 진단 소개
2. 문제 진술: 그러나 그 결론("완화 불가")은 프롬프트 수준 개입 2종에서만 귀납됨
3. 핵심 주장: 구조적 개입은 attrition을 지연이 아니라 제거할 수 있다 (가설)
4. 방법론: 프레임워크 이름 + 4가지 구조적 개입 한 문장 요약
5. 정량 결과 1: critical fact 생존율 (앵커의 27.6% → X%)
6. 정량 결과 2: downstream 정확도/prior 일치율/주입 방어율 중 최강 수치
7. 함의: 환상은 숙의의 본질이 아니라 프로토콜의 부재
8. 결론 문장: 앵커의 "consensus-centric evaluation is unreliable"에 대구를 이루는 한 문장
9. (선택) 권장사항: 숙의 시스템 설계 시 사실 상태를 1급 시민으로 다뤄야 함

## 3. Introduction 문단 흐름 (8–9문단, 앵커 미러링)

1. 배경: 다중 에이전트 LLM 시스템의 확산과 숙의에 대한 기대
2. 앵커 논문의 진단 소개: factual attrition + stance homogenization (수치 인용: 72%, 3.5배)
3. 문제 제기: 앵커의 "완화 불가능" 결론의 논리적 틈 — ∀ 주장을 프롬프트 수준 개입 2개로 귀납
4. 핵심 질문: 숙의의 *구조*를 바꾸면 attrition이 제거되는가?
5. 용어/개념 정의: structural intervention vs prompt-level intervention 구분
6. **Figure 1**: 동일 사례(UBI류)에서 기본 숙의 vs 구조적 개입 숙의의 사실 생존 비교 시각화
7. 프레임워크 소개: 4가지 개입 + DelibTrace 지표 재사용으로 직접 비교 가능함을 강조
8. 주요 결과 요약: 핵심 수치 3개 (생존율, downstream 정확도, 주입 방어)
9. 함의: FOL-0′ — 환상은 설계 결함이며, contribution 목록 (보통 3–4개 bullet)

## 4. Figure/Table 계획 (앵커 미러링)

| 위치 | 항목 | 내용 |
|------|------|------|
| Intro | Fig 1 | 사례 비교: 무개입 vs 개입 숙의의 사실 생존 (앵커 Fig 1의 대구) |
| Intro/§3 | Fig 2 | 프레임워크 개요 다이어그램 (앵커 Fig 2의 대구) |
| §4.3 | Table 1 | 주 결과표: 개입 × 모델 × 도메인별 critical fact 생존율 (앵커 Table 1과 동일 포맷 — 직접 비교 열 포함) |
| §4.3 | Fig 3 | 라운드별 입장 엔트로피 + 사실 생존 추이 (개입별 곡선) |
| §5 | Table 2–4 | ablation, downstream 정확도, prior 일치율 |
| §5.5 | Fig 4 | 악의적 주입 하 침투율 비교 |
| Appendix | Fig 5–9 | 사례 연구, 프롬프트, 추가 분석 |

**규칙**: 앵커와 수치가 직접 비교되는 표에는 반드시 앵커의 원 수치를 재현(re-run) 열로 포함한다. 인용 수치가 아니라 동일 코드로 재측정한 baseline이어야 함.

## 5. 문체 규칙

- 시제: 방법·결과는 현재형 ("We introduce…", "Discussion erases…" 스타일)
- 앵커의 명명 관행을 따름: 프레임워크에 고유명 부여 (DelibTrace처럼 CamelCase 한 단어), 현상에 2단어 학술 용어 부여
- 수치는 본문 문장 안에 삽입 (예: "preserving 94.2% of critical facts, versus 27.6% without intervention")
- 각 결과 서브섹션은 **볼드 선언문으로 시작**하는 앵커 스타일: "**Retained facts distort reconstruction.**" → 새 논문: "**Fact ledgers eliminate attrition, not merely delay it.**"
- 주장 강도 관리: 실험이 지지하는 범위까지만. ∃ 가설이므로 "in at least one protocol class"류의 한정을 명시
- 앵커 논문은 존중하며 인용: 반박 대상은 그들의 *일반화*이지 *측정*이 아님. §2와 §5에서 "their diagnosis is correct; their prognosis is not" 프레임 유지

## 6. 작성 순서 (권장 워크플로)

1. Table 1 스켈레톤(측정할 수치의 자리)부터 확정 — 실험이 채울 칸을 먼저 정의
2. §3 방법론 → §4 실험 → §5 분석 → §1 Intro → Abstract → §2 Related Work → §6 Conclusion
3. 각 섹션 완성 시 체크: (a) FOL-0′를 지지하는가 (b) 앵커의 대응 섹션과 1:1 대구인가 (c) 볼드 선언문 규칙을 지켰는가

## 7. 참조 파일

- 앵커 논문 PDF: `deliberative-illusion-2606.03032.pdf`
- 앵커 FOL 사슬: `FOL-original-paper.md`
- 새 논문 논증: `FOL-new-paper.md` (FOL-9′, FOL-0′)
