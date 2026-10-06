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
# --- terminology: 감정 나침반 (feature), 작품 (one result), 나의 창작물 (collection)
for k,a,b,n in [(1,'감정 창작물"','감정 작품"',9),(1,'<em>나만의 창작물</em>','<em>나만의 작품</em>',1),
                (7,'<em>마음의 위치</em>로','<em>감정 나침반</em>으로',1),(7,'마음의 위치를 먼저 찍고','감정 나침반에서 위치를 먼저 찍고',1)]:
    assert src[k].count(a)==n,(k,a,src[k].count(a)); src[k]=src[k].replace(a,b)
# --- readability fixes (03, 06, 09, 10)
for a,b in [('선택지는 단순하고 말로 옮기기는 어려워, 기록을 시작하는 것부터 부담이 됩니다.','고를 말이 부족해, 시작부터 부담이 됩니다.'),
            ('하루에도 바뀌는 감정이 하나로 뭉뚱그려져, 쌓여도 마음의 흐름이 보이지 않습니다.','바뀌는 감정이 하루 한 번으로 뭉뚱그려집니다.'),
            ('쌓인 기록이 그래프로 확인될 뿐, 내 것으로 남거나 다음으로 이어지지 않습니다.','그래프로 확인될 뿐, 다음으로 이어지지 않습니다.')]:
    assert src[3].count(a)==1,a; src[3]=src[3].replace(a,b)
src[3]=src[3].replace('</style>','.slide .q,.slide .ds{font-size:14px}</style>',1)
a='<h1><em>4개 탭으로 정보 구조</em>와 핵심 기능을 정리했습니다.</h1>'; assert src[6].count(a)==1
src[6]=src[6].replace(a,'<h1><em>기록 → 창작 → 아카이브</em> 한 흐름에 집중해, 꼭 필요한 4개 탭만 남겼습니다.</h1>')
src[9]=src[9].replace('</style>','.slide .th figcaption,.slide .sp small,.slide .nt,.slide .sum div span{font-size:13px}</style>',1)
a='한 달의 감정을 돌아보고, 마음에 든 작품은 <em>굿즈로 미리 봅니다</em>.'; assert src[10].count(a)==1
src[10]=src[10].replace(a,'한 달의 <em>감정 흐름</em>을 돌아보고, 마음에 든 작품은 굿즈로 이어 갑니다.')
new={k:open(f'pf/s{k}.html').read() for k in ('11g','13v','14r')}
order=[('01 인트로',src[1]),('02 배경',src[2]),('03 리서치 · 문제 정의',src[3]),('04 시장조사',src[4]),('05 컨셉모델',src[5]),('06 IA · 기능 구조',src[6]),
       ('07 HOME',src[7]),('08 CREATE',src[8]),('09 CREATE · Variations',src[9]),('10 ARCHIVE',src[10]),
       ('11 디자인 시스템',new['11g'].replace('Develop · Design System','Deliver · Design System')),
       ('12 검증 계획 · 다음 단계',new['13v']),('13 회고',new['14r'])]

# --- portfolio design system: type scale + min size, applied to every slide
PF_SCALE=[12,13,14,15,16,18,20,24,28,32,40]
PF_TOKENS=(':root{--pf-fs-label:12px;--pf-fs-caption:13px;--pf-fs-body:14px;--pf-fs-body-strong:15px;--pf-fs-lead:16px;'
 '--pf-fs-h4:18px;--pf-fs-h3:20px;--pf-fs-h2:24px;--pf-fs-stat:28px;--pf-fs-h1:32px;--pf-fs-display:40px;'
 '--pf-ink:#18181c;--pf-ink2:#55535f;--pf-ink3:#6a6874;--pf-ink4:#74727e;--pf-line:#ece9f1;--pf-bg:#fbfaf8;'
 '--pf-point:#6f5fc9;--pf-point-strong:#5a4ab3;--pf-accent:#8a7bd8;--pf-soft:#f5f3fa;--pf-tint:#efecfa}')
def pf_snap(v,floor):
    v=max(v,floor)
    return next(x for x in PF_SCALE if x>=v-0.01) if v<=40 else v
def pf_ds(d,floor=12):
    i=d.find('<section'); i=0 if i<0 else i
    def fix(m): return 'font-size:'+('%g'%pf_snap(float(m.group(1)),floor))+'px'
    head,body=d[:i],d[i:]
    head=_re.sub(r'font-size:\s*([\d.]+)px',fix,head); body=_re.sub(r'font-size:\s*([\d.]+)px',fix,body)
    return (head+body).replace('</style>','</style><style id="pf-ds">'+PF_TOKENS+'</style>',1)
FLOOR={'05 컨셉모델':13,'06 IA · 기능 구조':13}   # diagrams are scaled .94/.97 -> 13px renders >= 12px
order=[(l,pf_ds(d,FLOOR.get(l,12))) for l,d in order]
body=''.join(f'<section class="s"><div class="lbl">{l}</div><div class="frame"><iframe srcdoc="{html.escape(d,quote=True)}"{tail_attr}</iframe></div></section>' for l,d in order)
start=t.find(secs[0][0]); end=t.find(secs[-1][0])+len(secs[-1][0])
out=t[:start]+body+t[end:]
out=out.replace('<title>감정로그 포트폴리오 v41</title>','<title>감정로그 포트폴리오 v81</title>',1)
old_hdr=re.search(r'<header>.*?</header>',out,re.S).group(0)
toc=' · '.join(l for l,_ in order)
new_hdr='<header><h1>감정로그 포트폴리오 <span style="font-size:14px;color:var(--ink3);font-weight:600">v81</span></h1><p>'+toc+'</p></header>'
out=out.replace(old_hdr,new_hdr,1)
open('감정로그_포트폴리오_v81.html','w').write(out)
print('sections',out.count('<section class="s">'),'size MB',round(len(out)/1e6,2))
