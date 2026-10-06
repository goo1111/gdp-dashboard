const {chromium}=require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
(async()=>{const [dir,out]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:810}});await p.route(/^https?:/,r=>r.abort());
for(let i=1;i<=13;i++){await p.goto('file://'+dir+'/s'+String(i).padStart(2,'0')+'.html');await p.waitForTimeout(400);
 await p.evaluate(()=>{const S=document.querySelector('.slide');const g=document.createElement('div');g.style.cssText='position:absolute;inset:0;pointer-events:none;z-index:9999';
  const line=(css)=>{const d=document.createElement('div');d.style.cssText='position:absolute;'+css;g.appendChild(d)};
  for(const x of [88,1352])line(`left:${x}px;top:0;bottom:0;width:0;border-left:2px dashed rgba(255,0,80,.7)`);
  for(const [y,c] of [[204,'0,140,255'],[686,'0,140,255'],[710,'255,140,0'],[766,'255,140,0']])line(`top:${y}px;left:0;right:0;height:0;border-top:2px dashed rgba(${c},.8)`);
  S.appendChild(g)});
 await p.screenshot({path:`${out}/g${String(i).padStart(2,'0')}.png`})}
await b.close()})();
