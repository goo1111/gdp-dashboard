"""v71 → v72: 접근성 1단계 (확대 허용, 컨트롤 이름·라벨, 탭바 현재 위치, 달력 칸 감정 이름)
사용법: python3 tools/build_v72.py <출력.html> <v71.html>"""
import sys
OUT, SRC = sys.argv[1], sys.argv[2]
t = open(SRC, encoding='utf-8').read()

def rep(old, new, count):
    global t
    n = t.count(old)
    assert n == count, (old[:70], n, count)
    t = t.replace(old, new)

rep('<title>감정일기 v71</title>', '<title>감정일기 v72</title>', 1)

# 1. 확대 허용 (WCAG 1.4.4)
rep('content="width=device-width,initial-scale=1,maximum-scale=1"', 'content="width=device-width,initial-scale=1"', 1)

# 2. 알림 토글: 무엇을 켜고 끄는지 이름 붙이기 (aria-pressed는 이미 있음)
rep('h("button",{type:"button",className:props.value?"active":"","aria-pressed":props.value,',
    'h("button",{type:"button",className:props.value?"active":"","aria-label":props.label,"aria-pressed":props.value,', 1)

# 3. 본문 입력칸 라벨 (placeholder는 입력하면 사라짐)
rep("h('textarea',{value:journal,maxLength:100,",
    "h('textarea',{'aria-label':'오늘의 한 문장',value:journal,maxLength:100,", 2)
rep('h("textarea",{value:$txt,maxLength:100,', 'h("textarea",{"aria-label":"그날에 덧붙일 말",value:$txt,maxLength:100,', 1)
rep("(0,c.jsx)('textarea',{value:$txt,maxLength:100,", "(0,c.jsx)('textarea',{'aria-label':'그날에 덧붙일 말',value:$txt,maxLength:100,", 1)

# 4. 하단 탭바: 현재 탭 알리기
for k in ['home', 'creation', 'archive', 'my']:
    rep(f'(0,c.jsxs)("button",{{className:t==="{k}"?"active":"",type:"button",',
        f'(0,c.jsxs)("button",{{className:t==="{k}"?"active":"","aria-current":t==="{k}"?"page":void 0,type:"button",', 1)

# 5. 달력 칸: "2026-10-04 감정 기록" → "10월 4일 불안 기록"
rep('"aria-label":key+(record?" 감정 기록":"")',
    '"aria-label":Number(key.slice(5,7))+"월 "+dayNumber+"일"+(record?" "+((EMOTION_TOKENS.get(record.emotion_color)||{label:"감정"}).label)+" 기록":"")', 1)


import re, os, collections
stats = collections.Counter()

# 0. 토큰 블록을 최신 design-tokens.css로 교체
tok = open(os.path.join(os.path.dirname(__file__), '..', 'design-tokens.css'), encoding='utf-8').read()
i = t.find('<style id="design-tokens">'); j = t.find('</style>', i)
assert i > 0; t = t[:i] + '<style id="design-tokens">\n' + tok + t[j:]

# ---------- 3단계: 터치 영역 44px ----------
TOUCH = """<style id="touch-targets">
/* 터치 영역 최소 44px (--size-touch-min). 보이는 크기를 키우는 요소와, 모양은 두고 누르는 영역만 넓히는 요소를 나눴다.
   기존 규칙들이 !important로 크기를 고정하고 있어 같은 우선순위로 마지막에 둔다. 캐스케이드 정리 때 각 컴포넌트 규칙으로 옮길 것. */
.home-only-page .home-only-device .app-home-sub-grid-v43>button{min-height:var(--size-touch-min)!important}
.home-only-page .home-only-device .recent-record-chips-v19>button{min-height:var(--size-touch-min)!important}
.home-only-page .home-only-device .app-home-flow-head-v43 button{min-width:var(--size-touch-min)!important;min-height:var(--size-touch-min)!important}
.home-only-page .home-only-device .calendar-month>button{min-width:var(--size-touch-min)!important;min-height:var(--size-touch-min)!important}
.home-only-page .home-only-device .app-home-v43-week-grid>button{min-width:var(--size-touch-min)!important}
/* 모양 유지, 누르는 영역만 확장 */
.home-only-page .home-only-device .onboarding-screen header button,
.home-only-page .home-only-device .my-live-toggle-v98>button{position:relative!important}
.home-only-page .home-only-device .onboarding-screen header button::after,
.home-only-page .home-only-device .my-live-toggle-v98>button::after{content:"";position:absolute;left:50%;top:50%;width:max(100%,var(--size-touch-min));height:max(100%,var(--size-touch-min));transform:translate(-50%,-50%)}
</style>
"""
assert t.count('</body>') == 1
t = t.replace('</body>', TOUCH + '</body>')

