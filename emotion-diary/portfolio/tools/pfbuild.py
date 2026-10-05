import re,html,base64
t=open('pf68-full.html').read()
secs=re.findall(r'(<section class="s"><div class="lbl">(.*?)</div><div class="frame"><iframe srcdoc="(.*?)"(.*?)</iframe></div></section>)',t,re.S)
assert len(secs)==10
src={i+1:html.unescape(s[2]) for i,s in enumerate(secs)}
tail_attr=secs[0][3]
# --- phone screenshots: alt -> capture
ALT={'1단계 마음 위치':'07-1','2단계 세부 감정':'07-2','3단계 한 문장':'07-3','저장 후 홈':'07-4','창작소':'08-1','기록 선택':'08-2','재료 확인':'08-3','작품 결과':'08-4',
     '결과 화면 스타일 전환':'09-1','감정 달력과 리포트':'10-1','감정 달력과 나의 창작물':'10-2','작품 상세':'10-3','굿즈 미리보기':'10-4'}
n=0
def swap(d):
    global n
    def r(m):
        global n
        alt=re.search(r'alt="([^"]*)"',m.group(2)); key=alt and ALT.get(alt.group(1))
        if not key: return m.group(0)
        n+=1; b=base64.b64encode(open(f'pfcap/{key}.jpg','rb').read()).decode()
        return f'<img src="data:image/jpeg;base64,{b}"{m.group(2)}>'
    return re.sub(r'<img src="data:image/jpeg;base64,[A-Za-z0-9+/=]+"([^>]*)>',lambda m:r(type('M',(),{'group':lambda s,i:[m.group(0),None,m.group(1)][i]})()),d)
for k in (7,8,9,10): src[k]=swap(src[k])
assert n==13,n
# --- intro updates
a='2026.06 – 2026.09'; assert src[1].count(a)==1; src[1]=src[1].replace(a,'2026.06 – 2026.10')
a='데스크 리서치 · 문제 정의 · IA · 기능 구조 설계 · 프로토타입'; assert src[1].count(a)==1
src[1]=src[1].replace(a,'데스크 리서치 · 문제 정의 · IA · 기능 구조 설계 · 프로토타입 · 디자인 시스템 · 사용성 테스트 설계')
# --- no problem tags on any slide
import re as _re
for k in src: src[k]=_re.sub(r'<span class="eb2">[^<]*</span>','',src[k])
# --- conclusion bars: INSIGHT, same position on 03-06 (+ new slides); period wording
BAR='.opp{position:absolute;left:88px;right:88px;bottom:44px;height:56px;border-radius:12px;background:#efecfa;border:1px solid #e3def6;display:flex;align-items:center;padding:0 28px;gap:18px;font-size:16px;font-weight:600;color:var(--ink);margin:0}.opp em{font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#5a4ab3!important}.opp b{color:#5a4ab3}.slide .opp span{font-size:16px;font-weight:600;color:var(--ink)}.slide .opp{font-size:16px;margin:0}'
def bar(k,html_):
    src[k]=src[k].replace('</style>',BAR+'</style>',1)
    if html_: 
        assert src[k].count('</section>')==1; src[k]=src[k].replace('</section>',html_+'</section>')
a='<div class="kp"><em>KEY PROBLEM</em>'; assert src[3].count(a)==1; src[3]=src[3].replace(a,'<div class="opp"><em>INSIGHT</em>'); bar(3,'')
a='<div class="opp"><em>INSIGHT</em>입력 · 축적 · 보상을 하나로 잇는 \'감정 창작 구조\'를 제안합니다.</div>'; assert src[4].count(a)==1
src[4]=src[4].replace(a,'<div class="opp"><em>INSIGHT</em><span>입력 · 축적 · 보상을 하나로 잇는 <b>\'감정 창작 구조\'</b>를 제안합니다.</span></div>'); bar(4,'')
# 04: bar was nested inside .cz (unclosed div) -> move it to section level
_m=_re.search(r'\s*<div class="opp"><em>INSIGHT</em><span>입력.*?</span></div>',src[4],_re.S); _b=_m.group(0)
src[4]=src[4].replace(_b,'',1); src[4]=src[4].replace('</section>',_b+'</section>',1)
# 05/06: lift and shrink diagrams slightly so the bar does not touch them
src[5]=src[5].replace('</style>','.cz{transform:translateY(-22px) scale(.94);transform-origin:720px 202px}</style>',1)
src[6]=src[6].replace('</style>','.cz{transform:translateY(-16px) scale(.97);transform-origin:720px 200px}</style>',1)
bar(5,'<div class="opp"><em>INSIGHT</em><span>사용자는 <b>고르기만</b> 하고, 흐름 정리와 창작은 감정로그가 맡아 기록의 부담을 줄였습니다.</span></div>')
bar(6,'<div class="opp"><em>INSIGHT</em><span><b>기록 → 창작 → 아카이브</b> 흐름 하나만 깊게 만들고, 나머지는 형태만 구현했습니다.</span></div>')
a='2인 · 4개월'; assert src[6].count(a)==1; src[6]=src[6].replace(a,'2인 · 5개월')
a='>팀 프로젝트<'; assert src[1].count(a)==1; src[1]=src[1].replace(a,'>팀 프로젝트 (2인)<')
new={k:open(f'pf/s{k}.html').read() for k in ('11g','13v')}
order=[('01 인트로',src[1]),('02 배경',src[2]),('03 리서치 · 문제 정의',src[3]),('04 시장조사',src[4]),('05 컨셉모델',src[5]),('06 IA · 기능 구조',src[6]),
       ('07 HOME',src[7]),('08 CREATE',src[8]),('09 CREATE · Variations',src[9]),('10 ARCHIVE',src[10]),
       ('11 디자인 시스템',new['11g'].replace('Develop · Design System','Deliver · Design System')),
       ('12 검증 계획 · 다음 단계',new['13v'])]
body=''.join(f'<section class="s"><div class="lbl">{l}</div><div class="frame"><iframe srcdoc="{html.escape(d,quote=True)}"{tail_attr}</iframe></div></section>' for l,d in order)
start=t.find(secs[0][0]); end=t.find(secs[-1][0])+len(secs[-1][0])
out=t[:start]+body+t[end:]
out=out.replace('<title>감정로그 포트폴리오 v41</title>','<title>감정로그 포트폴리오 v79</title>',1)
old_hdr=re.search(r'<header>.*?</header>',out,re.S).group(0)
toc=' · '.join(l for l,_ in order)
new_hdr='<header><h1>감정로그 포트폴리오 <span style="font-size:14px;color:var(--ink3);font-weight:600">v79</span></h1><p>'+toc+'</p></header>'
out=out.replace(old_hdr,new_hdr,1)
open('감정로그_포트폴리오_v79.html','w').write(out)
print('sections',out.count('<section class="s">'),'size MB',round(len(out)/1e6,2))
