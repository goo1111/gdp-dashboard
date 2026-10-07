import re
base=open('s04.html').read()
# head: everything up to the end of the 2nd <style> block (font + shared base)
idx=[m.end() for m in re.finditer(r'</style>',base)]
head=base[:idx[1]]
head=re.sub(r'<title>[^<]*</title>','<title>{TITLE}</title>',head)
TAIL='''<script> function fit(){const s=Math.min(innerWidth/1440,innerHeight/810),x=(innerWidth-1440*s)/2,y=(innerHeight-810*s)/2;document.getElementById('wrap').style.transform=`translate(${x}px,${y}px) scale(${s})`} addEventListener('resize',fit);fit(); </script> </body> </html>'''
COMMON='''<style>.slide h1 em{font-style:normal;color:#6f5fc9}
.opp{position:absolute;left:88px;right:88px;bottom:44px;height:56px;border-radius:12px;background:#efecfa;border:1px solid #e3def6;display:flex;align-items:center;padding:0 28px;gap:18px;font-size:16px;font-weight:600;color:var(--ink)}
.opp em{font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#5a4ab3}
.opp b{color:#5a4ab3}.opp span{font-weight:600}
.cd{border-radius:18px;background:#fff;box-shadow:0 16px 36px -26px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);padding:22px 26px}
.ph3{font-size:19px;font-weight:700;letter-spacing:-.04em;display:flex;align-items:center;gap:8px}
.ph3 em{font-style:normal;font-size:11px;font-weight:700;color:#fff;background:var(--accent);border-radius:999px;padding:1px 8px}
.k{font-size:13px;font-weight:500;color:var(--ink3);line-height:1.45;margin-top:4px}
.chip{display:inline-block;font-size:11.5px;font-weight:700;color:#5a4ab3;background:#efecfa;border-radius:999px;padding:2px 9px;letter-spacing:0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;letter-spacing:0;color:#5a4ab3;background:#f5f3fa;border-radius:5px;padding:1px 5px}
</style>'''
def slide(title,eyebrow,h1,sub,body,opp,css):
    return head.replace('{TITLE}',title)+COMMON+'<style>'+css+'</style><div id="wrap"><section class="slide"><div class="eyebrow">'+eyebrow+'</div><h1>'+h1+'</h1><p class="sub">'+sub+'</p>'+body+'<div class="opp"><em>INSIGHT</em><span>'+opp+'</span></div></section></div>'+TAIL

# ---------- 11 Design System ----------
EM=[('설렘','#f05a8a','#fff1f5','#d93d6a','#972047'),('평온','#8bd0bd','#eaf8f3','#55aa92','#347565'),('기쁨','#f7bd4e','#fff4d4','#d99400','#8c5d00'),('복합','#d19cdb','#f8ecfb','#a96abb','#744789'),
    ('슬픔','#80a9dc','#eaf3fc','#5689c1','#426d9e'),('불안','#dfa292','#ffede8','#bd6552','#954b3e'),('무기력','#9ca9b1','#eef2f4','#718089','#59666e'),('화남','#e66f5c','#ffeae6','#c8493d','#a23b32')]
emo=''.join(f'<div class="em" style="background:{t};border-color:{b}"><b style="color:{x}">{n}</b><div class="sw"><i style="background:{f}"></i><i style="background:{t};box-shadow:inset 0 0 0 1px {b}"></i><i style="background:{b}"></i><i style="background:{x}"></i></div></div>' for n,f,t,b,x in EM)
layers=[('Primitive','값','54','<code>rose/400 #f05a8a</code> 감정 8색 × 4단계 · 웜 뉴트럴 · 파스텔'),
        ('Semantic','역할','59','<code>color/emotion/flutter/fill</code> → <code>var(--color-emotion-flutter-fill)</code>'),
        ('Style','레시피','17','텍스트 14 (display · title · body · caption) · 그림자 3 (sm · md · lg)'),
        ('Component','부품','4','Button 8 · EmotionChip 16 · DayCell 18 · ListRow — 프로퍼티 = 코드 props')]
