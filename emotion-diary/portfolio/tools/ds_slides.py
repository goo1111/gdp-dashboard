import json,re
exec(open('newslides.py').read().split('# ---------- 11 Design System ----------')[0])  # head, COMMON, slide()
TAB=json.load(open('../tabicons.json')); EMI=json.load(open('../emoicons.json'))
def tabicon(i,color): return TAB[i].replace("stroke='black'",f"stroke='{color}'").replace("<svg ","<svg width='22' height='22' ")
EM=[('flutter','설렘','#f05a8a','#fff1f5','#d93d6a','#972047'),('calm','평온','#8bd0bd','#eaf8f3','#55aa92','#347565'),('joy','기쁨','#f7bd4e','#fff4d4','#d99400','#8c5d00'),('complex','복합','#d19cdb','#f8ecfb','#a96abb','#744789'),
    ('sad','슬픔','#80a9dc','#eaf3fc','#5689c1','#426d9e'),('anxious','불안','#dfa292','#ffede8','#bd6552','#954b3e'),('empty','무기력','#9ca9b1','#eef2f4','#718089','#59666e'),('angry','화남','#e66f5c','#ffeae6','#c8493d','#a23b32')]
NEU=[('0','#ffffff'),('50','#faf9f4'),('100','#f3f0eb'),('200','#e4dfda'),('250','#dedbd8'),('400','#a39b95'),('500','#6f6964'),('600','#5f5a56'),('900','#1c1a18'),('950','#2b2733')]
DSCSS='''.col h4{font-size:15px;font-weight:700;letter-spacing:-.03em;margin-bottom:2px}
.lbl2{font-size:12px;font-weight:600;color:var(--ink3);margin:12px 0 7px;letter-spacing:0}
.lbl2 small{font-weight:500;color:var(--ink4);margin-left:6px}
.cd{padding:20px 22px}'''

# ================= Foundation =================
typ=[('display/lg','32','Bold'),('title/lg','24','Bold'),('title/sm','18','Bold'),('body/sm','14','SemiBold'),('caption/sm','12','Regular')]
tw={'Bold':700,'SemiBold':600,'Regular':400}
trows=''.join(f'<div class="tr"><code>{n}</code><span style="font-size:{min(int(s),24)}px;font-weight:{tw[w]}">오늘의 마음</span><em>{s} · {w}</em></div>' for n,s,w in typ)
emo=''.join(f'<div class="ec"><i style="background:{f}"></i><b>{l}</b><code>{f}</code><div class="er"><s style="background:{t};box-shadow:inset 0 0 0 1px {b}"></s><s style="background:{b}"></s><s style="background:{x}"></s></div></div>' for k,l,f,t,b,x in EM)
neu=''.join(f'<div class="nc"><i style="background:{h}"></i><small>{n}</small></div>' for n,h in NEU)
rad=''.join(f'<div class="rc"><i style="border-radius:{v}px"></i><small>{n} {v if v<99 else "full"}</small></div>' for n,v in [('sm',8),('md',12),('lg',16),('xl',20),('2xl',24),('full',999)])
sp=''.join(f'<div class="sc"><i style="width:{v}px"></i><small>{v}</small></div>' for v in [4,8,12,16,24,32,48])
sh=''.join(f'<div class="hc"><i style="box-shadow:{v}"></i><small>{n}</small></div>' for n,v in [('sm','0 1px 3px rgba(28,26,24,.08)'),('md','0 4px 8px rgba(28,26,24,.12)'),('lg','0 8px 24px rgba(28,26,24,.16)')])
cssA=DSCSS+'''.g3{margin-top:22px;display:grid;grid-template-columns:330px 1fr 340px;gap:18px;height:468px}
.font{font-size:46px;font-weight:700;letter-spacing:-.05em;line-height:1.1;margin-top:6px}
.wts{display:flex;gap:14px;margin-top:6px;font-size:13px;color:var(--ink2)}
.tr{display:grid;grid-template-columns:86px 1fr 86px;align-items:center;height:44px;border-bottom:1px solid var(--line)}.tr:last-child{border-bottom:0}
.tr code{font-size:11px;background:none;padding:0;color:var(--ink3)}.tr span{white-space:nowrap;overflow:hidden;color:var(--ink)}.tr em{font-style:normal;font-size:11.5px;color:var(--ink3);text-align:right}
.eg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.ec{border-radius:12px;background:#fbfaf8;border:1px solid var(--line);padding:9px 10px}
.ec i{display:block;height:26px;border-radius:8px}.ec b{display:block;margin-top:6px;font-size:13px;font-weight:700}
.ec code{font-size:10.5px;background:none;padding:0;color:var(--ink3)}
.er{display:flex;gap:3px;margin-top:5px}.er s{flex:1;height:10px;border-radius:3px;display:block}
.ng{display:grid;grid-template-columns:repeat(10,1fr);gap:4px}.nc i{display:block;height:28px;border-radius:6px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.nc small{display:block;margin-top:3px;font-size:10.5px;color:var(--ink3);text-align:center}
.sem{display:grid;grid-template-columns:1fr 1fr;gap:6px 12px;font-size:12px;color:var(--ink2)}
.sem div{display:flex;align-items:center;gap:6px;white-space:nowrap}.sem i{width:12px;height:12px;border-radius:4px;flex:none;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.rg{display:flex;gap:10px}.rc i{display:block;width:40px;height:30px;background:#f1eefc;border:1.5px solid #b3a8e8}.rc small,.sc small,.hc small{display:block;margin-top:4px;font-size:10.5px;color:var(--ink3)}
.sg{display:flex;align-items:flex-end;gap:10px;height:42px}.sc i{display:block;height:14px;background:#b3a8e8;border-radius:3px}
.hg{display:flex;gap:16px}.hc i{display:block;width:62px;height:34px;border-radius:10px;background:#fff}
.flow{display:flex;align-items:center;gap:6px;font-size:11.5px;color:var(--ink2);flex-wrap:wrap}.flow code{font-size:11px}'''
sem=[('text/primary','#1c1a18'),('text/secondary','#5f5a56'),('text/tertiary','#6f6964'),('text/inverse','#ffffff'),('bg/canvas','#faf9f4'),('bg/surface','#ffffff'),('border/default','#e4dfda'),('action/primary','#2b2733')]
semh=''.join(f'<div><i style="background:{h}"></i>{n}</div>' for n,h in sem)
bodyA=f'''<div class="g3">
<div class="cd col"><h4>Typography</h4><div class="lbl2">General<small>Pretendard</small></div><div class="font">Pretendard</div><div class="wts"><b>Bold 700</b><span style="font-weight:600">SemiBold 600</span><span>Regular 400</span></div>
<div class="lbl2">Text Style<small>14종 중 5종 · 최소 12px</small></div>{trows}</div>
<div class="cd col"><h4>Color</h4><div class="lbl2">Emotion<small>감정 8색 · fill / tint · border · text</small></div><div class="eg">{emo}</div>
<div class="lbl2">Neutral<small>웜 그레이 10단계 (Primitive)</small></div><div class="ng">{neu}</div>
<div class="lbl2">Semantic<small>컴포넌트는 이 이름만 참조</small></div><div class="sem">{semh}</div></div>
<div class="cd col"><h4>Scale &amp; Effect</h4><div class="lbl2">Radius</div><div class="rg">{rad}</div>
<div class="lbl2">Spacing<small>4 · 8 기반</small></div><div class="sg">{sp}</div>
<div class="lbl2">Shadow</div><div class="hg">{sh}</div>
<div class="lbl2">Token 흐름<small>Figma = CSS 1:1</small></div><div class="flow"><code>rose/400</code>→<code>color/emotion/flutter/fill</code>→<code>var(--color-emotion-flutter-fill)</code></div>
<div class="lbl2">Size</div><div class="flow"><code>touch-min 44</code><code>button-lg 48</code><code>button-md 40</code></div></div>
</div>'''
sA=slide('감정로그 · Design System · Foundation','Develop · Design System — Foundation','감정이 어느 화면에서나 <em>같은 색과 글자</em>로 보이도록, 토큰부터 다시 세웠습니다.',
 '하드코딩으로 흩어진 색 984종 · 글자 크기 65종을 <b>Primitive → Semantic 토큰과 텍스트 스타일 14종</b>으로 정리하고, Figma 베리어블과 CSS 변수를 1:1로 맞췄습니다.',bodyA,
 '감정 색은 이 앱의 <b>데이터</b>입니다. 원본을 하나로 두니 평온이 4가지 색으로 보이던 문제가 사라졌습니다.',cssA)

