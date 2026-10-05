import re, json, sys, collections
SRC=sys.argv[2] if len(sys.argv)>2 else '감정일기_v70.html'; OUT=sys.argv[1] if len(sys.argv)>1 else 'v71.html'
NOFONT='--nofont' in sys.argv
t=open(SRC,encoding='utf-8').read()
stats=collections.Counter()
def rep(old,new,count=1,s=None):
    global t
    n=t.count(old)
    assert n==count, (old[:80],n,count)
    t=t.replace(old,new); stats['replace']+=1

# ---------- 1. 문서 제목 ----------
rep('<title>감정일기 v70</title>','<title>감정일기 v71</title>')

# ---------- 2. 정적 토큰 파일 + Pretendard ----------
tokens=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','design-tokens.css'),encoding='utf-8').read()
font_link='' if NOFONT else '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">\n'
i=t.find('</title>')+len('</title>')
t=t[:i]+'\n'+font_link+'<style id="design-tokens">\n'+tokens+'</style>'+t[i:]

# ---------- 3. 데모 초기화: URL로 끌 수 있게, 누락 키 포함 ----------
rep("window.EMOTION_DIARY_DEMO=true;",
    "window.EMOTION_DIARY_DEMO=!/[?&]demo=0\\b/.test(location.search);")
rep("return /^emotion-(diary|log)[:-]/.test(k)","return /^emotion-(diary|log|app-home)[:-]/.test(k)")

# ---------- 4. EMOTION_TOKENS: 색은 CSS 토큰에서 읽기 ----------
i=t.find('<script id="emotion-tokens">'); j=t.find('</script>',i)
s=t[i:j]
m=re.search(r'var EMOTIONS=(\[.*?\]);\n',s,re.S)
E=json.loads(m.group(1))
for e in E:
    for k in ['fill','tint','border','text','glow']: e.pop(k,None)
new_s='''<script id="emotion-tokens">
/* 감정의 유일한 원본(데이터). 키·라벨·좌표·그룹·세부 톤은 여기서, 색(fill/tint/border/text/glow)은 #design-tokens CSS에서만 정의한다.
   JS는 CSS 토큰 값을 읽어 쓰고, 투명도는 alpha()로 color-mix를 만든다. */
(function(){
  var EMOTIONS=%s;
  var root=getComputedStyle(document.documentElement);
  function token(name){return root.getPropertyValue(name).trim()}
  EMOTIONS.forEach(function(e){
    ['fill','tint','border','text'].forEach(function(f){e[f]=token('--color-emotion-'+e.key+'-'+f)});
    e.glow=[token('--color-emotion-'+e.key+'-glow-start'),token('--color-emotion-'+e.key+'-glow-end')];
    if(!e.fill&&window.console)console.warn('[emotion-tokens] 토큰 누락: '+e.key);
  });
  var byKey={},ALIASES={unknown:'angry',anger:'angry',peace:'calm',sadness:'sad',anxiety:'anxious',lethargy:'empty','분노':'angry','모르겠음':'angry'};
  EMOTIONS.forEach(function(e){byKey[e.key]=e;ALIASES[e.label]=e.key});
  function id(v){if(v==null||v==='')return v;return byKey[v]?v:(ALIASES[v]||v)}
  function map(field){var o={};EMOTIONS.forEach(function(e){o[e.key]=e[field]});return o}
  function get(k){return byKey[id(k)]||null}
  function hex(k,field){var e=get(k);return e?e[field||'fill']:null}
  function alpha(color,percent){return color?'color-mix(in srgb, '+color+' '+percent+'%%, transparent)':color}
  window.EMOTION_TOKENS={list:EMOTIONS,keys:EMOTIONS.map(function(e){return e.key}),id:id,map:map,get:get,hex:hex,alpha:alpha};
  /* 날짜는 이 함수들로만 만든다 */
  var WD='일월화수목금토';
  window.APP_DATE={
    today:function(){return new Date()},
    year:function(d){return (d||new Date()).getFullYear()},
    month:function(d){return (d||new Date()).getMonth()+1},
    weekday:function(d){return WD[(d||new Date()).getDay()]},
    label:function(d){d=d||new Date();return (d.getMonth()+1)+'월 '+d.getDate()+'일 '+WD[d.getDay()]+'요일'},
    dayInMonth:function(k){var n=new Date(),last=new Date(n.getFullYear(),n.getMonth()+1,0).getDate();return new Date(n.getFullYear(),n.getMonth(),Math.min(k,last))}
  };
})();
''' % json.dumps(E,ensure_ascii=False)
t=t[:i]+new_s+t[j:]

