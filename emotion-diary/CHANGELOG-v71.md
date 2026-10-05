# 감정일기 v71 변경 사항

v70 리뷰에서 나온 개선점을 반영하고, Part 1 강의 기준(Primitive → Semantic 토큰, 텍스트 스타일, 네이밍 규칙)에 맞춰 정리한 버전입니다.

## 파일

| 파일 | 내용 |
| --- | --- |
| `감정일기_v71.html` | 프로토타입 본체 |
| `design-tokens.css` | 토큰 원본. Primitive(값)와 Semantic(역할) 2단 구조. v71 HTML의 `<style id="design-tokens">`에 그대로 들어감 |
| `tools/build_v71.py` | v70 → v71 변환 스크립트. `python3 tools/build_v71.py <출력.html> <v70 원본.html>` |

## 바뀐 것

### 토큰
- 정적 토큰 파일을 추가했어요. 감정 8색은 `--primitive-rose-400` 같은 Primitive를 `--color-emotion-flutter-fill` 같은 Semantic이 참조해요.
- JS는 이제 색을 들고 있지 않아요. `EMOTION_TOKENS`는 키·라벨·좌표·그룹·세부 톤만 갖고, fill/tint/border/text/glow는 CSS 토큰에서 읽어요.
- hex 뒤에 투명도를 붙이던 코드(`color+"38"`) 11곳을 `EMOTION_TOKENS.alpha(color, 22)`(color-mix)로 바꿨어요.
- 기존 별칭 변수(`--app-ink`, `--app-muted`, `--app-faint`, `--text`, `--text-sub`, `--text-weak`, `--ink`)가 Semantic 텍스트 토큰을 가리키게 했어요.

### 텍스트 · 모서리
- 중립 글자색 812곳을 `--color-text-primary/secondary/tertiary/inverse/disabled` 5개로 정리했어요. tertiary(`#6f6964`)는 캔버스·카드·서브 배경 모두에서 4.5:1 이상이에요.
- font-size 1,278곳을 10단계 스케일(`--font-size-caption-sm` 12px ~ `--font-size-display-lg` 32px)로 바꿨어요. 12px 미만은 없어요.
- font-weight 422곳을 regular 400, semibold 600, bold 700 세 가지로 바꿨어요.
- border-radius 556곳을 `--radius-xs` ~ `--radius-2xl`, `--radius-full`로 바꿨어요.
- 글꼴은 Pretendard를 1순위로 두고, 로드되지 않으면 Apple SD Gothic Neo, Noto Sans KR 순으로 써요.

### 런타임 보정 제거
- `v57-minfont`와 `v66-contrast` 스크립트를 지웠어요. 두 스크립트 없이 19개 화면을 감사한 결과, 대비·최소 크기 위반이 v70 202건에서 v71 0건이 됐어요.
- 선택한 세부 감정 칩의 글자색을 감정 `text` 토큰으로 바꿨어요(기존 3.76:1).

### 버그 · 정리
- 화남의 홈 배경이 기쁨과 같던 문제를 고쳤어요. 이제 화남 팔레트에서 만든 coral → red 배경이에요.
- 날짜는 `APP_DATE`(`today`, `year`, `month`, `weekday`, `label`, `dayInMonth`)로 모았어요. `dayInMonth`는 31일이 없는 달에 다음 달로 넘어가지 않아요.
- 화면에 보이지 않던 감정 기록 카드 규칙 2벌(뒤쪽 `!important`에 덮여 있던 것)을 지우고, 남은 흰 카드 규칙의 색을 `--color-bg-surface`, `--color-border-card` 토큰으로 바꿨어요.
- 쓰이지 않는 `HOME_MATERIALS`와 `__GDEMO`의 중복 `angry` 키를 지웠어요. 별칭 `'모르겠음'`은 기존 `unknown`과 같은 `angry`로 맞췄어요.
- 데모 초기화는 `?demo=0`으로 끌 수 있고, `emotion-app-home-*` 키도 함께 지워요.

## 지표 (v70 → v71)

| 항목 | v70 | v71 |
| --- | --- | --- |
| CSS 선언 중 `var()` 비율 | 2.6% | 22.9% |
| 색상 속성 토큰 사용률 | 10.3% | 45.3% |
| color 리터럴 종류 | 249 | 23 |
| font-size 리터럴 종류 | 39 | 9 (34px 초과 큰 숫자 등) |
| font-weight 리터럴 종류 | 13 | 1 |
| border-radius 리터럴 종류 | 54 | 29 (0, 다중 값, 26px 초과) |
| 12px 미만 font-size 선언 | 562 | 0 |
| 보정 스크립트 없이 대비·크기 위반 | 202 | 0 |
| MutationObserver | 3 | 1 (`v69-fit-viewport`) |
| `!important` | 2,947 | 2,931 |

## 검증
- Chromium 430×900에서 v70과 v71을 같은 시나리오로 실행했어요. 온보딩 → 홈 → 기록 1~3단계·저장 → 창작소 → 감정 캐릭터 기간 선택 → 아카이브 일/주/창작물 → 마이와 하위 6개 화면까지 20개 화면이에요. 콘솔 오류는 0건이에요.
- 화면별 픽셀 차이는 0~4%예요. 차이는 글자색 미세 조정, 12px 올림, 화남 홈 배경에서 나왔어요.

## 남은 일
- `!important` 2,931개와 버전별 스타일 블록 61개(캐스케이드 정리)
- 간격(padding 384종, gap 35종), 그림자(166종) 토큰 적용
- 버전 번호가 붙은 클래스명 235개를 역할 기준 이름으로 바꾸기
- 감정 fill의 흰 배경 대비(기쁨 1.70:1, 평온 1.77:1) 보강
- 렌더링되지 않는 레거시 아카이브 컴포넌트(8월 주간 버킷 `$wk`) 삭제
