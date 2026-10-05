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