# ================= Components =================
def em(k): return next(e for e in EM if e[0]==k)
def btn(style,size,dis=False,label='다음'):
    h=48 if size=='L' else 40; r=20 if size=='L' else 16; fs=15 if size=='L' else 14
    if dis: c='background:#f3f0eb;color:#a39b95;border-color:#f3f0eb'
    elif style=='P': c='background:#2b2733;color:#fff;border-color:#2b2733'
    else: c='background:#fff;color:#1c1a18;border-color:#e4dfda'
    return f'<span class="bt" style="height:{h}px;border-radius:{r}px;font-size:{fs}px;{c}">{label}</span>'
def chip(k,word,sel):
    _,l,f,t,b,x=em(k)
    s=f'background:{t};border-color:{b};color:{x}' if sel else 'background:#fff;border-color:#e4dfda;color:#1c1a18'
    return f'<span class="ch" style="{s}"><i style="background:{f}"></i>{word}</span>'
def day(n,k=None,sel=False,today=False):
    st='background:#2b2733;color:#fff' if sel else (f'background:{em(k)[3]}' if k else '')
    bar=f'<s style="background:{em(k)[2]}"></s>' if k else ('<s style="background:#1c1a18"></s>' if today else '<s style="opacity:0"></s>')
    return f'<span class="dc" style="{st}"><b style="{"font-weight:700" if k or sel else ""}">{n}</b>{bar}</span>'
def emoi(k,sel=False):
    e=next(x for x in EMI if x['label']==em(k)[1]); f=em(k)[2]
    return f'<span class="ei{" on" if sel else ""}"><i style="background:{f};opacity:{1 if sel else .55}">{e["svg"]}</i><small>{e["label"]}</small></span>'
def nav(active):
    names=['홈','창작소','아카이브','마이']
    return '<div class="nv">'+''.join(f'<span class="{"on" if i==active else ""}">{tabicon(i,"#1c1a18" if i==active else "#a39b95")}<small>{n}</small></span>' for i,n in enumerate(names))+'</div>'