# ---------- 5. hex 뒤에 투명도 붙이기 → alpha() ----------
for var in ['color','A']:
    for hx,pct in [('38',22),('24',14),('2b',17)]:
        n=t.count(f'{var}+"{hx}"')
        t=t.replace(f'{var}+"{hx}"',f'EMOTION_TOKENS.alpha({var},{pct})'); stats['alpha']+=n
n=t.count('col+"24"'); t=t.replace('col+"24"','EMOTION_TOKENS.alpha(col,14)'); stats['alpha']+=n
n=t.count("main.color+'18'"); t=t.replace("main.color+'18'","EMOTION_TOKENS.alpha(main.color,9)"); stats['alpha']+=n
n=t.count("item[3]+'18'"); t=t.replace("item[3]+'18'","EMOTION_TOKENS.alpha(item[3],9)"); stats['alpha']+=n

# ---------- 6. 날짜 조립을 APP_DATE로 ----------
pairs=[
 ("new Date(new Date().getFullYear(),new Date().getMonth(),k)","APP_DATE.dayInMonth(k)"),
 ("new Date(new Date().getFullYear(),new Date().getMonth(),o)","APP_DATE.dayInMonth(o)"),
 ("(new Date().getMonth()+1)+'월 '+new Date().getDate()+'일 '+['일','월','화','수','목','금','토'][new Date().getDay()]+'요일'","APP_DATE.label()"),
 ("(new Date().getMonth()+1)+'월 '+new Date().getDate()+'일 '+EMO_WD[new Date().getDay()]+'요일'","APP_DATE.label()"),
 ("EMO_WD[new Date().getDay()]+'요일'","APP_DATE.weekday()+'요일'"),
 ("`${new Date().getFullYear()}년 ${new Date().getMonth()+1}월","`${APP_DATE.year()}년 ${APP_DATE.month()}월"),
 ("`${new Date().getMonth()+1}월","`${APP_DATE.month()}월"),
 ("new Date().getFullYear()+\"년 \"+(new Date().getMonth()+1)+\"월\"","APP_DATE.year()+\"년 \"+APP_DATE.month()+\"월\""),
 ("(new Date().getMonth()+1)","APP_DATE.month()"),
 ("var EMO_TD=new Date().getDate();","var EMO_TD=APP_DATE.today().getDate();"),
 ("savedAt:APP_RECORD_DATE_KEY(new Date())","savedAt:APP_RECORD_DATE_KEY(APP_DATE.today())"),
]
for a,b in pairs:
    n=t.count(a); assert n>0,a; t=t.replace(a,b); stats['date:'+b[:22]]+=n

# ---------- 7. 죽은 코드 정리 ----------
i=t.find('var HOME_MATERIALS={'); j=t.find('}',t.find("angry:['부드러운 중간색'",i))+1
assert 0<i<j and j-i<1200; t=t[:i]+'/* HOME_MATERIALS: 사용처 없음, v71에서 삭제 */'+t[j:]
rep(',angry:"화남",upbeat:"설렘",settled:"평온",tense:"불안",heavy:"슬픔",mixed:"복합",angry:"화남"}',
    ',angry:"화남",upbeat:"설렘",settled:"평온",tense:"불안",heavy:"슬픔",mixed:"복합"}')

