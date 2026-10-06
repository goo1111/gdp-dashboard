const {chromium}=require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
const fs=require('fs');
(async()=>{const [proto,out]=process.argv.slice(2);const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2});const p=await ctx.newPage();await p.route(/jsdelivr/,r=>r.abort());
 await p.clock.setFixedTime(new Date('2026-09-30T10:00:00'));await p.goto('file://'+proto);await p.waitForTimeout(1200);
 const dev=p.locator('.home-only-device');let n=0,dir='',dur=[];
 const dot=(x,y,press)=>p.evaluate(([x,y,press])=>{let d=document.getElementById('tdot');if(!d){d=document.createElement('div');d.id='tdot';document.body.appendChild(d)}
   if(x==null){d.style.display='none';return}
   Object.assign(d.style,{display:'block',position:'fixed',left:(x-22)+'px',top:(y-22)+'px',width:'44px',height:'44px',borderRadius:'50%',zIndex:99999,pointerEvents:'none',
    background:press?'rgba(43,39,51,.38)':'rgba(43,39,51,.22)',boxShadow:'0 0 0 3px rgba(255,255,255,.9)',transform:press?'scale(.82)':'scale(1)'})},[x,y,press]);
 const shot=async(ms)=>{n++;await dev.screenshot({path:`${out}/${dir}/${String(n).padStart(3,'0')}.png`,animations:'disabled'});dur.push(ms)};
 const ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
 let cur=null;
 const tap=async(x,y,hold)=>{
   if(cur){for(let i=1;i<=6;i++){const t=ease(i/6);await dot(cur[0]+(x-cur[0])*t,cur[1]+(y-cur[1])*t,false);await shot(60)}}else{await dot(x,y,false);await shot(300)}
   await dot(x,y,true);await shot(120);await p.mouse.click(x,y);await p.waitForTimeout(120);await dot(x,y,false);
   for(let i=0;i<3;i++){await p.waitForTimeout(110);await shot(110)}
   await shot(hold);cur=[x,y]};
 await p.getByText('건너뛰기').click();await p.waitForTimeout(400);
 // ---- A: compass
 dir='f07';n=0;dur=[];await p.getByText('기록하기').first().click();await p.waitForTimeout(700);
 const cb=await p.locator('.app-home-compass-v43').first().boundingBox();
 await dot(null);await shot(700);
 let first=true;for(const [x,y] of [[.2,.22],[.8,.22],[.25,.78],[.62,.4]]){if(!first){await p.keyboard.press('Escape');await p.waitForTimeout(250);await shot(200)}first=false;await tap(cb.x+cb.width*x,cb.y+cb.height*y,1100);
   console.log('sel',await p.evaluate(()=>{const s=document.querySelector('.app-home-main-grid-v43 .selected');return s&&s.textContent}))}
 await dot(null);await shot(400);fs.writeFileSync(`${out}/f07/dur.json`,JSON.stringify(dur));
 // continue to the creation result
 await p.locator('.app-home-modal-next-v43').click();await p.waitForTimeout(500);
 await p.locator('.app-home-sub-grid-v43 button').first().click();
 await p.getByRole('button',{name:'다음',exact:true}).last().click();await p.waitForTimeout(500);
 await p.getByRole('textbox',{name:'오늘의 한 문장'}).fill('오랜만에 친구를 만나 설렜다.');
 await p.getByRole('button',{name:'저장하기',exact:true}).click();await p.waitForTimeout(600);
 await p.locator('nav button').filter({hasText:'창작소'}).click();await p.waitForTimeout(500);
 await p.getByText('한 장의 그림으로').click();await p.waitForTimeout(400);
 await p.getByRole('button',{name:'다음',exact:true}).last().click();await p.waitForTimeout(400);
 await p.getByRole('button',{name:'이 재료로 만들기'}).click();await p.waitForTimeout(1500);
 if(await p.getByRole('button',{name:'결과 바로 보기'}).count())await p.getByRole('button',{name:'결과 바로 보기'}).click();
 await p.waitForTimeout(800);
 // ---- B: style switch
 dir='f09';n=0;dur=[];cur=null;await dot(null);await shot(900);
 const btn=async name=>{const bb=await p.getByRole('button',{name}).boundingBox();return [bb.x+bb.width/2,bb.y+bb.height/2]};
 for(const name of ['컬러 라인 포스터','그림일기']){const [x,y]=await btn(name);await tap(x,y,1500)}
 await dot(null);await shot(300);fs.writeFileSync(`${out}/f09/dur.json`,JSON.stringify(dur));
 console.log('frames',fs.readdirSync(out+'/f07').length,fs.readdirSync(out+'/f09').length);await b.close()})();