cssB=DSCSS+'''.g3{margin-top:22px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;height:494px}
.prop{font-size:11px;font-weight:600;color:#5a4ab3;background:#efecfa;border-radius:999px;padding:1px 8px;margin-left:6px;letter-spacing:0}
.row{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.sz{font-size:11px;color:var(--ink3);width:34px;flex:none}
.bt{display:inline-flex;align-items:center;justify-content:center;border:1px solid;font-weight:700;padding:0 18px;min-width:96px;letter-spacing:-.02em}
.tg{width:44px;height:26px;border-radius:999px;background:#e4dfda;position:relative;display:inline-block}.tg:after{content:"";position:absolute;left:3px;top:3px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.tg.on{background:#2b2733}.tg.on:after{left:21px}
.hd{border-radius:12px;background:#fff;box-shadow:0 0 0 1px var(--line);padding:10px 14px}
.hd small{display:block;font-size:11px;color:var(--ink3);font-weight:600}.hd b{font-size:16px;font-weight:700}
.fh{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--ink2)}
.ch{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px;border:1px solid;border-radius:12px;font-size:12.5px;font-weight:600}
.ch i{width:7px;height:7px;border-radius:50%}
.ei{display:inline-flex;flex-direction:column;align-items:center;gap:3px;width:40px}
.ei i{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center}.ei i svg{width:18px;height:18px}
.ei.on i{box-shadow:0 0 0 2px #fff,0 0 0 4px #1c1a18}.ei small{font-size:11px;color:var(--ink2);font-weight:600}
.dc{width:36px;height:36px;border-radius:12px;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font-size:13px;color:#6f6964}
.dc s{display:block;width:12px;height:3px;border-radius:2px}
.nv{display:grid;grid-template-columns:repeat(4,1fr);border-radius:12px;background:#fff;box-shadow:0 0 0 1px var(--line);height:56px;align-items:center}
.nv span{display:flex;flex-direction:column;align-items:center;gap:2px}.nv small{font-size:10.5px;color:#a39b95;font-weight:600}.nv .on small{color:#1c1a18}
.sg2{display:grid;grid-template-columns:repeat(3,1fr);background:#f3f0eb;border-radius:12px;padding:4px;height:40px}
.sg2 span{display:flex;align-items:center;justify-content:center;font-size:12.5px;color:#6f6964;font-weight:600;border-radius:9px}.sg2 .on{background:#fff;color:#1c1a18;box-shadow:0 1px 3px rgba(28,26,24,.08)}
.ul{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--line);height:34px}
.ul span{display:flex;align-items:center;justify-content:center;font-size:13px;color:#6f6964;font-weight:600}.ul .on{color:#1c1a18;box-shadow:inset 0 -2px 0 #1c1a18}
.rc2{border-radius:14px;background:#fff;box-shadow:0 0 0 1px #dedbd8;padding:10px 14px 10px 18px;position:relative}
.rc2:before{content:"";position:absolute;left:8px;top:10px;bottom:10px;width:3px;border-radius:2px;background:#e66f5c}
.rc2 div{display:flex;justify-content:space-between;font-size:13px;font-weight:700}.rc2 div small{font-weight:500;color:#6f6964;font-size:11.5px}
.rc2 p{font-size:12px;color:#5f5a56;margin-top:2px}
.lr{border-radius:12px;background:#fff;box-shadow:0 0 0 1px var(--line);display:flex;justify-content:space-between;align-items:center;padding:8px 14px}
.lr b{display:block;font-size:13px}.lr small{font-size:11.5px;color:#6f6964}.lr em{font-style:normal;color:#6f6964}'''
bodyB=f'''<div class="g3">
<div class="cd col"><h4>Button<span class="prop">Style × Size × State · 8</span></h4>
<div class="lbl2">Primary / Secondary</div>
<div class="row"><span class="sz">48px</span>{btn('S','L',label='이전')}{btn('P','L')}</div>
<div class="row" style="margin-top:8px"><span class="sz">40px</span>{btn('S','M',label='이전')}{btn('P','M')}</div>
<div class="row" style="margin-top:8px"><span class="sz">Disabled</span>{btn('P','L',True,'저장하기')}</div>
<div class="lbl2">Toggle<span class="prop">pressed</span></div><div class="row"><span class="tg on"></span><span class="tg"></span><small style="font-size:11.5px;color:var(--ink3)">누르는 영역 44px</small></div>
<div class="lbl2">Header<span class="prop">type: tab · flow</span></div>
<div class="hd"><small>아카이브</small><b>소소한 날들이 쌓였어요</b></div>
<div class="hd fh" style="margin-top:8px"><span>‹</span><span><small style="font-size:11px;color:var(--ink3)">1단계 · 마음 위치</small></span><span>닫기</span></div></div>
<div class="cd col"><h4>Emotion<span class="prop">emotion × selected</span></h4>
<div class="lbl2">Emotion Picker<small>8가지 감정</small></div><div class="row" style="gap:2px;flex-wrap:nowrap">{''.join(emoi(k,k=='angry') for k,*_ in EM)}</div>
<div class="lbl2">EmotionChip<small>최대 3개 선택 · 높이 44px 영역</small></div>
<div class="row">{chip('angry','화난',False)}{chip('angry','짜증난',True)}{chip('angry','답답한',True)}</div>
<div class="row" style="margin-top:8px">{chip('calm','평온한',False)}{chip('calm','편안한',True)}{chip('joy','뿌듯한',True)}</div>
<div class="lbl2">DayCell<span class="prop">emotion · selected · isToday</span></div>
<div class="row" style="gap:6px">{day(1,'complex')}{day(2)}{day(3,'flutter')}{day(4,'anxious')}{day(5,'angry',sel=True)}{day(6,today=True)}{day(7)}</div>
<div class="lbl2">Card UI · 이번 주 기록</div><div class="rc2"><div>화남 · 짜증난<small>오늘</small></div><p>회의가 길어져서 짜증이 났다.</p></div></div>
<div class="cd col"><h4>Navigation<span class="prop">selected</span></h4>
<div class="lbl2">Bottom Navigation<small>Default · 홈 선택</small></div>{nav(0)}
<div class="lbl2" style="margin-top:8px">Activate<small>아카이브 선택</small></div>{nav(2)}
<div class="lbl2">Tabs<span class="prop">style: segment · underline</span></div>
<div class="sg2"><span>일간</span><span class="on">주간</span><span>월간</span></div>
<div class="ul" style="margin-top:8px"><span class="on">감정 리포트</span><span>나의 창작물</span></div>
<div class="lbl2">ListRow<span class="prop">title · description · chevron</span></div>
<div class="lr"><span><b>데이터 관리</b><small>내 데이터 확인과 내보내기</small></span><em>›</em></div></div>
</div>'''
sB=slide('감정로그 · Design System · Components','Develop · Design System — Components','자주 쓰는 화면 요소를 <em>컴포넌트</em>로 묶고, 상태와 크기는 <em>프로퍼티</em>로 정리했습니다.',
 '같은 버튼이 화면마다 높이 3종 · 모서리 3종으로 만들어져 있던 것을 하나로 모았습니다. <b>Figma 프로퍼티는 코드 props와 1:1로 이름을 맞췄습니다.</b>',bodyB,
 'Figma에서 <b>Style=Primary, Size=Large</b>를 고르면, 코드에서는 <b>&lt;Button variant="primary" size="lg" /&gt;</b>가 됩니다.',cssB)
open('s11a.html','w').write(sA);open('s11b.html','w').write(sB);print('ok')

