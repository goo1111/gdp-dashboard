// 감정로그 포트폴리오 PDF 내보내기 — PPT 기본 크기(와이드 16:9, 13.333 × 7.5 in)로 한 장씩
// Usage: python3 tools/build.py <version> <out_dir> --pdf  (장별 문서를 <out_dir>/pdf-pages/ 에 씀)
//        node tools/export_pdf.js <out_dir>/pdf-pages <out.pdf>
// 1440×810 장을 0.8889배로 인쇄해 13.333 × 7.5 in 한 페이지에 정확히 맞춰요. 움직이는 이미지는 pdf-stills.json의 정지 프레임으로 바뀌어 있어요.
const {execFileSync} = require('child_process');
const fs = require('fs'), path = require('path');
const {chromium} = require(execFileSync('npm', ['root', '-g']).toString().trim() + '/playwright');
(async () => {
  const [dir, out] = process.argv.slice(2);
  const files = fs.readdirSync(dir).filter(f => /^\d+\.html$/.test(f)).sort();
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1440, height: 810}});
  await p.route(/^https?:/, r => r.abort());
  const parts = [];
  for (const f of files) {
    await p.goto('file://' + path.resolve(dir, f));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    const part = path.resolve(dir, f.replace('.html', '.pdf'));
    await p.pdf({path: part, width: '13.333in', height: '7.5in', scale: 13.333 / 15, printBackground: true,
                 margin: {top: 0, right: 0, bottom: 0, left: 0}, pageRanges: '1'});
    parts.push(part);
  }
  await b.close();
  execFileSync('pdfunite', [...parts, path.resolve(out)]);
  console.log(out, parts.length, 'pages');
})();
