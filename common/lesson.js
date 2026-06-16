/* ══════════════════════════════════════════════════════════
   Olivia's Math Lessons — Shared Runtime + Simulation Library
   Linked by every generated lesson. Plain ES5, no build step.
   ──────────────────────────────────────────────────────────
   Globals exposed:
     mj()                 re-typeset MathJax safely
     rev(id)              toggle a .reveal block + re-typeset
     hidpi(canvas)        retina-scale a canvas, returns 2d ctx
                          (also sets canvas._w / canvas._h in CSS px)
     C2                   muted grey '#94a3b8'
     GP.monteCarlo(opts)  area-probability scatter simulation
     GP.numberLine(opts)  1-D length-probability draggable point
     GP.squareDrag(opts)  2-D draggable point in the unit square
   See README.md in /tools for authoring details.
   ══════════════════════════════════════════════════════════ */

/* MathJax delimiters — set before the CDN script loads. */
window.MathJax = window.MathJax || {
  tex:{ inlineMath:[['\\(','\\)']], displayMath:[['\\[','\\]']] },
  svg:{ fontCache:'global' }
};

/* ── twinkling starfield ── */
(function(){
  function start(){
    var sc=document.getElementById('stars'); if(!sc) return;
    var x=sc.getContext('2d'), st=[];
    function init(){sc.width=innerWidth;sc.height=innerHeight;
      st=Array.from({length:160},function(){return{x:Math.random()*sc.width,y:Math.random()*sc.height,
        r:Math.random()*1.3+0.3,a:Math.random(),da:(Math.random()-0.5)*0.006};});}
    function draw(){x.clearRect(0,0,sc.width,sc.height);
      st.forEach(function(s){s.a=Math.max(0.1,Math.min(1,s.a+s.da));if(s.a<=0.1||s.a>=1)s.da*=-1;
        x.beginPath();x.arc(s.x,s.y,s.r,0,6.283);x.fillStyle='rgba(255,255,255,'+s.a+')';x.fill();});
      requestAnimationFrame(draw);}
    init();draw();addEventListener('resize',init);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
})();

/* ── helpers ── */
function mj(){if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise();}
function rev(id){var e=document.getElementById(id);if(e){e.classList.toggle('show');mj();}}
function hidpi(cv){var d=window.devicePixelRatio||1,c=cv.getContext('2d');var w=cv.width,h=cv.height;
  cv.style.width=w+'px';cv.style.height=h+'px';cv.width=w*d;cv.height=h*d;c.scale(d,d);cv._w=w;cv._h=h;return c;}
var C2='#94a3b8';

/* ── generic multiple-choice concept questions ──
   Markup:  <div class="choices" data-quiz>
              <button class="choice" data-correct>A</button>
              <button class="choice">B</button> ... </div>          */
(function(){
  function wire(){
    document.querySelectorAll('.choices[data-quiz]').forEach(function(box){
      box.querySelectorAll('.choice').forEach(function(ch){
        ch.addEventListener('click',function(){
          if(box.querySelector('.choice.correct'))return;            // already answered
          box.querySelectorAll('.choice').forEach(function(c){
            if(c.hasAttribute('data-correct'))c.classList.add('correct');
          });
          if(!ch.hasAttribute('data-correct'))ch.classList.add('wrong');
          mj();
        });
      });
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',wire);else wire();
})();

/* ══════════════════════════════════════════════════════════
   GP — Geometric-Probability simulation toolkit
   ══════════════════════════════════════════════════════════ */
var GP=(function(){

  function el(id){return document.getElementById(id);}

  /* Map the unit square [0,1]^2 onto a canvas with padding. */
  function squareMap(W,H,pad){
    pad=pad||34; var sz=Math.min(W,H)-2*pad;
    return {pad:pad, sz:sz,
      X:function(v){return pad+v*sz;},
      Y:function(v){return (Math.min(W,H)-pad)-v*sz;}};
  }

  /* ── Monte-Carlo area probability ──
     opts:
       canvas    (id, required)            target canvas
       test(x,y) -> bool  (required)       success predicate on [0,1]^2
       readout   (id)                      element to print convergence
       button    (id)                      "run" button; if absent runs on load
       trials    (number, default 3000)
       target    (string)                  e.g. "1/4 = 0.25" shown as goal
       drawRegion(ctx,M)                   optional: fill the favorable region
       axisX, axisY (strings)              optional axis captions
       sampler() -> [x,y]                  optional custom sampler (default uniform) */
  function monteCarlo(opts){
    var cv=el(opts.canvas); if(!cv) return;
    var ctx=hidpi(cv),W=cv._w,H=cv._h,M=squareMap(W,H,opts.pad);
    var trials=opts.trials||3000, sampler=opts.sampler||function(){return [Math.random(),Math.random()];};
    var pts=[],good=0,n=0,running=false;

    function frame(){
      ctx.clearRect(0,0,W,H);
      if(opts.drawRegion){ctx.save();ctx.fillStyle='rgba(34,197,94,0.20)';opts.drawRegion(ctx,M);ctx.restore();}
      pts.forEach(function(p){ctx.fillStyle=p.g?'rgba(34,197,94,0.85)':'rgba(239,68,68,0.40)';
        ctx.beginPath();ctx.arc(M.X(p.x),M.Y(p.y),2,0,6.283);ctx.fill();});
      ctx.strokeStyle='#3b82f6';ctx.lineWidth=2;ctx.strokeRect(M.X(0),M.Y(1),M.sz,M.sz);
      ctx.fillStyle=C2;ctx.font='11px system-ui';ctx.textAlign='center';
      if(opts.axisX)ctx.fillText(opts.axisX,M.X(0.5),H-8);
      if(opts.axisY){ctx.save();ctx.translate(12,M.Y(0.5));ctx.rotate(-Math.PI/2);ctx.fillText(opts.axisY,0,0);ctx.restore();}
    }
    function print(){if(!opts.readout)return;
      var pr=n?(good/n).toFixed(3):'—';
      el(opts.readout).innerHTML='Trials: <b>'+n+'</b> — empirical \\(P=\\) <b>'+pr+'</b>'+
        (opts.target?' (target '+opts.target+')':'');
      mj();}
    function run(){
      if(running)return; running=true; pts=[];good=0;n=0;
      (function add(){
        for(var i=0;i<60&&n<trials;i++){var s=sampler(),g=!!opts.test(s[0],s[1]);
          pts.push({x:s[0],y:s[1],g:g});n++;if(g)good++;}
        frame();print();
        if(n<trials)requestAnimationFrame(add);else running=false;
      })();
    }
    frame();
    if(opts.button&&el(opts.button))el(opts.button).onclick=run; else run();
    return {run:run};
  }

  /* ── 1-D length probability: draggable point on a segment ──
     opts:
       canvas (id), readout (id)
       min,max          segment ends (default 0..1)
       start            initial value (default midpoint)
       success(t)->bool predicate; the green sub-region(s)
       regions          array of [lo,hi] to shade green (the success set)
       label(t)->string optional custom readout text
       prob             string shown as the exact answer (e.g. "1/2") */
  function numberLine(opts){
    var cv=el(opts.canvas); if(!cv) return;
    var ctx=hidpi(cv),W=cv._w,H=cv._h;
    var a=(opts.min!=null?opts.min:0), b=(opts.max!=null?opts.max:1);
    var t=(opts.start!=null?opts.start:(a+b)/2), drag=false;
    var x0=46,x1=W-46,y=H/2,L=x1-x0;
    function px(v){return x0+(v-a)/(b-a)*L;}
    function draw(){
      ctx.clearRect(0,0,W,H);
      // success regions
      (opts.regions||[]).forEach(function(r){ctx.strokeStyle='rgba(34,197,94,0.5)';ctx.lineWidth=14;ctx.lineCap='butt';
        ctx.beginPath();ctx.moveTo(px(r[0]),y);ctx.lineTo(px(r[1]),y);ctx.stroke();});
      ctx.strokeStyle='#1e3a5f';ctx.lineWidth=4;ctx.lineCap='round';
      ctx.beginPath();ctx.moveTo(x0,y);ctx.lineTo(x1,y);ctx.stroke();
      ctx.fillStyle=C2;ctx.font='12px system-ui';ctx.textAlign='center';
      ctx.fillText(''+a,x0,y+28);ctx.fillText(''+b,x1,y+28);
      var ok=opts.success?!!opts.success(t):false;
      ctx.fillStyle=ok?'#22c55e':'#ef4444';ctx.beginPath();ctx.arc(px(t),y,8,0,6.283);ctx.fill();
      ctx.strokeStyle='#050a18';ctx.lineWidth=2;ctx.stroke();
      if(opts.readout){
        var txt=opts.label?opts.label(t):('value = <b>'+t.toFixed(2)+'</b> → '+
          (ok?'<span style="color:#86efac;font-weight:700;">success ✓</span>'
             :'<span style="color:#fca5a5;font-weight:700;">fail ✗</span>'))+
          (opts.prob?' &nbsp; \\(P=\\) <b>'+opts.prob+'</b>':'');
        el(opts.readout).innerHTML=txt;mj();
      }
    }
    function set(mx){t=Math.max(a,Math.min(b,a+(mx-x0)/L*(b-a)));draw();}
    function mp(e){var r=cv.getBoundingClientRect();return (e.touches?e.touches[0].clientX:e.clientX)-r.left;}
    cv.addEventListener('mousedown',function(e){drag=true;set(mp(e));});
    addEventListener('mousemove',function(e){if(drag)set(mp(e));});
    addEventListener('mouseup',function(){drag=false;});
    cv.addEventListener('touchstart',function(e){drag=true;set(mp(e));e.preventDefault();},{passive:false});
    cv.addEventListener('touchmove',function(e){if(drag){set(mp(e));e.preventDefault();}},{passive:false});
    draw();
    return {draw:draw};
  }

  /* ── 2-D draggable point in the unit square ──
     opts: canvas, readout, test(x,y)->bool, drawRegion(ctx,M),
           start ([x,y] default [0.5,0.5]), axisX, axisY            */
  function squareDrag(opts){
    var cv=el(opts.canvas); if(!cv) return;
    var ctx=hidpi(cv),W=cv._w,H=cv._h,M=squareMap(W,H,opts.pad);
    var p=opts.start||[0.5,0.5], drag=false;
    function draw(){
      ctx.clearRect(0,0,W,H);
      if(opts.drawRegion){ctx.save();ctx.fillStyle='rgba(34,197,94,0.20)';opts.drawRegion(ctx,M);ctx.restore();}
      ctx.strokeStyle='#3b82f6';ctx.lineWidth=2;ctx.strokeRect(M.X(0),M.Y(1),M.sz,M.sz);
      ctx.fillStyle=C2;ctx.font='11px system-ui';ctx.textAlign='center';
      if(opts.axisX)ctx.fillText(opts.axisX,M.X(0.5),H-8);
      if(opts.axisY){ctx.save();ctx.translate(12,M.Y(0.5));ctx.rotate(-Math.PI/2);ctx.fillText(opts.axisY,0,0);ctx.restore();}
      var ok=opts.test?!!opts.test(p[0],p[1]):false;
      ctx.fillStyle=ok?'#22c55e':'#ef4444';ctx.beginPath();ctx.arc(M.X(p[0]),M.Y(p[1]),7,0,6.283);ctx.fill();
      ctx.strokeStyle='#fff';ctx.lineWidth=2;ctx.stroke();
      if(opts.readout){el(opts.readout).innerHTML='('+p[0].toFixed(2)+', '+p[1].toFixed(2)+') → '+
        (ok?'<span style="color:#86efac;font-weight:700;">inside ✓</span>'
           :'<span style="color:#fca5a5;font-weight:700;">outside ✗</span>');}
    }
    function set(mx,my){p=[Math.max(0,Math.min(1,(mx-M.pad)/M.sz)),
                          Math.max(0,Math.min(1,((Math.min(W,H)-M.pad)-my)/M.sz))];draw();}
    function mp(e){var r=cv.getBoundingClientRect();var c=e.touches?e.touches[0]:e;return [c.clientX-r.left,c.clientY-r.top];}
    cv.addEventListener('mousedown',function(e){drag=true;var m=mp(e);set(m[0],m[1]);});
    addEventListener('mousemove',function(e){if(drag){var m=mp(e);set(m[0],m[1]);}});
    addEventListener('mouseup',function(){drag=false;});
    cv.addEventListener('touchstart',function(e){drag=true;var m=mp(e);set(m[0],m[1]);e.preventDefault();},{passive:false});
    cv.addEventListener('touchmove',function(e){if(drag){var m=mp(e);set(m[0],m[1]);e.preventDefault();}},{passive:false});
    draw();
    return {draw:draw};
  }

  /* Run a list of sim factory calls once the DOM is ready. */
  function ready(fn){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',fn);else fn();}

  return {monteCarlo:monteCarlo, numberLine:numberLine, squareDrag:squareDrag, squareMap:squareMap, ready:ready};
})();