# ================= Single merged slide =================
typ2=[('display/lg','32','Bold'),('title/sm','18','Bold'),('body/sm','14','SemiBold'),('caption/sm','12','Regular')]
trows2=''.join(f'<div class="tr"><code>{n}</code><span style="font-size:{min(int(s),26)}px;font-weight:{tw[w]}">오늘의 마음</span><em>{s} · {w}</em></div>' for n,s,w in typ2)
emo2=''.join(f'<div class="ec2"><i style="background:{f}"></i><div><b>{l}</b><code>{f}</code></div></div>' for k,l,f,t,b,x in EM)
neu2=''.join(f'<i style="background:{h}" title="{n}"></i>' for n,h in NEU)
cssC=cssB+'''.split{margin-top:22px;display:grid;grid-template-columns:500px 1fr;gap:18px;height:468px}
.font{font-size:40px;font-weight:700;letter-spacing:-.05em;line-height:1.05}
.fw{display:flex;align-items:flex-end;justify-content:space-between}.wts{display:flex;gap:10px;font-size:12px;color:var(--ink2)}
.tr{display:grid;grid-template-columns:84px 1fr 84px;align-items:center;height:32px;border-bottom:1px solid var(--line)}.tr:last-child{border-bottom:0}
.tr code{font-size:10.5px;background:none;padding:0;color:var(--ink3)}.tr span{white-space:nowrap;overflow:hidden}.tr em{font-style:normal;font-size:11px;color:var(--ink3);text-align:right}
.eg2{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.ec2{display:flex;align-items:center;gap:7px;border-radius:10px;background:#fbfaf8;border:1px solid var(--line);padding:6px 8px}
.ec2 i{width:22px;height:22px;border-radius:6px;flex:none}.ec2 b{display:block;font-size:12px;font-weight:700;line-height:1.2}.ec2 code{font-size:10px;background:none;padding:0;color:var(--ink3)}
.ng2{display:grid;grid-template-columns:repeat(10,1fr);gap:3px}.ng2 i{display:block;height:20px;border-radius:5px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.ngl{display:flex;justify-content:space-between;font-size:10px;color:var(--ink3);margin-top:3px}
.flow{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--ink2);flex-wrap:wrap}.flow code{font-size:10.5px}
.cg{display:grid;grid-template-columns:1fr 1fr;gap:0 24px;align-items:start}
.cg .lbl2:first-child,.cg>div>.lbl2:first-child{margin-top:0}
.bt{min-width:84px;padding:0 14px}
.ch{height:32px;font-size:12px;padding:0 10px}
.dc{width:32px;height:32px;font-size:12.5px}
.nv{height:50px}.nv svg{width:20px;height:20px}
.sg2{height:36px}.ul{height:30px}'''
bodyC=f'''<div class="split">
<div class="cd col"><h4>Foundation<span class="prop">Primitive → Semantic</span></h4>
<div class="lbl2">Typography<small>Pretendard · 텍스트 스타일 14종 · 최소 12px</small></div>
<div class="fw"><div class="font">Pretendard</div><div class="wts"><b>Bold</b><span style="font-weight:600">SemiBold</span><span>Regular</span></div></div>
<div style="margin-top:6px">{trows2}</div>
<div class="lbl2">Emotion Color<small>감정 8색 · 각각 fill · tint · border · text 4역할</small></div><div class="eg2">{emo2}</div>
<div class="lbl2">Neutral<small>웜 그레이 10단계</small></div><div class="ng2">{neu2}</div><div class="ngl"><span>0 #ffffff</span><span>500 #6f6964 (보조 글자, 4.5:1)</span><span>950 #2b2733</span></div></div>
<div class="cd col"><h4>Components<span class="prop">Figma 프로퍼티 = 코드 props</span></h4>
<div class="cg" style="margin-top:12px">
<div><div class="lbl2">Button<small>Style × Size × State</small></div>
<div class="row"><span class="sz">48px</span>{btn('S','L',label='이전')}{btn('P','L')}</div>
<div class="row" style="margin-top:6px"><span class="sz">40px</span>{btn('S','M',label='이전')}{btn('P','M')}</div>
<div class="row" style="margin-top:6px"><span class="sz">Off</span>{btn('P','L',True,'저장하기')}<span class="tg on" style="margin-left:6px"></span><span class="tg"></span></div>
<div class="lbl2">EmotionChip<small>emotion × selected · 최대 3개</small></div>
<div class="row">{chip('angry','화난',False)}{chip('angry','짜증난',True)}{chip('angry','답답한',True)}</div>
<div class="lbl2">DayCell<small>emotion · selected · isToday</small></div>
<div class="row" style="gap:5px">{day(1,'complex')}{day(2)}{day(3,'flutter')}{day(4,'anxious')}{day(5,'angry',sel=True)}{day(6,today=True)}{day(7)}</div></div>
<div><div class="lbl2">Bottom Navigation<small>Default · Active</small></div>{nav(0)}<div style="height:6px"></div>{nav(2)}
<div class="lbl2">Tabs<small>segment · underline</small></div>
<div class="sg2"><span>일간</span><span class="on">주간</span><span>월간</span></div>
<div class="ul" style="margin-top:6px"><span class="on">감정 리포트</span><span>나의 창작물</span></div>
<div class="lbl2">Card UI<small>이번 주 기록</small></div><div class="rc2"><div>화남 · 짜증난<small>오늘</small></div><p>회의가 길어져서 짜증이 났다.</p></div></div>
</div></div></div>'''
sC=slide('감정로그 · Design System','Develop · Design System','감정이 어느 화면에서나 <em>같은 색 · 같은 규격</em>으로 보이도록 디자인 시스템을 세웠습니다.',
 '흩어진 색 984종 · 글자 크기 65종을 <b>토큰과 텍스트 스타일로 정리</b>하고, 화면마다 따로 만들던 요소를 <b>프로퍼티를 가진 컴포넌트</b>로 묶었습니다.',bodyC,
 'Figma에서 <b>Style=Primary, Size=Large</b>를 고르면 코드는 <b>&lt;Button variant="primary" size="lg" /&gt;</b>, 색은 <b>var(--color-…)</b>로 그대로 이어집니다.',cssC)
open('s11c.html','w').write(sC);print('merged ok')

# ================= Clean single slide =================
emoStrip=''.join(f'<div class="es"><i style="background:{f}"></i><small>{l}</small></div>' for k,l,f,t,b,x in EM)
neuStrip=''.join(f'<i style="background:{h}"></i>' for n,h in NEU)
cssD=cssB+'''.panel{margin-top:30px;height:458px;border-radius:20px;background:#fff;box-shadow:0 16px 36px -26px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);display:grid;grid-template-columns:1.15fr 1fr 1fr}
.pc{padding:30px 34px;border-left:1px solid var(--line)}.pc:first-child{border-left:0}
.pc h4{font-size:16px;font-weight:700;letter-spacing:-.03em;margin-bottom:22px}
.it+.it{margin-top:26px}
.it>small{display:block;font-size:12.5px;font-weight:600;color:var(--ink3);margin-bottom:10px;letter-spacing:0}
.font{font-size:44px;font-weight:700;letter-spacing:-.05em;line-height:1}
.wts{display:flex;gap:16px;margin-top:10px;font-size:13px;color:var(--ink2)}
.estrip{display:grid;grid-template-columns:repeat(8,1fr);gap:4px}
.es i{display:block;height:44px;border-radius:8px}.es small{display:block;margin-top:6px;font-size:11.5px;color:var(--ink2);text-align:center;font-weight:500}
.nstrip{display:grid;grid-template-columns:repeat(10,1fr);height:28px;border-radius:8px;overflow:hidden;border:1px solid var(--line)}.nstrip i{display:block}
.row{gap:8px}
.bt{min-width:92px}
.nv{height:56px}'''
bodyD=f'''<div class="panel">
<div class="pc"><h4>Foundation</h4>
<div class="it"><small>Typography</small><div class="font">Pretendard</div><div class="wts"><b>Bold</b><span style="font-weight:600">SemiBold</span><span>Regular</span><span style="color:var(--ink3)">· 최소 12px</span></div></div>
<div class="it"><small>Emotion Color</small><div class="estrip">{emoStrip}</div></div>
<div class="it"><small>Grayscale</small><div class="nstrip">{neuStrip}</div></div></div>
<div class="pc"><h4>Components</h4>
<div class="it"><small>Button</small><div class="row">{btn('S','L',label='이전')}{btn('P','L')}</div><div class="row" style="margin-top:8px">{btn('S','M',label='이전')}{btn('P','M')}</div></div>
<div class="it"><small>Emotion Chip</small><div class="row">{chip('angry','화난',False)}{chip('angry','짜증난',True)}{chip('angry','답답한',True)}</div></div>
<div class="it"><small>Day Cell</small><div class="row" style="gap:6px">{day(1,'complex')}{day(2)}{day(3,'flutter')}{day(4,'anxious')}{day(5,'angry',sel=True)}{day(6,today=True)}</div></div></div>
<div class="pc"><h4>&nbsp;</h4>
<div class="it"><small>Bottom Navigation</small>{nav(0)}</div>
<div class="it"><small>Tabs</small><div class="sg2"><span>일간</span><span class="on">주간</span><span>월간</span></div><div class="ul" style="margin-top:10px"><span class="on">감정 리포트</span><span>나의 창작물</span></div></div>
<div class="it"><small>Card</small><div class="rc2"><div>화남 · 짜증난<small>오늘</small></div><p>회의가 길어져서 짜증이 났다.</p></div></div></div>
</div>'''
sD=slide('감정로그 · Design System','Develop · Design System','감정이 어느 화면에서나 <em>같은 색, 같은 규격</em>으로 보이도록 디자인 시스템을 세웠습니다.',
 '흩어진 색과 글자 크기를 토큰으로 정리하고, 화면마다 따로 만들던 요소를 <b>컴포넌트로 묶었습니다.</b>',bodyD,
 'Figma의 변수와 프로퍼티를 <b>코드의 CSS 변수 · props와 같은 이름</b>으로 맞춰, 한쪽을 고치면 다른 쪽도 그대로 따라옵니다.',cssD)