lay=''.join(f'<div class="ly"><div class="lt"><b>{a}</b><span>{b}</span></div><div class="ln">{c}</div><div class="ld">{d}</div></div>'+('<div class="la">↓</div>' if i<3 else '') for i,(a,b,c,d) in enumerate(layers))
css11='''.grid{margin-top:30px;display:grid;grid-template-columns:1fr 470px;gap:20px;height:470px}
.ly{display:grid;grid-template-columns:120px 64px 1fr;align-items:center;gap:14px;height:76px;padding:0 20px;border-radius:14px;background:#f8f7fc;border:1px solid #ebe7f6}
.ly:last-child{background:#f1eefc}
.lt b{display:block;font-size:16px;font-weight:700}.lt span{font-size:12.5px;color:var(--ink3);font-weight:500}
.ln{font-size:28px;font-weight:700;color:#5a4ab3;letter-spacing:-.04em}
.ld{font-size:13.5px;color:var(--ink2);font-weight:500;line-height:1.5}
.la{text-align:center;color:#b3a8e8;font-size:14px;height:18px;line-height:18px}
.emg{margin-top:16px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.em{border:1px solid;border-radius:12px;padding:14px 14px;display:flex;align-items:center;justify-content:space-between}
.em b{font-size:14px;font-weight:700}
.sw{display:flex;gap:4px}.sw i{width:20px;height:20px;border-radius:6px;display:block}
.leg{margin-top:12px;font-size:12px;color:var(--ink3);font-weight:500}'''
body11=f'''<div class="grid"><div class="cd"><div class="ph3"><em>01</em>4단계 구조</div><p class="k">컴포넌트는 Semantic만 참조합니다. 숫자는 Figma 라이브러리의 개수입니다.</p><div style="margin-top:16px">{lay}</div></div>
<div class="cd"><div class="ph3"><em>02</em>감정 토큰</div><p class="k">감정 하나에 네 가지 역할을 두어, 같은 감정이 화면마다 다르게 칠해지던 문제를 없앴습니다.</p><div class="emg">{emo}</div><p class="leg">fill 점·그래프 · tint 카드 배경 · border 선택 테두리 · text 감정 위 글자(4.5:1 이상)</p></div></div>'''
s11=slide('감정로그 · Design System','Develop · Design System','흩어진 값을 <em>토큰과 컴포넌트</em>로 모아, 디자인과 코드를 하나의 원본으로 맞췄습니다.',
 '반복 수정으로 쌓인 하드코딩(색 984종, 덮어쓰기 규칙 2,949곳)을 점검하고, <b>Figma 베리어블과 CSS 변수를 이름까지 1:1로 연결</b>했습니다.',body11,
 'Figma의 <b>color/text/primary</b>는 코드의 <b>var(--color-text-primary)</b>입니다. 값 하나를 바꾸면 Figma와 화면이 함께 바뀝니다.',css11)

# ---------- 12 Quality ----------
rows=[('CSS 토큰 사용 비율','2.2%','36.7%'),('감정 색 정의','5곳','1곳'),('보정 없이 대비·글자 크기 위반','202','0'),('44px 미만 터치 영역','128','0'),
      ('이름 없는 컨트롤','3','0'),('주요 버튼 규격','높이 · 모서리 3종씩','1종'),('키보드로 기록하기','불가','가능')]
mt=''.join(f'<tr><th>{a}</th><td class="b">{b}</td><td class="ar">→</td><td class="a">{c}</td></tr>' for a,b,c in rows)
acts=[('색 · 글자','감정 색 원본을 토큰 하나로 모으고, 글자색 812곳 · 크기 1,278곳을 Semantic 토큰으로 바꿨습니다.'),
      ('보정 스크립트 제거','화면을 사후에 칠하고 키우던 런타임 스크립트를 지우고, 토큰 값 자체가 4.5:1 대비와 12px 이상을 지키게 했습니다.'),
      ('손가락 · 키보드','달력 칸 · 칩 · 탭을 44px로 키우고, 마음 지도를 키보드로 열 수 있는 대화상자로 바꿨습니다.'),
      ('Button 컴포넌트','34곳에 흩어진 버튼 클래스를 Figma Button과 같은 규격 하나로 묶었습니다.')]
