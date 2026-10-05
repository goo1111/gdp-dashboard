exec(open('newslides.py').read().split('# ---------- 11 Design System ----------')[0])
cols=[('KEEP','잘된 점','#5a4ab3',[
  ('202 → 0','원본을 고치니 접근성도 따라왔다','화면을 덧칠하던 보정 스크립트를 지우고 토큰 값을 고쳐, 대비 · 글자 크기 위반이 사라졌습니다.'),
  ('5곳 → 1곳','감정 색을 데이터로 다뤘다','흩어진 감정 색 정의를 하나로 모으니, 같은 감정이 화면마다 다른 색으로 보이던 문제가 없어졌습니다.'),
  ('145 / 145','Figma와 코드가 같은 이름을 쓴다','컴포넌트의 칠 · 선을 모두 변수로 연결해, 디자인과 코드가 함께 바뀝니다.')]),
 ('PROBLEM','아쉬운 점','#a23b32',[
  ('2차 자료','사용자를 직접 만나지 못했다','리서치는 논문 속 인터뷰와 앱 리뷰가 전부였고, 사용성 테스트도 아직 하지 않았습니다.'),
  ('2,900여 개','버전마다 덧댄 스타일이 쌓였다','!important와 버전 이름이 붙은 클래스가 남아, 작은 수정에도 규칙끼리 충돌했습니다.'),
  ('이름 3개','같은 기능을 다르게 불렀다','마음 지도 · 감정 나침반 · 마음의 위치처럼 용어가 흩어져, 마지막에야 하나로 맞췄습니다.')]),
 ('TRY','다음에 다르게','#347565',[
  ('먼저','토큰과 컴포넌트를 화면보다 먼저','화면을 다 만든 뒤 정리하는 대신, 시스템을 먼저 세우고 그 위에 화면을 올리겠습니다.'),
  ('초기에','용어 사전을 첫 주에 확정','서비스명과 기능 이름을 IA 단계에서 정하고, 문구 · 문서 · 코드가 같은 단어를 쓰게 하겠습니다.'),
  ('5명','직접 인터뷰와 테스트를 일정에 고정','Discover에 인터뷰 5명, Deliver에 사용성 테스트를 처음부터 일정으로 넣겠습니다.')])]
def col(tag,name,c,items):
    it=''.join(f'<div class="ri"><b style="color:{c}">{n}</b><div><h5>{h}</h5><p>{p}</p></div></div>' for n,h,p in items)
    return f'<div class="rc"><div class="rh"><span style="color:{c}">{tag}</span><h4>{name}</h4></div>{it}</div>'
css='''.rg{margin-top:30px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.rc{border-radius:18px;background:#fff;box-shadow:0 16px 36px -26px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);padding:22px 24px;height:486px}
.rh{display:flex;align-items:baseline;gap:10px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.rh span{font-size:12px;font-weight:700;letter-spacing:.06em}.rh h4{font-size:18px;font-weight:700;letter-spacing:-.03em}
.ri{display:grid;grid-template-columns:92px 1fr;gap:12px;padding:26px 0;border-bottom:1px solid var(--line)}.ri:last-child{border-bottom:0}
.ri>b{font-size:18px;font-weight:700;letter-spacing:-.03em;line-height:1.3}
.ri h5{font-size:16px;font-weight:700;letter-spacing:-.03em}.ri p{margin-top:6px;font-size:13.5px;line-height:1.55;color:var(--ink2);font-weight:500;word-break:keep-all}'''
body='<div class="rg">'+''.join(col(*c) for c in cols)+'</div>'
s=slide('감정로그 · Retrospective','Retrospective','화면을 덧칠하기보다 <em>원본을 고치는 것</em>이 가장 빠른 길이었습니다.',
 '디자인 시스템으로 품질을 원본에서 지킨 것은 남기고, 사용자 검증과 용어 정리를 늦게 시작한 것은 다음 프로젝트에서 바꾸겠습니다.',body,
 '다음 프로젝트의 순서 — <b>사용자를 먼저 만나고, 이름과 시스템을 정한 뒤, 화면을 만든다.</b>',css)
open('s14r.html','w').write(s);print('ok')