open('s11d.html','w').write(sD);print('clean ok')

# ================= E: Foundation / Token · Mode / Components =================
tsty=[('title/lg','24 Bold',24,700,'짜증난 마음에 있어요'),('title/md','20 Bold',20,700,'어떤 감정을 남길까요?'),('body/lg','16 Regular',16,400,'회의가 길어져서 짜증이 났다.'),
      ('label/md','13 Bold',13,700,'화남 · 짜증난'),('caption/sm','12 SemiBold',12,600,'10월 5일 월요일')]
tsE=''.join(f'<div class="ts"><span style="font-size:{px}px;font-weight:{w}">{s}</span><em>{z}</em></div>' for n,z,px,w,s in tsty)
keyc=[('#2b2733','action/primary','주요 버튼 · 선택','흰 글자 14.6:1'),('#6f6964','text/tertiary','보조 글자','캔버스 위 5.1:1'),('#a23b32','emotion/*/text','감정 글자 8종','tint 위 4.8~5.7:1')]
kcE=''.join(f'<div class="kc"><i style="background:{h}"></i><div><b>{n}</b><span>{r}</span></div><em>{c}</em></div>' for h,n,r,c in keyc)
def modecard(k,word,sent):
    _,l,f,t,b,x=em(k)
    return f'''<div class="mc"><div class="mh"><span class="ch" style="background:{t};border-color:{b};color:{x}"><i style="background:{f}"></i>{word}</span><span class="dc" style="background:{t}"><b style="font-weight:700">5</b><s style="background:{f}"></s></span></div>
<div class="rc2 m" style="--bar:{f}"><div>{l} · {word}<small>오늘</small></div><p>{sent}</p></div><code>emotion = {k}</code></div>'''
cssE=cssD+'''.panel{grid-template-columns:1fr 1fr 1.08fr;height:492px;margin-top:22px}
.pc{padding:22px 26px}.pc h4{margin-bottom:12px;display:flex;align-items:baseline;gap:8px}.pc h4 small{font-size:12px;font-weight:500;color:var(--ink3);letter-spacing:0}
.it+.it{margin-top:16px}.it>small{margin-bottom:7px}
.pc em,.pc small,.pc code,.tflow{letter-spacing:0}
.ts{display:flex;justify-content:space-between;align-items:baseline;gap:10px;padding:3px 0;border-bottom:1px solid var(--line);white-space:nowrap}.ts:last-child{border-bottom:0}
.ts span{color:var(--ink);letter-spacing:-.03em;overflow:hidden;text-overflow:ellipsis}.ts em{font-style:normal;font-size:11px;color:var(--ink3);flex:none}
.estrip{gap:3px}.es i{height:22px;border-radius:6px}.es small{font-size:11px;margin-top:4px}
.kc{display:grid;grid-template-columns:18px 1fr auto;align-items:center;gap:10px;padding:3px 0}.kc i{width:18px;height:18px;border-radius:6px}
.kc b{display:block;font-size:12px;font-weight:700;font-family:ui-monospace,monospace;letter-spacing:-.02em}.kc span{font-size:11px;color:var(--ink3);margin-left:6px}.kc div{display:flex;align-items:baseline}.kc em{font-style:normal;font-size:11.5px;font-weight:700;color:#5a4ab3;background:#efecfa;border-radius:999px;padding:2px 8px}
.tier{display:grid;grid-template-columns:1fr 14px 1fr 14px 1fr;align-items:center;text-align:center}
.tier div{border-radius:12px;background:#fbfaf8;box-shadow:inset 0 0 0 1px var(--line);padding:9px 4px}.tier b{display:block;font-size:22px;font-weight:700;letter-spacing:-.03em}.tier small{font-size:11px;color:var(--ink3);font-weight:600}
.tier>i{font-style:normal;color:var(--ink4);font-size:12px}
.tflow{margin-top:8px;font-size:11px;color:var(--ink3)}.tflow code{font-size:10.5px}
.mode{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mc{border-radius:12px;background:#fbfaf8;box-shadow:inset 0 0 0 1px var(--line);padding:9px}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:7px}.mh .ch{height:30px;font-size:12px;padding:0 10px}.mh .dc{width:32px;height:32px}
.rc2.m{padding:8px 10px 8px 16px}.rc2.m:before{background:var(--bar)}.rc2.m div{font-size:12px}.rc2.m p{font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mc code{display:block;margin-top:4px;font-size:10.5px;color:var(--ink3);background:none;padding:0;text-align:center}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;text-align:center}.stats div{border-radius:10px;background:#fbfaf8;box-shadow:inset 0 0 0 1px var(--line);padding:7px 2px}
.stats b{display:block;font-size:18px;font-weight:700;letter-spacing:-.03em}.stats small{font-size:10.5px;color:var(--ink3);font-weight:600}
.note{margin-top:7px;font-size:11px;color:var(--ink3);line-height:1.45}
.cg{display:grid;grid-template-columns:1fr 1fr;gap:14px 14px}.cg .it{margin:0}.cg .full{grid-column:1/-1}
.cg .bt{min-width:0;padding:0 14px;height:40px;font-size:13.5px;border-radius:16px}
.inp{border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px #e4dfda;padding:9px 12px;font-size:13px;color:var(--ink)}.inp small{display:block;text-align:right;font-size:11px;color:var(--ink3);margin-top:2px}
.hero{border-radius:16px;padding:12px 14px;background:linear-gradient(135deg,#ffd9cf,#f6a395);font-size:15px;font-weight:700;letter-spacing:-.03em;line-height:1.35;color:#1c1a18}.hero em{font-style:normal;color:#a23b32}
.sheet{border-radius:16px 16px 0 0;background:#fff;box-shadow:0 0 0 1px var(--line),0 -6px 16px -10px rgba(0,0,0,.2);padding:8px 10px 10px}.sheet:before{content:"";display:block;width:28px;height:3px;border-radius:2px;background:#dedbd8;margin:0 auto 7px}
.sheet .row{gap:2px;justify-content:space-between}.sheet .ei{width:34px}.sheet .ei i{width:26px;height:26px}.sheet .ei i svg{width:15px;height:15px}.sheet .ei small{font-size:10px}
.nv{height:50px}'''
bodyE=f'''<div class="panel">
<div class="pc"><h4>Foundation<small>글자 · 색의 기준</small></h4>
<div class="it"><small>Pretendard · 텍스트 스타일 5단계</small>{tsE}</div>
<div class="it"><small>감정 8색 — 색이 곧 데이터</small><div class="estrip">{emoStrip}</div></div>
<div class="it"><small>주요 색과 대비</small>{kcE}</div></div>
<div class="pc"><h4>Token · Mode<small>값 → 역할 → 부품</small></h4>
<div class="it"><small>3단 구조</small><div class="tier"><div><b>54</b><small>Primitive</small></div><i>→</i><div><b>59</b><small>Semantic</small></div><i>→</i><div><b>4</b><small>Component</small></div></div>
<div class="tflow"><code>coral/400</code> → <code>emotion/angry/fill</code> → EmotionChip · DayCell</div></div>
<div class="it"><small>감정 모드 — 같은 컴포넌트, 감정 키만 바꿈</small><div class="mode">{modecard('angry','짜증난','회의가 길어져서 짜증이 났다.')}{modecard('calm','편안한','산책하고 나니 마음이 가라앉았다.')}</div></div>
<div class="it"><small>Figma 연동</small><div class="stats"><div><b>147</b><small>변수</small></div><div><b>14</b><small>텍스트 스타일</small></div><div><b>3</b><small>이펙트</small></div><div><b>0</b><small>하드코딩</small></div></div>
<div class="note">하드코딩 0은 Figma 컴포넌트 기준(칠·선 145개 모두 변수). 코드 색상 토큰화는 45%.</div></div></div>
<div class="pc"><h4>Components<small>v73 프로토타입 실제 부품</small></h4>
<div class="cg">
<div class="it full"><small>Button · 기본 · 보조 · 비활성</small><div class="row" style="flex-wrap:nowrap">{btn('P','M',label='저장하기')}{btn('S','M',label='이전')}{btn('P','M',dis=True,label='다음')}</div></div>
<div class="it"><small>Emotion Chip</small><div class="row">{chip('angry','짜증난',True)}{chip('angry','화난',False)}</div></div>
<div class="it"><small>Toggle · Day Cell</small><div class="row"><span class="tg on"></span>{day(4,'anxious')}{day(5,'angry',sel=True)}</div></div>
<div class="it"><small>Input · 오늘의 한 문장</small><div class="inp">회의가 길어져서 짜증이 났다.<small>16 / 100</small></div></div>
<div class="it"><small>Hero Card</small><div class="hero">오늘의 감정은<br><em>짜증난 마음</em>에 있어요</div></div>
<div class="it"><small>감정 선택 시트</small><div class="sheet"><div class="row">{emoi('calm')}{emoi('joy')}{emoi('sad')}{emoi('angry',True)}</div></div></div>
<div class="it"><small>Bottom Tab Bar</small>{nav(0)}</div>
</div></div>
</div>'''
sE=slide('감정로그 · Design System','Develop · Design System','감정이 어느 화면에서나 <em>같은 색, 같은 규격</em>으로 보이도록 디자인 시스템을 세웠습니다.',
 '<b>Foundation</b>에서 글자와 색의 기준을 정하고, <b>토큰</b>으로 값과 역할을 나눈 뒤, 화면마다 따로 만들던 요소를 <b>컴포넌트</b>로 묶었습니다.',bodyE,
 '감정 색은 장식이 아니라 <b>데이터</b>입니다. 컴포넌트는 감정 키 하나만 받아 칩 · 달력 · 카드 색을 함께 바꿉니다.',cssE)