# ---------- 8. 런타임 보정 스크립트 제거 ----------
for sid in ['v57-minfont','v66-contrast']:
    i=t.find(f'<script id="{sid}">'); j=t.find('</script>',i)+len('</script>')
    assert i>0; t=t[:i]+f'<!-- {sid} 제거: 최소 글자 크기·대비는 #design-tokens의 텍스트 토큰이 담당 -->'+t[j:]

# ---------- 9. 감정 기록 카드: 덮어써져 보이지 않던 규칙 2벌 삭제 ----------
EM=['flutter','calm','joy','complex','sad','anxious','empty','angry']
blk1=''.join(f'\n.home-only-page .home-record-v72.emotion-{k}{{border-color:var(--color-emotion-{k}-border);background:var(--color-emotion-{k}-tint)}}' for k in EM)
blk2=''.join(f'\n.home-colorized-v94 .home-record-v72.emotion-{k}{{background:var(--color-emotion-{k}-tint)!important;border-color:var(--color-emotion-{k}-border)!important}}' for k in EM)
rep(blk1,'\n/* home-record-v72 감정별 배경·테두리: 아래 흰 카드 규칙이 최종 디자인이라 삭제 (v71) */')
rep(blk2,'')

# ---------- 10. CSS 값 → 토큰 ----------
def L(rgb):
    v=[x/255 for x in rgb];v=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in v];return .2126*v[0]+.7152*v[1]+.0722*v[2]
def parse_color(v):
    v=v.strip().lower()
    m=re.fullmatch(r'#([0-9a-f]{3}|[0-9a-f]{6})',v)
    if m:
        h=m.group(1); h=''.join(c*2 for c in h) if len(h)==3 else h
        return [int(h[k:k+2],16) for k in (0,2,4)],1.0
    m=re.fullmatch(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)',v)
    if m: return [int(m.group(k)) for k in (1,2,3)], float(m.group(4)) if m.group(4) else 1.0
    if v in('white',):return [255,255,255],1.0
    if v in('black',):return [0,0,0],1.0
    return None,None
def text_token(val,sel):
    imp='!important' if '!important' in val else ''
    core=val.replace('!important','').strip()
    rgb,a=parse_color(core)
    if rgb is None: return None
    if max(rgb)-min(rgb)>48: return None        # 감정색 등 채도 있는 색은 유지
    eff=[round(c*a+255*(1-a)) for c in rgb]      # 흰 배경 위 실효색
    cw=(1.05)/(L(eff)+0.05)
    if a==1 and min(rgb)>=245: tok='--color-text-inverse'
    elif a<1 and min(rgb)>=200: return None      # 어두운 배경 위 반투명 흰 글자
    elif sel.strip() and all(('disabled' in x or 'placeholder' in x) for x in re.sub(r':not\([^)]*\)','',sel).split(',')): tok='--color-text-disabled'
    elif cw>=10: tok='--color-text-primary'
    elif cw>=5.9: tok='--color-text-secondary'
    else: tok='--color-text-tertiary'
    return f'var({tok}){imp}'
FS=[(12,'caption-sm'),(13,'caption-lg'),(14,'body-sm'),(15,'body-md'),(16,'body-lg'),(18,'title-sm'),(20,'title-md'),(24,'title-lg'),(28,'display-sm'),(32,'display-lg')]
def fs_token(val,sel):
    imp='!important' if '!important' in val else ''
    m=re.fullmatch(r'([\d.]+)px',val.replace('!important','').strip())
    if not m: return None
    px=float(m.group(1))
    if px>34: return None
    px=max(px,12)
    best=min(FS,key=lambda f:(abs(f[0]-px),-f[0]))
    return f'var(--font-size-{best[1]}){imp}'
def fw_token(val,sel):
    imp='!important' if '!important' in val else ''
    v=val.replace('!important','').strip()
    v={'normal':'400','bold':'700','bolder':'700'}.get(v,v)
    if not v.isdigit(): return None
    n=int(v); tok='regular' if n<=450 else 'semibold' if n<=650 else 'bold'
    return f'var(--font-weight-{tok}){imp}'