# 달력 칸·기간 탭은 크기를 정하는 원본 규칙(diary-v8-reference-calendar)의 값을 직접 토큰으로 바꾼다
rep('.archive-live-v97 .calendar-days>button{position:relative!important;display:flex!important;align-items:center!important;justify-content:center!important;align-self:center!important;justify-self:center!important;box-sizing:border-box!important;width:36px!important;max-width:100%!important;height:32px!important;min-height:32px!important;',
    '.archive-live-v97 .calendar-days>button{position:relative!important;display:flex!important;align-items:center!important;justify-content:center!important;align-self:center!important;justify-self:center!important;box-sizing:border-box!important;width:var(--size-touch-min)!important;max-width:100%!important;height:var(--size-touch-min)!important;min-height:var(--size-touch-min)!important;', 1)
rep('.archive-report-panel-v113>.archive-period-tabs button{min-height:36px!important;', '.archive-report-panel-v113>.archive-period-tabs button{min-height:var(--size-touch-min)!important;', 1)

rep('.home-only-page .archive-live-v97 .archive-cat-tabs button{\n  min-height:36px!important;', '.home-only-page .archive-live-v97 .archive-cat-tabs button{\n  min-height:var(--size-touch-min)!important;', 1)

# ---------- 4단계: 간격 · 그림자 토큰 ----------
SP = [(2,'2xs'),(4,'xs'),(8,'sm'),(12,'md'),(16,'lg'),(20,'xl'),(24,'2xl'),(32,'3xl'),(40,'4xl'),(48,'5xl')]
def sp_val(part):
    m = re.fullmatch(r'([\d.]+)px', part)
    if not m: return part
    px = float(m.group(1))
    if px < 2 or px > 48: return part
    best = min(SP, key=lambda s: (abs(s[0]-px), s[0]))   # 같은 거리면 작은 쪽
    return f'var(--spacing-{best[1]})'
def sp_token(val):
    imp = '!important' if '!important' in val else ''
    core = val.replace('!important', '').strip()
    if '(' in core: return None
    parts = core.split()
    new = [sp_val(p) for p in parts]
    if new == parts: return None
    return ' '.join(new) + imp
def L(r,g,b): return max(r,g,b)-min(r,g,b)
def sh_token(val):
    imp = '!important' if '!important' in val else ''
    core = val.replace('!important', '').strip()
    if 'inset' in core or 'var(' in core or core.count('rgba') != 1: return None
    m = re.fullmatch(r'(-?[\d.]+)(?:px)?\s+(-?[\d.]+)px\s+([\d.]+)px(?:\s+(-?[\d.]+)px)?\s+rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)', core)
    if not m: return None
    x, y, blur = float(m.group(1)), float(m.group(2)), float(m.group(3))
    r, g, b, a = int(m.group(5)), int(m.group(6)), int(m.group(7)), float(m.group(8))
    if x != 0 or y < 0 or L(r,g,b) > 40 or max(r,g,b) > 90 or a > .25: return None   # 감정색·글로우·인셋은 유지
    lvl = 'sm' if blur <= 4 else 'md' if blur <= 14 else 'lg'
    return f'var(--shadow-{lvl}){imp}'
PROPS = {p: sp_token for p in ['padding','padding-top','padding-right','padding-bottom','padding-left','padding-inline','padding-block',
                                 'margin','margin-top','margin-right','margin-bottom','margin-left','margin-inline','margin-block',
                                 'gap','row-gap','column-gap']}