open('s11e.html','w').write(sE);print('E ok')

# ================= F: prioritized, card layout =================
tsF=''.join(f'<div class="ts"><span style="font-size:{px}px;font-weight:{w}">{s}</span><em>{z}</em></div>' for z,px,w,s in [('Title · 24 / 700',24,700,'짜증난 마음'),('Body · 16 / 400',16,400,'회의가 길어져서 짜증이 났다.'),('Caption · 12 / 600',12,600,'10월 5일 월요일')])
emoDots=''.join(f'<i style="background:{f}"></i>' for k,l,f,t,b,x in EM)
colF=f'''<div class="cr"><span class="dots">{emoDots}</span><b>감정 8색</b><span>그날의 감정 · 기록</span></div>
<div class="cr"><i style="background:#2b2733"></i><b>차콜</b><span>누르는 것 · 선택</span><em>14.6:1</em></div>
<div class="cr"><i style="background:#6f6964"></i><b>웜 그레이</b><span>보조 정보</span><em>5.1:1</em></div>'''
def mcF(k,word,sent):
    _,l,f,t,b,x=em(k)
    return f'''<div class="mw"><div class="mcf" style="background:{t};box-shadow:inset 0 0 0 1.5px {b}"><small style="color:{x}">10월 5일</small><b style="color:{x}">{l} · {word}</b><p>{sent}</p>
<div class="mrow"><span class="ch" style="background:#fff;border-color:{b};color:{x}"><i style="background:{f}"></i>{word}</span><span class="dc" style="background:#fff"><b style="font-weight:700">5</b><s style="background:{f}"></s></span></div></div><code style="color:{x}">emotion = {k}</code></div>'''
week=''.join([day(1,'complex'),day(2,'calm'),day(3,'flutter'),day(4,'anxious'),day(5,'angry',sel=True),day(6),day(7)])
cssF=cssB+'''body{background:#faf9f4}
.gf{margin-top:28px;display:grid;grid-template-columns:1fr 1.12fr 1fr;gap:18px;height:478px}
.cdf{background:#fff;border-radius:20px;box-shadow:0 16px 36px -28px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);padding:24px 26px;display:flex;flex-direction:column}
.cdf h4{font-size:16px;font-weight:700;letter-spacing:-.03em;margin-bottom:14px}
.stack{display:grid;grid-template-rows:auto 1fr;gap:16px}
.font{font-size:40px;font-weight:800;letter-spacing:-.05em;line-height:1;margin-bottom:12px}
.ts{display:flex;justify-content:space-between;align-items:baseline;gap:10px;padding:5px 0;white-space:nowrap}
.ts span{letter-spacing:-.03em}.ts em{font-style:normal;font-size:11.5px;color:var(--ink3);font-weight:600;letter-spacing:0}
.cr{display:grid;grid-template-columns:62px 72px 1fr auto;align-items:center;gap:8px;height:42px;font-size:13px}
.cr>i{width:26px;height:26px;border-radius:8px}.cr b{font-weight:700}.cr span{color:var(--ink2)}
.cr em{font-style:normal;font-size:11.5px;font-weight:700;color:#5a4ab3;background:#efecfa;border-radius:999px;padding:2px 8px;letter-spacing:0}
.dots{display:grid;grid-template-columns:repeat(4,12px);gap:3px}.dots i{width:12px;height:12px;border-radius:50%}
.tier{display:grid;grid-template-columns:1fr 18px 1fr 18px 1fr;align-items:center;text-align:center}
.tier div{border-radius:12px;background:#f5f3fb;padding:9px 4px}.tier small{display:block;font-size:11.5px;color:#5a4ab3;font-weight:700;letter-spacing:0}.tier b{font-size:22px;font-weight:700}
.tier>i{font-style:normal;color:var(--ink4)}
.cap{text-align:center;font-size:12.5px;color:var(--ink2);line-height:1.55;margin:14px 0}
.stage{flex:1;border-radius:16px;background:linear-gradient(180deg,#f6f4fb,#faf9f4);display:flex;align-items:center;justify-content:center;gap:14px;padding:0 16px}
.mw{text-align:center}.mw code{display:block;margin-top:8px;font-size:11.5px;font-weight:700;background:none;padding:0;letter-spacing:0}
.mcf{width:186px;border-radius:16px;padding:14px;text-align:left}.mcf small{font-size:11.5px;font-weight:600}.mcf b{display:block;font-size:16px;font-weight:700;margin:2px 0 4px;letter-spacing:-.03em}
.mcf p{font-size:12px;color:#5f5a56;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mrow{display:flex;justify-content:space-between;align-items:center;margin-top:10px}.mrow .ch{height:30px;font-size:12px;padding:0 10px}.mrow .dc{width:32px;height:32px}
.brow{display:grid;grid-template-columns:1fr 1fr;gap:10px}.brow .bt{height:48px;border-radius:20px;font-size:15px;min-width:0}
.crow{display:flex;justify-content:center;gap:6px;margin:14px 0}.crow .ch{height:32px;font-size:12px;padding:0 10px}
.stage.h{flex-direction:column;gap:12px;padding:18px}
.hero{width:100%;border-radius:18px;padding:16px 18px;background:linear-gradient(135deg,#ffd9cf,#f6a395)}
.hero p{font-size:19px;font-weight:700;letter-spacing:-.03em;line-height:1.35;color:#1c1a18}.hero p em{font-style:normal;color:#a23b32}
.wk{display:flex;justify-content:space-between;margin-top:12px;background:rgba(255,255,255,.7);border-radius:14px;padding:4px}
.stage.h .nv{width:100%;height:52px}'''
bodyF=f'''<div class="gf">
<div class="stack"><div class="cdf"><h4>Typography</h4><div class="font">Pretendard</div>{tsF}</div>
<div class="cdf"><h4>Color</h4>{colF}</div></div>
<div class="cdf"><h4>Token · Mode</h4><div class="tier"><div><small>Primitive</small><b>54</b></div><i>→</i><div><small>Semantic</small><b>59</b></div><i>→</i><div><small>Component</small><b>4</b></div></div>
<p class="cap">같은 카드 · 칩 · 달력 칸을 그대로 쓰고 감정 키만 바꿔,<br>그날의 감정을 색으로 구분합니다.</p>
<div class="stage">{mcF('angry','짜증난','회의가 길어져서 짜증이 났다.')}{mcF('calm','편안한','산책하고 나니 가라앉았다.')}</div></div>
<div class="cdf"><h4>Components</h4><div class="brow">{btn('P','L',label='저장하기')}{btn('S','L',label='이전')}</div>
<div class="crow">{chip('angry','짜증난',True)}{chip('angry','화난',False)}{chip('calm','편안한',True)}{chip('joy','기쁜',False)}</div>
<div class="stage h"><div class="hero"><p>오늘의 감정은<br><em>짜증난 마음</em>에 있어요</p><div class="wk">{week}</div></div>{nav(0)}</div></div>
</div>'''
sF=slide('감정로그 · Design System','Develop · Design System','색 하나에 <em>감정 하나</em>, 토큰과 컴포넌트로 화면 전체를 묶었습니다.',
 'Primitive 54 → Semantic 59 → Component 4. Figma 변수 147개와 CSS 변수 이름을 1:1로 맞추고, Figma 컴포넌트에는 hex를 직접 쓰지 않았습니다.',bodyF,
 '감정색은 기록, 차콜은 누르는 것 — 색의 의미를 고정해 글보다 먼저 그날의 감정이 읽히게 했습니다.',cssF)