RAD=[(4,'xs'),(8,'sm'),(12,'md'),(16,'lg'),(20,'xl'),(24,'2xl')]
def rad_token(val,sel):
    imp='!important' if '!important' in val else ''
    m=re.fullmatch(r'([\d.]+)px',val.replace('!important','').strip())
    if not m: return None
    px=float(m.group(1))
    if px==0: return None
    if px>=99: return f'var(--radius-full){imp}'
    if px>26: return None
    best=min(RAD,key=lambda r:(abs(r[0]-px),-r[0]))
    return f'var(--radius-{best[1]}){imp}'
def ff_token(val,sel):
    imp='!important' if '!important' in val else ''
    if re.search(r'arial|apple sd gothic|noto sans kr|pretendard|-apple-system|system-ui',val,re.I) and 'mono' not in val.lower():
        return f'var(--font-family-base){imp}'
    return None
HANDLERS={'color':text_token,'font-size':fs_token,'font-weight':fw_token,'border-radius':rad_token,'font-family':(None if NOFONT else ff_token)}
decl_re=re.compile(r'(^|[{;\s])(color|font-size|font-weight|border-radius|font-family)(\s*:\s*)([^;{}]+)')
def transform_css(css):
    out=[];pos=0
    # 규칙 단위: selector{body}
    for m in re.finditer(r'([^{}]*)\{([^{}]*)\}',css):
        sel,body=m.group(1),m.group(2)
        if '--' in body and 'design-tokens' in sel: pass
        def sub(dm):
            prop=dm.group(2); h=HANDLERS.get(prop)
            if not h: return dm.group(0)
            val=dm.group(4); r=h(val,sel.lower())
            if r is None: return dm.group(0)
            stats['css:'+prop]+=1
            return dm.group(1)+prop+dm.group(3)+r
        newbody=decl_re.sub(sub,body)
        def subvar(vm):
            name,val=vm.group(2),vm.group(4)
            if re.search(r'ink|text|muted|faint|weak',name):
                r=text_token(val,'')
                if r: stats['css:alias-color']+=1; return vm.group(1)+name+vm.group(3)+r
            if name=='--fp-sub':
                r=fs_token(val,'')
                if r: stats['css:alias-size']+=1; return vm.group(1)+name+vm.group(3)+r
            return vm.group(0)
        newbody=re.sub(r'(^|[{;\s])(--[a-z0-9-]+)(\s*:\s*)([^;{}]+)',subvar,newbody)
        out.append(css[pos:m.start(2)]+newbody); pos=m.end(2)
    out.append(css[pos:]); return ''.join(out)
parts=[];pos=0
for m in re.finditer(r'(<style(?![^>]*design-tokens)[^>]*>)(.*?)(</style>)',t,re.S):
    parts.append(t[pos:m.start(2)]); parts.append(transform_css(m.group(2))); pos=m.end(2)
parts.append(t[pos:]); t=''.join(parts)

# ---------- 10b. 선택된 세부 감정 칩 글자는 감정 text 토큰 ----------
old="style:active?{color:item[3],borderColor:item[3],background:EMOTION_TOKENS.alpha(item[3],9)}"
n=t.count(old); assert n==2,n
t=t.replace(old,"style:active?{color:EMOTION_TOKENS.hex(main.target,'text'),borderColor:item[3],background:EMOTION_TOKENS.alpha(item[3],9)}")

# ---------- 11. 남은 흰 카드 규칙의 중립색 토큰화 ----------
n=t.count('.home-record-v72.emotion-angry{border:1px solid #dedbd8!important;background:#fff!important;')
assert n==1
t=t.replace('.home-record-v72.emotion-angry{border:1px solid #dedbd8!important;background:#fff!important;',
            '.home-record-v72.emotion-angry{border:1px solid var(--color-border-card)!important;background:var(--color-bg-surface)!important;')

open(OUT,'w',encoding='utf-8').write(t)
for k,v in sorted(stats.items()): print(f'{v:6} {k}')
