"""감정로그 포트폴리오 빌드: src/ -> 감정로그_포트폴리오_<version>.html

Usage: python3 tools/build.py <version> [out_dir] [--pdf]

--pdf: PDF용 장별 문서를 <out_dir>/pdf-pages/NN.html로도 써요(움직이는 이미지 -> 정지 프레임,
       화면 맞춤 스크립트 없음). 이어서 node tools/export_pdf.js 로 PPT 기본 크기 PDF를 만들어요.

- 모든 장은 src/pf-ds.css(토큰 + 공통 요소)를 참조해요.
- src/slides/NN.html: 장별 <title>, <style>, <section class="slide">.
- src/assets/: 'asset:<name>'으로 참조하는 이미지. 빌드할 때 data URI로 넣어요.
"""
import base64, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
args = [a for a in sys.argv[1:] if not a.startswith('--')]
PDF = '--pdf' in sys.argv
version = args[0]
out_dir = args[1] if len(args) > 1 else ROOT
STILLS = json.load(open(os.path.join(SRC, 'pdf-stills.json')))['stills']

MIME = {'jpg': 'image/jpeg', 'png': 'image/png', 'webp': 'image/webp', 'svg': 'image/svg+xml'}
FIT = ("<script>\nfunction fit(){const s=Math.min(innerWidth/1440,innerHeight/810),x=(innerWidth-1440*s)/2,"
       "y=(innerHeight-810*s)/2;document.getElementById('wrap').style.transform=`translate(${x}px,${y}px) scale(${s})`}\n"
       "addEventListener('resize',fit);fit();\n</script>")

ds_css = open(os.path.join(SRC, 'pf-ds.css')).read()
manifest = json.load(open(os.path.join(SRC, 'manifest.json')))
shell = open(os.path.join(SRC, 'shell.html')).read()


def inline_assets(s):
    def r(m):
        name = m.group(1)
        raw = open(os.path.join(SRC, 'assets', name), 'rb').read()
        return f"data:{MIME[name.rsplit('.', 1)[1]]};base64,{base64.b64encode(raw).decode()}"
    return re.sub(r'asset:([0-9a-f]{12}\.[a-z]+)', r, s)


def slide_doc(path, font, pdf=False):
    font_css = open(os.path.join(SRC, 'fonts', font)).read()
    s = open(path).read()
    title = re.search(r'<title>(.*?)</title>', s).group(1)
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    sec = re.search(r'<section class="slide">.*</section>', s, re.S).group(0)
    doc = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
           f'<title>{title}</title>\n<style id="embedded-pretendard">{font_css}</style>\n'
           f'<style id="pf-ds">{ds_css}</style>\n<style id="slide">{css}</style>\n</head>\n<body>\n'
           f'<div id="wrap">\n{sec}\n</div>\n{"" if pdf else FIT}\n</body>\n</html>')
    if pdf:
        for a, still in STILLS.items():
            doc = doc.replace('asset:' + a, 'asset:' + still)
        doc = doc.replace('</head>', '<style>@page{size:13.333in 7.5in;margin:0}html,body{width:1440px;height:810px;overflow:hidden}</style>\n</head>')
    return inline_assets(doc)


sections = []
for m in manifest:
    doc = slide_doc(os.path.join(SRC, 'slides', m['file']), m['font'])
    sections.append(f'<section class="s"><div class="lbl">{m["label"]}</div><div class="frame">'
                    f'<iframe srcdoc="{html.escape(doc, quote=True)}" loading="lazy" title="{html.escape(m["label"])}"></iframe></div></section>')
toc = ' · '.join(m['label'] for m in manifest)
header = (f'<h1>감정로그 포트폴리오 <span style="font-size:14px;color:var(--ink3);font-weight:600">{version}</span></h1>'
          f'<p>{toc}</p>')
out = (shell.replace('{{SECTIONS}}', ''.join(sections)).replace('{{TITLE}}', f'감정로그 포트폴리오 {version}')
       .replace('{{HEADER}}', header))
# 프레임이 장 수만큼 온전히 닫혔는지 확인 (태그가 깨지면 일부 장이 사라져요)
assert out.count('<iframe srcdoc="') == out.count('"></iframe></div></section>') == len(manifest), 'broken iframe markup'
path = os.path.join(out_dir, f'감정로그_포트폴리오_{version}.html')
open(path, 'w').write(out)
print(path, len(manifest), 'slides', round(len(out) / 1e6, 2), 'MB')
if PDF:
    pdir = os.path.join(out_dir, 'pdf-pages')
    os.makedirs(pdir, exist_ok=True)
    for old in os.listdir(pdir):  # 지난 빌드의 장 파일이 남으면 PDF에 섞여 들어가요
        if re.match(r'^\d+\.(html|pdf)$', old):
            os.remove(os.path.join(pdir, old))
    for m in manifest:
        open(os.path.join(pdir, m['file']), 'w').write(slide_doc(os.path.join(SRC, 'slides', m['file']), m['font'], pdf=True))
    print(pdir, len(manifest), 'pdf pages')
