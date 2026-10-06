// 빌드된 포트폴리오의 모든 프레임이 열리고 장 제목이 순서대로 나오는지 확인: node tools/check_frames.js <portfolio.html>
const {chromium}=require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
(async()=>{const f=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:950}});await p.route(/^https?:/,r=>r.abort());
await p.goto('file://'+f);await p.waitForTimeout(1500);const fr=p.locator('.frame iframe');const n=await fr.count();console.log('iframes',n,'sections',await p.locator('section.s').count());
for(let i=0;i<n;i++){await fr.nth(i).scrollIntoViewIfNeeded();await p.waitForTimeout(250);const h=await fr.nth(i).contentFrame().locator('h1').first().innerText().catch(e=>'ERR');console.log(i+1,(await fr.nth(i).getAttribute('title')),'|',h.replace(/\n/g,' ').slice(0,40))}
await b.close()})();