PROPS['box-shadow'] = sh_token
decl = re.compile(r'(^|[{;\s])(' + '|'.join(sorted(PROPS, key=len, reverse=True)) + r')(\s*:\s*)([^;{}]+)')
def tx(css):
    def sub(m):
        r = PROPS[m.group(2)](m.group(4))
        if r is None: return m.group(0)
        stats[m.group(2).split('-')[0] if m.group(2) != 'box-shadow' else 'box-shadow'] += 1
        return m.group(1) + m.group(2) + m.group(3) + r
    return decl.sub(sub, css)
parts = []; pos = 0
for m in re.finditer(r'(<style(?![^>]*(?:design-tokens|touch-targets))[^>]*>)(.*?)(</style>)', t, re.S):
    parts.append(t[pos:m.start(2)]); parts.append(tx(m.group(2))); pos = m.end(2)
parts.append(t[pos:]); t = ''.join(parts)


# ---------- 5단계: Button 컴포넌트 (Figma Components/Button ↔ src/components/Button.tsx) ----------
P, S = 'ds-button ds-button--primary ds-button--lg', 'ds-button ds-button--secondary ds-button--lg'
for q in ['"', "'"]:
    for cls in ['home-black-button', 'home-black-button my-save-button', 'app-home-flow-next-v43', 'app-home-modal-next-v43', 'app-home-save-v43']:
        old = f'className:{q}{cls}{q}'
        n = t.count(old)
        if n: t = t.replace(old, f'className:{q}{P} {cls}{q}'); stats['button:' + cls.split()[0]] += n
rep("h('div',{className:'app-home-modal-split-v43'},h('button',{type:'button',onClick:function(){setStep(1)}},'이전'),h('button',{type:'button',onClick:next},'다음'))",
    "h('div',{className:'app-home-modal-split-v43'},h('button',{type:'button',className:'" + S + "',onClick:function(){setStep(1)}},'이전'),h('button',{type:'button',className:'" + P + "',onClick:next},'다음'))", 2)
BUTTON = '''<style id="component-button">
/* Button — Figma: Components/Button (Style=Primary|Secondary × Size=Large|Medium × State=Default|Disabled)
   코드 기준: src/components/Button.tsx. 화면별로 흩어진 버튼 클래스(home-black-button, app-home-*-v43 …)는 이 규칙을 따른다.
   기존 버전별 규칙이 !important로 크기를 지정하고 있어 html body 범위로 둔다. 캐스케이드 정리 후 범위를 낮출 것. */
html body .home-only-page .home-only-device .ds-button{display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:var(--spacing-xs)!important;box-sizing:border-box!important;border-width:1px!important;border-style:solid!important;font-family:inherit!important;font-weight:var(--font-weight-bold)!important;line-height:1.5!important;letter-spacing:0!important;box-shadow:none!important;cursor:pointer}
html body .home-only-page .home-only-device .ds-button.ds-button--lg{height:var(--size-button-lg)!important;min-height:var(--size-button-lg)!important;padding:0 var(--spacing-2xl)!important;border-radius:var(--radius-xl)!important;font-size:var(--font-size-body-md)!important}
html body .home-only-page .home-only-device .ds-button.ds-button--md{height:var(--size-button-md)!important;min-height:var(--size-button-md)!important;padding:0 var(--spacing-lg)!important;border-radius:var(--radius-lg)!important;font-size:var(--font-size-body-sm)!important}
html body .home-only-page .home-only-device .ds-button.ds-button--primary{background:var(--color-action-primary)!important;border-color:var(--color-action-primary)!important;color:var(--color-text-inverse)!important}
html body .home-only-page .home-only-device .ds-button.ds-button--secondary{background:var(--color-bg-surface)!important;border-color:var(--color-border-default)!important;color:var(--color-text-primary)!important}
html body .home-only-page .home-only-device .ds-button:disabled{background:var(--color-bg-subtle)!important;border-color:var(--color-bg-subtle)!important;color:var(--color-text-disabled)!important;cursor:default}
</style>
'''
t = t.replace('<style id="touch-targets">', BUTTON + '<style id="touch-targets">')

open(OUT, 'w', encoding='utf-8').write(t)
for k, v in sorted(stats.items()): print(f'{v:6} {k}')
print('ok')
