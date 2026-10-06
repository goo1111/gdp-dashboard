"""포트폴리오 디자인 시스템 검사: src/slides/*.html이 토큰만 쓰는지 확인해요.

Usage: python3 tools/lint.py

규칙
- font-size는 var(--pf-fs-*)만 (px 직접 쓰기 금지)
- 색은 var(--pf-*) 또는 데이터 색(앱 감정색 · 앱 중립색 · 차트 표시색)만
- border-radius는 var(--pf-r-*), 50%, 0만. 예외: 'pf-lint: app-examples' 표시가 있는 장(디자인 시스템)의 앱 컴포넌트 예시(클래스 · 인라인, 앱의 실제 값을 보여 줌)
- box-shadow의 카드 그림자는 var(--pf-shadow-*)
- 카드(모서리 var(--pf-r-lg))의 안쪽 여백은 var(--pf-pad-card)
- 모든 글자가 src/fonts/pretendard-subset.css에 들어 있어야 함 (없으면 다른 글꼴로 그려짐)
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'slides')
DATA = set('''#f05a8a #8bd0bd #f7bd4e #d19cdb #80a9dc #dfa292 #9ca9b1 #e66f5c
#fff1f5 #eaf8f3 #fff4d4 #f8ecfb #eaf3fc #ffede8 #eef2f4 #ffeae6
#d93d6a #55aa92 #d99400 #a96abb #5689c1 #bd6552 #718089 #c8493d
#972047 #347565 #8c5d00 #744789 #426d9e #954b3e #59666e #a23b32
#2b2733 #1c1a18 #6f6964 #5f5a56 #e4dfda #dedbd8 #a39b95 #f3f0eb #faf9f4 #f1f0f3 #fbfaf7 #fff5f2 #ffd9cf #f6a395
#ee9f8d #6fc3a6 #eeb35a #f3bcad #acdccb'''.split())
APP_EXAMPLE = re.compile(r'\.(bt|ch|dc|tg|nv|sg2|ul|rc2|lr|hd|ei|hero|wk|sheet|prop|sz|fh|row|mrow|crow|cts|dcs|bgrid|ins|dots|es|nstrip|ec|er|nc|rc|sc|hc|rg|sg|hg|flow|sem|tr|mh|mw|m|tlbl)\b')


def decls(s):
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', s):
        yield m.group(1).strip(), m.group(2)
    for m in re.finditer(r'style="([^"]*)"', s):
        yield 'inline', m.group(1)


errors = []
for fn in sorted(os.listdir(SRC)):
    s = open(os.path.join(SRC, fn)).read()
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)  # inline icons keep their own fills
    app_examples = 'pf-lint: app-examples' in s  # 앱 컴포넌트 예시가 있는 장(디자인 시스템)
    for sel, body in decls(s):
        for prop, val in re.findall(r'([a-z-]+)\s*:\s*([^;]+)', body):
            if prop == 'font-size' and re.search(r'\d+(\.\d+)?px', val):
                errors.append(f'{fn} {sel[:40]} font-size:{val.strip()}')
            for h in re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', val):
                if h.lower() not in DATA:
                    errors.append(f'{fn} {sel[:40]} {prop}:{h}')
            if prop == 'padding' and 'var(--pf-r-lg)' in body and re.search(r'(1[89]|[2-9]\d)px', val):
                errors.append(f'{fn} {sel[:40]} card padding:{val.strip()} -> var(--pf-pad-card)')
            if prop == 'border-radius' and re.search(r'\d+px', val):
                if not (app_examples and (sel == 'inline' or APP_EXAMPLE.search(sel))):
                    errors.append(f'{fn} {sel[:40]} border-radius:{val.strip()}')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import font_subset
for c in font_subset.check():
    errors.append(f'font: "{c}" (U+{ord(c):04X}) not in pretendard-subset.css -> python3 tools/font_subset.py build <ttf>')
for e in errors:
    print(e)
print(f'{len(errors)} violation(s)')
sys.exit(1 if errors else 0)
