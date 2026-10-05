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
new={k:open(f'pf/s{k}.html').read() for k in ('11d',12,13)}
order=[('01 인트로',src[1]),('02 배경',src[2]),('03 리서치 · 문제 정의',src[3]),('04 시장조사',src[4]),('05 컨셉모델',src[5]),('06 IA · 기능 구조',src[6]),
       ('07 디자인 시스템',new['11d']),('08 HOME',src[7]),('09 CREATE',src[8]),('10 CREATE · Variations',src[9]),('11 ARCHIVE',src[10]),
       ('12 품질 · 접근성',new[12]),('13 사용성 테스트 설계',new[13])]
body=''.join(f'<section class="s"><div class="lbl">{l}</div><div class="frame"><iframe srcdoc="{html.escape(d,quote=True)}"{tail_attr}</iframe></div></section>' for l,d in order)
start=t.find(secs[0][0]); end=t.find(secs[-1][0])+len(secs[-1][0])
out=t[:start]+body+t[end:]
out=out.replace('<title>감정로그 포트폴리오 v41</title>','<title>감정로그 포트폴리오 v72</title>',1)
old_hdr=re.search(r'<header>.*?</header>',out,re.S).group(0)
toc=' · '.join(l for l,_ in order)
new_hdr='<header><h1>감정로그 포트폴리오 <span style="font-size:14px;color:var(--ink3);font-weight:600">v72</span></h1><p>'+toc+'</p></header>'
out=out.replace(old_hdr,new_hdr,1)
open('감정로그_포트폴리오_v72.html','w').write(out)
print('sections',out.count('<section class="s">'),'size MB',round(len(out)/1e6,2))
