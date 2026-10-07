const {chromium}=require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/guide.html');await p.waitForTimeout(800);
 const over=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((pg,i)=>{const foot=pg.querySelector('.foot').getBoundingClientRect().top;let max=0;[...pg.children].forEach(c=>{if(!c.classList.contains('foot'))max=Math.max(max,c.getBoundingClientRect().bottom)});return {page:i+1,overflow:Math.round(max-(foot-10))}}));
 console.log('overflow',JSON.stringify(over.filter(o=>o.overflow>0)), 'font NG loaded', await p.evaluate(async()=>{await document.fonts.ready;return [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight)}));
 await p.pdf({path:'guide.pdf',width:'8.5in',height:'11in',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});await b.close()})();