open('s11f.html','w').write(sF);print('F ok')

# ================= G: reference structure (Type+Spacing / Color / Components) =================
spG=''.join(f'<div class="sp"><i style="width:{v*.9}px;height:{v*.9}px"></i><small>{v}</small></div>' for v in [2,4,8,12,16,20,24,32,40,48])
raG=''.join(f'<div class="ra"><i style="border-radius:{min(v,22)}px"></i><small>{lab}</small></div>' for v,lab in [(8,'8 · 태그'),(12,'12 · 칩'),(16,'16 · 카드'),(20,'20 · 버튼'),(999,'full · 토글')])
tiles=[('#e66f5c','#ffeae6','#a23b32','감정 8색','그날의 감정'),('#ffeae6','#fff5f2','#a23b32','감정 tint','기록한 날'),('#2b2733','#f1f0f3','#2b2733','차콜','누르는 것'),('#6f6964','#f3f0eb','#5f5a56','웜 그레이','보조 정보'),('#faf9f4','#fbfaf7','#5f5a56','아이보리','바탕')]
tlG=''.join(f'<div class="tl" style="background:{bg}"><i style="background:{f};box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)"></i><b style="color:{x}">{n}</b><small>{m}</small></div>' for f,bg,x,n,m in tiles)
emoRamp=''.join(f'<span style="background:{f}"><small>{l}</small></span>' for k,l,f,t,b,x in EM)
coral=[('50','#ffeae6','tint · 배경','#a23b32'),('400','#e66f5c','fill · 점','#fff'),('600','#c8493d','border · 선','#fff'),('800','#a23b32','text · 5.7:1','#fff')]
crRamp=''.join(f'<span style="background:{h};color:{c}"><small>{n}</small><small>{r}</small></span>' for n,h,r,c in coral)
neuR=[('950','#2b2733','13.8:1','#fff'),('900','#1c1a18','16.5:1','#fff'),('600','#5f5a56','6.5:1','#fff'),('500','#6f6964','5.1:1','#fff'),('400','#a39b95','장식','#fff'),('200','#e4dfda','테두리','#5f5a56')]
neRamp=''.join(f'<span style="background:{h};color:{c}"><small>{n}</small><small>{r}</small></span>' for n,h,r,c in neuR)
cssG=cssF+'''.gg{margin-top:28px;display:grid;grid-template-columns:1fr 1.14fr 1.08fr;gap:18px;height:478px}
.cdf{padding:22px 24px}.cdf h4{margin-bottom:12px}
.font{font-size:38px;margin-bottom:10px}.ts{padding:4px 0}
.sps{display:flex;align-items:flex-end;gap:7px;height:52px}.sp{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px}
.sp i{display:block;background:#d9d3f1;border-radius:3px;min-width:2px;min-height:2px}.sp small,.ra small{font-size:10.5px;color:var(--ink3);font-weight:600;letter-spacing:0;white-space:nowrap}
.ras{display:flex;gap:8px;margin-top:14px}.ra{display:flex;flex-direction:column;align-items:center;gap:4px}.ra i{display:block;width:52px;height:30px;background:#f1eefc;border:1.5px solid #b3a8e8}
.nt{font-size:11.5px;color:var(--ink3);margin-top:8px;letter-spacing:0}
.tls{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.tl{border-radius:12px;padding:10px 9px}
.tl i{display:block;width:20px;height:20px;border-radius:6px;margin-bottom:8px}.tl b{display:block;font-size:13px;font-weight:700;letter-spacing:-.03em}.tl small{font-size:11px;color:var(--ink2);letter-spacing:0}
.cap{margin:12px 0}
.stage.v{flex-direction:column;align-items:stretch;justify-content:space-around;gap:0;padding:14px 16px}
.rl{font-size:11.5px;font-weight:700;color:var(--ink2);margin-bottom:6px;letter-spacing:0}.rl small{font-weight:500;color:var(--ink3);margin-left:4px}
.ramp{display:flex;height:40px;border-radius:10px;overflow:hidden}.ramp span{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:0 0 5px 7px;font-size:10px;font-weight:700;line-height:1.2}
.ramp small{font-size:10px;letter-spacing:0}.ramp.e span{color:#fff;text-shadow:0 0 2px rgba(0,0,0,.25)}
.inp{border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px #e4dfda;color:var(--ink)}.inp small{display:block;text-align:right;font-size:10.5px;color:var(--ink3);margin-top:2px}
.bgrid{display:grid;grid-template-columns:1fr 1fr;gap:8px}.bgrid .bt{height:44px;border-radius:20px;font-size:14px;min-width:0}
.ins{display:grid;grid-template-columns:1fr 1fr;gap:8px}.inp{font-size:12px;padding:9px 11px}.inp.ph{color:#a39b95}.inp.ph small{visibility:hidden}
.cts{display:flex;align-items:center;gap:6px}.cts .ch{height:32px;font-size:12px;padding:0 10px}.cts .tg{flex:none}
.dcs{display:flex;gap:6px;align-items:center}'''
bodyG=f'''<div class="gg">
<div class="stack"><div class="cdf"><h4>Typography</h4><div class="font">Pretendard</div>{tsF}</div>
<div class="cdf"><h4>Spacing · Radius</h4><div class="sps">{spG}</div><div class="nt">4 · 8 기준 10단계 · padding · margin · gap 1,970곳을 토큰으로</div>
<div class="ras">{raG}</div></div></div>
<div class="cdf"><h4>Color</h4><div class="tls">{tlG}</div>
<p class="cap">색마다 맡는 역할은 하나 — 글보다 색으로 먼저 그날의 감정을 읽습니다.</p>
<div class="stage v"><div><div class="rl">Emotion<small>감정 8색 · fill</small></div><div class="ramp e">{emoRamp}</div></div>
<div><div class="rl">Coral<small>화남 한 감정의 4가지 역할</small></div><div class="ramp">{crRamp}</div></div>
<div><div class="rl">Neutral<small>글자 대비 (캔버스 위)</small></div><div class="ramp">{neRamp}</div></div></div></div>
<div class="cdf"><h4>Components</h4><div class="bgrid">{btn('P','L',label='저장하기')}{btn('S','L',label='이전')}{btn('P','M',label='기록하기')}{btn('P','L',dis=True,label='다음')}</div>
<p class="cap">기본 · 보조 · 비활성 × L 48 / M 40 — 상태는 토큰으로만 바뀝니다.</p>
<div class="stage v"><div><div class="rl">Input<small>빈 칸 / 입력 중</small></div><div class="ins"><div class="inp ph">오늘을 한 문장으로<small>0 / 100</small></div><div class="inp">회의가 길어져서…<small>16 / 100</small></div></div></div>
<div><div class="rl">Chip · Toggle</div><div class="cts">{chip('angry','짜증난',True)}{chip('angry','화난',False)}<span class="tg on"></span><span class="tg"></span></div></div>
<div><div class="rl">Day Cell<small>기록한 날 · 선택 · 빈 날</small></div><div class="dcs">{day(2,'calm')}{day(3,'flutter')}{day(4,'anxious')}{day(5,'angry',sel=True)}{day(6)}{day(7)}</div></div></div></div>
</div>'''
sG=slide('감정로그 · Design System','Develop · Design System','색 하나에 <em>감정 하나</em>, 토큰과 컴포넌트로 화면 전체를 묶었습니다.',
 'Primitive 54 → Semantic 59 → Component 4. Figma 변수 147개와 CSS 변수 이름을 1:1로 맞추고, Figma 컴포넌트에는 hex를 직접 쓰지 않았습니다.',bodyG,
 '감정색은 기록, 차콜은 누르는 것 — 색의 의미를 고정해 글보다 먼저 그날의 감정이 읽히게 했습니다.',cssG)
open('s11g.html','w').write(sG);print('G ok')