ac=''.join(f'<div class="ac"><i>{i+1}</i><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate(acts))
css12='''.grid{margin-top:30px;display:grid;grid-template-columns:1fr 560px;gap:20px;height:470px}
.ac{display:grid;grid-template-columns:30px 1fr;gap:12px;padding:15px 0;border-bottom:1px solid var(--line)}.ac:last-child{border-bottom:0}
.ac i{font-style:normal;width:26px;height:26px;border-radius:50%;background:#e9e5f8;color:#5a4ab3;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center}
.ac b{display:block;font-size:15.5px;font-weight:700}.ac span{display:block;margin-top:3px;font-size:13.5px;line-height:1.55;color:var(--ink2);font-weight:500;word-break:keep-all}
table{margin-top:12px;width:100%;border-collapse:collapse}
th,td{padding:0 8px;height:50px;border-bottom:1px solid var(--line);font-size:14px;text-align:left}
tr:last-child th,tr:last-child td{border-bottom:0}
th{font-weight:600;color:var(--ink2);width:46%}
td.b{color:var(--ink3);font-weight:500;width:24%}td.ar{color:#b3a8e8;width:30px;text-align:center}
td.a{font-weight:700;color:#5a4ab3;font-size:16px}
thead th{height:30px;font-size:12px;color:var(--ink3);font-weight:600;border-bottom:1px solid var(--line)}'''
body12=f'''<div class="grid"><div class="cd"><div class="ph3"><em>01</em>무엇을 바꿨나</div><div style="margin-top:6px">{ac}</div></div>
<div class="cd"><div class="ph3"><em>02</em>프로토타입 v69 → v73</div><p class="k">같은 20개 화면을 브라우저로 자동 실행해 측정했습니다.</p>
<table><thead><tr><th>항목</th><th>v69</th><th></th><th>v73</th></tr></thead><tbody>{mt}</tbody></table></div></div>'''
s12=slide('감정로그 · Quality','Deliver · Quality &amp; Accessibility','토큰으로 옮기자, <em>보정 스크립트 없이도</em> 누구나 읽고 누를 수 있는 화면이 됐습니다.',
 '값을 원본에서 고치니 접근성도 함께 지켜졌습니다. <b>기능은 그대로 두고, 화면별 픽셀 비교로 회귀가 없는지 확인하며 바꿨습니다.</b>',body12,
 '디자인 시스템은 일관성만이 아니라, <b>접근성을 원본에서 지키는 장치</b>였습니다.',css12)

# ---------- 13 Usability test ----------
qs=[('Q1','마음 지도','에너지 × 편안함 두 축으로 감정 위치를 고르는 방식을 이해하는가'),('Q2','기록 흐름','감정 → 세부 감정 → 한 문장 3단계를 부담 없이 마치는가'),
    ('Q3','돌아보기','달력 색과 일간 · 주간 리포트로 지난 감정의 흐름을 설명하는가'),('Q4','핵심 가치','기록이 작품으로 남는 경험이 기존 일기 앱과 다르게 느껴지는가')]
q=''.join(f'<div class="q"><span class="chip">{a}</span><b>{b}</b><p>{c}</p></div>' for a,b,c in qs)
tasks=[('과업 1','오늘의 감정 기록하기','5분','지도 왼쪽 위 → 화남 → 짜증난 · 답답한 → 한 문장 저장'),('과업 2','홈 화면 이해','3분','오늘의 감정 · 이번 주 기록 · 이번 주 흐름의 색'),
       ('과업 3','아카이브에서 돌아보기','5분','어제 기록 선택 → 일간 · 주간 리포트 해석','core'),('과업 4','기록으로 작품 만들기','4분','오늘 기록 → 작품 생성 · 저장 → 나의 창작물에서 찾기')]
tk=''.join(f'<div class="t{" on" if len(x)>4 else ""}"><div class="th"><span class="chip">{x[0]}</span><small>{x[2]}</small></div><b>{x[1]}</b><p>{x[3]}</p></div>' for x in tasks)
css13='''.qs{margin-top:32px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.q{border-radius:14px;background:#f8f7fc;border:1px solid #ebe7f6;padding:16px 18px;height:132px}
.q b{display:block;margin-top:8px;font-size:15px;font-weight:700}.q p{margin-top:4px;font-size:12.5px;line-height:1.5;color:var(--ink2);font-weight:500;word-break:keep-all}
.tk{margin-top:18px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.t{border-radius:16px;background:#fff;box-shadow:0 16px 36px -26px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);padding:18px 20px;height:178px}
.t.on{box-shadow:0 0 0 2px #6f5fc9,0 16px 36px -26px rgba(60,40,90,.4)}
.th{display:flex;justify-content:space-between;align-items:center}.th small{font-size:12px;color:var(--ink3);font-weight:600}
.t b{display:block;margin-top:10px;font-size:16.5px;font-weight:700;letter-spacing:-.04em}.t p{margin-top:6px;font-size:13px;line-height:1.5;color:var(--ink2);font-weight:500;word-break:keep-all}
.t.on .th small:after{content:" · 핵심";color:#5a4ab3}
.meta{margin-top:18px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.mt{border-radius:14px;background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.05);padding:16px 20px;height:92px}
.mt small{font-size:12px;font-weight:700;color:#5a4ab3;letter-spacing:.04em}.mt p{margin-top:6px;font-size:14px;font-weight:600;color:var(--ink)}
.mt p span{color:var(--ink3);font-weight:500;font-size:13px}'''
body13=f'''<div class="qs">{q}</div><div class="tk">{tk}</div>
<div class="meta"><div class="mt"><small>결과 기록</small><p>도움 없이 / 조작 도움 후 / 이해 실패 <span>· 의미는 설명하지 않고 조작 방법만 안내</span></p></div>
<div class="mt"><small>결과 정리</small><p>사용자 행동 → 발언 → 문제 → 원인 → UI 개선 <span>· 2명 이상 반복되면 우선 수정</span></p></div></div>'''
s13=slide('감정로그 · Usability Test','Deliver · Usability Test Plan','메뉴를 찾는 능력이 아니라, <em>기록이 작품으로 이어지는 경험을 이해하는지</em> 확인합니다.',
 '참가자 3명 · 1인 30분 · 1:1 진행자 동석. <b>진행자가 화면 · 버튼 · 입력값을 모두 지정하고</b>, 참가자는 조작하며 소리 내어 해석합니다(Think-aloud).',body13,
 '반복된 문제부터 고쳐 <b>문제 발견 → 근거(발언) → UI 개선 → 개선 후 확인</b>으로 다음 버전에 잇습니다.',css13)
for n,s in [('s11',s11),('s12',s12),('s13',s13)]: open(n+'.html','w').write(s)
print('ok')
