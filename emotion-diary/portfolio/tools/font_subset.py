"""Pretendard 부분 글꼴 만들기 / 검사

모든 장(src/slides/*.html)에 쓰인 글자 + 기본 문장부호를 담은 부분 글꼴을 src/fonts/pretendard-subset.css로 만들어요.
문구를 고친 뒤에는 다시 실행하세요. 빠진 글자가 있으면 그 글자는 다른 글꼴로 그려져요.

Usage:
  python3 tools/font_subset.py build <PretendardVariable.ttf>   # npm pack pretendard 의 dist/public/variable/
  python3 tools/font_subset.py check                            # 빠진 글자 검사 (lint에서도 호출)
"""
import base64, html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
OUT = os.path.join(SRC, 'fonts', 'pretendard-subset.css')
EXTRA = ''.join(chr(c) for c in range(0x20, 0x7f)) + '·•…→←↑↓↔↕‘’“”–—×%°~₩·「」『』《》〈〉①②③④⑤▶▷►✓'


def used_chars():
    chars = set(EXTRA)
    for fn in sorted(os.listdir(os.path.join(SRC, 'slides'))):
        s = open(os.path.join(SRC, 'slides', fn)).read()
        for m in re.findall(r'content:\s*"([^"]*)"', s):
            chars.update(m)
        body = re.sub(r'<style.*?</style>|<title>.*?</title>|<!--.*?-->', '', s, flags=re.S)
        body = re.sub(r'<[^>]+>', ' ', body)
        chars.update(html.unescape(body))
    return {c for c in chars if c.isprintable() and not c.isspace()} | {' '}


def font_cmap():
    from fontTools.ttLib import TTFont
    css = open(OUT).read()
    b64 = re.search(r'base64,([A-Za-z0-9+/=]+)', css).group(1)
    return set(TTFont(io.BytesIO(base64.b64decode(b64))).getBestCmap())


def check():
    missing = sorted(c for c in used_chars() if ord(c) not in font_cmap())
    print(f'font check: {len(missing)} missing', ''.join(missing))
    return missing


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'build':
        from fontTools import subset
        chars = ''.join(sorted(used_chars()))
        opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.name_IDs = ['*']
        font = subset.load_font(sys.argv[2], opts)
        sub = subset.Subsetter(opts); sub.populate(text=chars); sub.subset(font)
        buf = io.BytesIO(); subset.save_font(font, buf, opts)
        data = base64.b64encode(buf.getvalue()).decode()
        open(OUT, 'w').write('@font-face{font-family:"Pretendard Variable";font-weight:45 920;font-style:normal;'
                             f'font-display:block;src:url(data:font/woff2;base64,{data}) format("woff2")}}')
        man_p = os.path.join(SRC, 'manifest.json'); man = json.load(open(man_p))
        for m in man:
            m['font'] = 'pretendard-subset.css'
        json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
        print(OUT, len(chars), 'chars', len(buf.getvalue()) // 1024, 'KB')
        sys.exit(1 if check() else 0)
    elif cmd == 'check':
        sys.exit(1 if check() else 0)
