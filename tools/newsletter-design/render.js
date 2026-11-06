// Usage: NODE_PATH=/opt/node22/lib/node_modules node render.js jobs.json
// jobs.json: [{"html":"/abs/in.html","out":"/abs/out.png","w":1200,"h":628,"scale":1,"type":"png"|"jpeg"}]
const {chromium}=require('playwright');
(async()=>{
  const jobs=JSON.parse(require('fs').readFileSync(process.argv[2],'utf8'));
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  for(const j of jobs){
    const p=await b.newPage({viewport:{width:j.w,height:j.h},deviceScaleFactor:j.scale||1});
    await p.goto('file://'+j.html);
    const [sw,sh]=await p.evaluate(()=>[document.documentElement.scrollWidth,document.documentElement.scrollHeight]);
    if(sw>j.w||sh>j.h) console.log('WARNING: '+j.html+' overflows '+sw+'x'+sh+' (canvas '+j.w+'x'+j.h+')');
    const o={path:j.out,type:j.type||'png'}; if(o.type==='jpeg') o.quality=95;
    await p.screenshot(o); await p.close();
  }
  await b.close();
})();
