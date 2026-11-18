/* ===== Oberfläche: Start, Üben, Spielwiese, Spickzettel, Eltern-Bereich ===== */
'use strict';
let USER=null,SES=null,CUR=null;
const setView=h=>{$('#app').innerHTML=h;window.scrollTo(0,0);};
const bar=p=>`<div class="bar"><i style="width:${Math.round(p*100)}%"></i></div>`;
const dots=n=>'●'.repeat(n)+'○'.repeat(3-n);
const norm=s=>String(s||'').replace(/\r/g,'').split('\n').map(l=>l.replace(/\s+$/,'')).join('\n').replace(/^\n+|\n+$/g,'');
function md(s){
  return String(s||'').split(/```\n?/).map((p,i)=>i%2?`<pre class="blk">${esc(p.replace(/\n$/,''))}</pre>`:esc(p).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\n/g,'<br>')).join('');
}
const codeBlock=c=>`<pre class="code">${esc(c).split('\n').map((l,i)=>`<span class="ln">${i+1}</span>${l}`).join('\n')}</pre>`;
function pyStatus(){pyStart().then(ok=>{const el=$('#pystat');if(el)el.textContent=ok?'Python bereit ✓':'Python konnte nicht geladen werden – bitte Seite neu laden.';});}
function header(u,back){
  return `<div class="top"><span class="logo eltern-hit" data-act="parents">🐍</span><div class="ttl">Python-Trainer <small>Programmieren lernen</small></div>${u?`<button class="who" data-act="switch">${esc(u.avatar)} ${esc(u.name)}</button>`:''}</div>${back?`<button class="back" data-act="${back}">‹ Zurück</button>`:''}`;
}
/* ---------- Start ---------- */
function viewStart(){
  USER=null;const names=Object.keys(DB.users);
  setView(`<div class="top"><span class="logo eltern-hit" data-act="parents">🐍</span><div class="ttl">Python-Trainer <small>Programmieren lernen</small></div></div>
  <h2 class="h2">Wer übt heute?</h2>
  <div class="users">${names.map(n=>`<button class="user" data-act="pick-user" data-n="${esc(n)}"><span>${esc(DB.users[n].avatar)}</span>${esc(n)}</button>`).join('')||'<p class="meta">Noch niemand angelegt.</p>'}</div>
  <div class="panel"><h3>Neu anlegen</h3><label>Name</label><input id="nn" maxlength="20" autocomplete="off"><label>Symbol</label><div class="avs">${AVATARS.map((a,i)=>`<button class="av ${i===0?'sel':''}" data-act="pick-av" data-a="${a}">${a}</button>`).join('')}</div>
  <div class="actions"><button class="btn primary" data-act="add-user">Anlegen ▸</button></div></div>
  <p class="meta" id="syncstat">${syncStatus}${STORAGE_OK?'':' · Speicher im Browser gesperrt!'}</p>`);
}
/* ---------- Home ---------- */
const mins=s=>Math.round((s||0)/60);
function viewHome(){
  const u=USER,k=todayKey(),total=Object.values(u.tasks).filter(p=>p.r+p.w>0).length;
  const due=TASKS.filter(t=>isDue(u,t.id)).length,weak=TASKS.filter(t=>isWeak(u,t.id)).length;
  setView(`${header(u)}
  <div class="panel hero"><h2>Hallo ${esc(u.name)}! ${esc(u.avatar)}</h2>
   <div class="meta">Heute: ${u.days[k]||0} Aufgaben · ${mins(u.dtime[k])} Min. · insgesamt ${total} von ${TASKS.length} Aufgaben probiert${due?` · <b>${due} zur Wiederholung fällig</b>`:''}</div>
   <label>Aufgaben pro Runde</label><div class="seg">${[6,10,15].map(n=>`<button class="${u.settings.len===n?'sel':''}" data-act="len" data-v="${n}">${n}</button>`).join('')}</div>
   <div class="actions"><button class="btn primary big-btn" data-act="train-all">▶ Üben (gemischt)</button>${weak?`<button class="btn" data-act="train-weak">🎯 Wackelaufgaben (${weak})</button>`:''}<button class="btn" data-act="play">🧪 Spielwiese</button></div></div>
  <h2 class="h2">Kapitel</h2>
  <div class="grid">${KAPITEL.map(c=>`<button class="tile" data-act="kap" data-k="${c.id}">${c.icon}<b>${c.id}. ${esc(c.name)}</b><small>${kapDone(u,c.id)} von ${tasksOf(c.id).length} gemeistert</small>${bar(kapMastery(u,c.id))}</button>`).join('')}</div>
  <div class="actions"><button class="btn" data-act="spick">📒 Spickzettel</button></div>
  <p class="meta" id="pystat">Python wird geladen …</p><p class="meta" id="syncstat">${syncStatus}</p>`);
  pyStatus();
}
function viewKap(id){
  const u=USER,c=KAPBY[id],ts=tasksOf(id);
  setView(`${header(u,'home')}<h2 class="h2">${c.icon} ${id}. ${esc(c.name)}</h2><p class="meta">${esc(c.info)}</p>
  <div class="actions"><button class="btn primary" data-act="train-kap" data-k="${id}">▶ Üben in diesem Kapitel</button><button class="btn" data-act="spick" data-k="${id}">📒 Spickzettel</button></div>
  <div class="panel">${[1,2,3].map(l=>{const open=lvlOpen(u,id,l),list=ts.filter(t=>t.lvl===l);if(!list.length)return '';
    return `<h3>Stufe ${l} <span class="dots">${dots(l)}</span>${open?'':' <small>(noch gesperrt – löse erst ein paar Aufgaben der Stufe davor)</small>'}</h3>${list.map(t=>{const p=u.tasks[t.id];const st=!p||!(p.r+p.w)?'neu':p.box>=3?'ok':isWeak(u,t.id)?'weak':'mid';
      return `<div class="sk st-${st}" ><span>${TYPES[t.typ][0]} ${esc(t.titel)}</span><span class="stat">${st==='ok'?'✓ sitzt':st==='weak'?'✗ üben':st==='mid'?'◐ läuft':'·'}</span></div>`;}).join('')}`;}).join('')}</div>`);
}
function viewSpick(k){
  const list=SPICK.filter(s=>!k||s.kap===k);
  setView(`${header(USER,k?'kap-'+k:'home')}<h2 class="h2">📒 Spickzettel</h2>${list.map(s=>`<div class="panel card"><h3>${s.kap}. ${esc(s.titel)}</h3>${s.html}</div>`).join('')}`);
}
/* ---------- Editor ---------- */
const SYMS=[['⇥','    '],['( )','()',1],['[ ]','[]',1],['{ }','{}',1],['" "','""',1],["' '","''",1],[':',':'],['=','='],['#','#'],['\\','\\']];
function edHtml(id,code,rows){
  return `<div class="ed"><pre class="lnum" id="${id}-ln"></pre><textarea id="${id}" class="codein" rows="${rows}" wrap="off" spellcheck="false" autocapitalize="off" autocorrect="off" autocomplete="off">${esc(code)}</textarea></div>
  <div class="syms">${SYMS.map((s,i)=>`<button class="sym" data-act="sym" data-ed="${id}" data-i="${i}">${esc(s[0])}</button>`).join('')}</div>`;
}
function insertAt(ta,text,back){
  ta.focus();const s=ta.selectionStart,e=ta.selectionEnd;ta.setRangeText(text,s,e,'end');
  if(back){const p=ta.selectionEnd-back;ta.selectionStart=ta.selectionEnd=p;}
  ta.dispatchEvent(new Event('input'));
}
function wireEd(id,rows){
  const ta=$('#'+id),ln=$('#'+id+'-ln');if(!ta)return;
  const upd=()=>{const n=Math.max(ta.value.split('\n').length,rows);ln.textContent=Array.from({length:n},(_,i)=>i+1).join('\n');};
  ta.addEventListener('input',upd);ta.addEventListener('scroll',()=>{ln.scrollTop=ta.scrollTop;});upd();
  ta.addEventListener('keydown',e=>{
    if(e.key==='Tab'){e.preventDefault();
      if(e.shiftKey){const v=ta.value,s=ta.selectionStart,ls=v.lastIndexOf('\n',s-1)+1;const m=/^ {1,4}/.exec(v.slice(ls));if(m){ta.setRangeText('',ls,ls+m[0].length,'preserve');ta.selectionStart=ta.selectionEnd=Math.max(ls,s-m[0].length);ta.dispatchEvent(new Event('input'));}}
      else insertAt(ta,'    ');}
    else if(e.key==='Enter'&&!e.shiftKey){
      const v=ta.value,s=ta.selectionStart,ls=v.lastIndexOf('\n',s-1)+1,line=v.slice(ls,s),ind=/^ */.exec(line)[0];
      e.preventDefault();insertAt(ta,'\n'+ind+(/:\s*$/.test(line)?'    ':''));}
  });
}
const SYMBY=i=>SYMS[i];
/* ---------- Aufgaben vorbereiten ---------- */
function inst(t){
  const v=t.vars;if(!v)return JSON.parse(JSON.stringify(t));
  const ks=Object.keys(v),i=rnd(v[ks[0]].length);
  const sub=x=>typeof x==='string'?x.replace(/<<(\w+)>>/g,(m,k)=>v[k][i]):Array.isArray(x)?x.map(sub):x&&typeof x==='object'?Object.fromEntries(Object.entries(x).map(([k,y])=>[k,k==='vars'?y:sub(y)])):x;
  return sub(JSON.parse(JSON.stringify(t)));
}
const testsOf=x=>x.typ==='predict'?[x.stdin||[]]:(x.tests&&x.tests.length?x.tests:[[]]);
const fillGap=(code,ans)=>{let c=code;ans.forEach(a=>{c=c.replace('___',()=>a);});return c;};
function refCode(x){return x.typ==='predict'?x.code:x.typ==='gap'?fillGap(x.code,x.ans):x.typ==='puzzle'?x.lines.join('\n'):x.ref;}
async function expectedOf(x){const code=refCode(x),o=[];for(const tl of testsOf(x))o.push(await pyRun(code,tl));return o;}
async function evalCode(x,code,exp){
  const tests=testsOf(x);
  for(let i=0;i<tests.length;i++){
    const r=await pyRun(code,tests[i]);
    if(r.err)return {ok:false,idx:i,input:tests[i],exp:exp[i].out,got:r.out,err:r.err};
    if(norm(r.out)!==norm(exp[i].out))return {ok:false,idx:i,input:tests[i],exp:exp[i].out,got:r.out};
  }
  for(const nd of x.need||[]){const m=new RegExp(nd.re).test(code);if(m===!!nd.not)return {ok:false,needMsg:nd.msg};}
  return {ok:true};
}
/* ---------- Übungsrunde ---------- */
function startSession(tasks){
  if(!tasks.length){alert('Keine passenden Aufgaben gefunden.');return;}
  SES={ids:tasks.map(t=>t.id),i:0,res:[],t0:Date.now()};pyStart();showTask();
}
function showTask(){
  const t=TASKBY[SES.ids[SES.i]];
  CUR={t,x:inst(t),tries:0,hints:0,done:false,busy:false};
  if(CUR.x.typ==='puzzle'){const n=CUR.x.lines.length;let idx=[...Array(n).keys()];for(let k=0;k<20;k++){idx.sort(()=>Math.random()-0.5);if(idx.some((v,i)=>v!==i))break;}CUR.pz={pool:idx,chosen:[]};}
  CUR.expP=expectedOf(CUR.x);
  renderTask();
  CUR.expP.then(exp=>{const el=$('#expbox');if(el)el.innerHTML=expHtml(exp);});
}
function expHtml(exp){
  const x=CUR.x;if(x.typ==='predict')return '';
  const tl=testsOf(x)[0],o=exp[0].out;
  return `<div class="expl"><b>Erwartete Ausgabe${tl.length?' (Beispiel)':''}:</b>${tl.length?`<br><small>Eingabe: ${tl.map(v=>'<code>'+esc(v)+'</code>').join(' · ')}</small>`:''}<pre class="out">${esc(o)||' '}</pre></div>`;
}
function renderTask(){
  const x=CUR.x,t=CUR.t,n=SES.ids.length,i=SES.i;
  const [ic,tn]=TYPES[x.typ];let body='';
  const stdin=x.typ==='predict'?(x.stdin||[]):[];
  if(x.typ==='predict'){
    body=`${codeBlock(x.code)}${stdin.length?`<div class="meta">Eingabe(n): ${stdin.map(v=>'<code>'+esc(v)+'</code>').join(' · ')}</div>`:''}<label>Was gibt das Programm aus? (jede Zeile genau so, wie sie erscheint)</label><textarea id="ans" class="ansin" rows="4" spellcheck="false" autocapitalize="off" autocorrect="off"></textarea>`;
  }else if(x.typ==='gap'){
    const parts=x.code.split('___');let h='';
    parts.forEach((p,k)=>{h+=esc(p);if(k<parts.length-1)h+=`<input class="gap" id="g${k}" size="${Math.max(5,(x.ans[k]||'').length+3)}" spellcheck="false" autocapitalize="off" autocorrect="off" autocomplete="off">`;});
    body=`<pre class="code gapcode">${h}</pre><div id="expbox"></div>`;
  }else if(x.typ==='puzzle'){
    body=`<div id="pzbox"></div><div id="expbox"></div>`;
  }else{
    const rows=Math.max(8,(x.typ==='bug'?x.code:x.start||'').split('\n').length+3);
    body=`${edHtml('ed',x.typ==='bug'?x.code:(x.start||''),rows)}<div id="expbox"></div><div class="actions"><button class="btn small" data-act="try">▶ Ausprobieren</button></div><div id="tryout"></div>`;
  }
  const hl=x.hints||[];
  setView(`${header(USER)}<div class="prog"><span>Aufgabe ${i+1} von ${n}</span><span><a href="#" data-act="quit">Runde beenden</a></span></div>${bar(i/n)}
  <div class="panel task"><div class="chips"><span class="chip">${ic} ${tn}</span><span class="chip">Stufe ${t.lvl} ${dots(t.lvl)}</span><span class="chip">${KAPBY[t.kap].icon} ${esc(KAPBY[t.kap].name)}</span></div>
  ${(x.typ==='bug'||x.typ==='predict')?'':`<h3>${esc(t.titel)}</h3>`}
  <div class="q">${md(x.text||(x.typ==='predict'?'Lies den Code genau. Was gibt dieses Programm aus?':''))}</div>
  ${body}
  <div id="tips"></div><div id="fb"></div>
  <div class="actions" id="btns"><button class="btn primary" data-act="check">Prüfen</button>${hl.length?`<button class="btn" data-act="hint" id="hintbtn">💡 Tipp (0/${hl.length})</button>`:''}</div></div>
  <p class="meta" id="pystat">Python wird geladen …</p>`);
  if(x.typ==='puzzle')renderPz();
  if(x.typ==='bug'||x.typ==='code')wireEd('ed',Math.max(8,(x.typ==='bug'?x.code:x.start||'').split('\n').length+3));
  pyStatus();
  const first=$('#ans')||$('#g0')||$('#ed');if(first&&!/iPad|iPhone/.test(navigator.userAgent))first.focus();
  $$('.gap').forEach(g=>g.addEventListener('keydown',e=>{if(e.key==='Enter')doCheck();}));
}
function renderPz(){
  const x=CUR.x,pz=CUR.pz;
  const btn=(i,act,k)=>`<button class="pzl" data-act="${act}" data-i="${k}">${esc(x.lines[i])||' '}</button>`;
  $('#pzbox').innerHTML=`<div class="pz"><div class="pzcol"><small>Zeilen – antippen, um sie zu setzen</small>${pz.pool.map((i,k)=>btn(i,'pz-add',k)).join('')||'<small>(alle gesetzt)</small>'}</div>
  <div class="pzcol ans"><small>Dein Programm – antippen, um eine Zeile zurückzulegen</small>${pz.chosen.map((i,k)=>btn(i,'pz-del',k)).join('')||'<small>noch leer</small>'}</div></div>`;
}
function setBusy(b){$$('#btns button').forEach(x=>{x.disabled=b;});}
async function doCheck(){
  if(!CUR||CUR.done||CUR.busy)return;
  const x=CUR.x;let code=null,studentOut=null;
  if(x.typ==='predict'){studentOut=$('#ans').value;if(!studentOut.trim()){say('no','Schreibe zuerst auf, was du erwartest.');return;}}
  else if(x.typ==='gap'){const vals=$$('.gap').map(g=>g.value.trim());if(vals.some(v=>!v)){say('no','Fülle alle Lücken aus.');return;}code=fillGap(x.code,vals);}
  else if(x.typ==='puzzle'){if(CUR.pz.chosen.length<x.lines.length){say('no','Setze erst alle Zeilen.');return;}code=CUR.pz.chosen.map(i=>x.lines[i]).join('\n');}
  else{code=$('#ed').value;if(!code.trim()){say('no','Schreibe zuerst dein Programm.');return;}}
  CUR.busy=true;setBusy(true);say('tip','Wird geprüft …');
  let res;
  try{
    const exp=await CUR.expP;
    if(x.typ==='predict'){res={ok:norm(studentOut)===norm(exp[0].out)};if(!res.ok)res.predict={exp:exp[0].out,got:studentOut};}
    else if(x.typ==='puzzle'&&code===x.lines.join('\n'))res={ok:true};
    else res=await evalCode(x,code,exp);
  }catch(e){res={ok:false,msg:String(e)};}
  CUR.busy=false;setBusy(false);
  CUR.tries++;
  if(res.ok)finishTask(CUR.tries===1?1:0.5,res);else wrong(res);
}
function say(kind,html){const el=$('#fb');if(el)el.innerHTML=`<div class="fb ${kind}">${html}</div>`;}
function wrong(res){
  const x=CUR.x;let h='<b>✗ Noch nicht richtig.</b> ';
  if(res.msg)h+=esc(res.msg);
  else if(res.needMsg)h+='Die Ausgabe stimmt, aber: '+esc(res.needMsg);
  else if(res.predict){
    const a=norm(res.predict.got).split('\n'),b=norm(res.predict.exp).split('\n');
    h+=a.length!==b.length?`Deine Antwort hat ${a.length} Zeile(n), die Ausgabe hat eine andere Zeilenzahl.`:'Die Zeilenzahl passt – prüfe jede Zeile genau (Leerzeichen, Groß-/Kleinschreibung, Zahlen).';
    if(CUR.tries>=2)h+=`<br>Die richtige Ausgabe wäre:<pre class="out">${esc(res.predict.exp)}</pre>`;
  }else{
    if(res.err)h+=`<br><span class="errm">${esc(deErr(res.err))}</span>`;
    else{
      h+='Die Ausgabe passt noch nicht.';
      const tl=res.input||[];
      h+=`<br><small>${tl.length?'Bei Eingabe '+tl.map(v=>'<code>'+esc(v)+'</code>').join(' · ')+' – ':''}erwartet:</small><pre class="out">${esc(res.exp)||' '}</pre><small>dein Programm gibt aus:</small><pre class="out">${esc(res.got)||'(nichts)'}</pre>`;
    }
  }
  const showSol=CUR.tries>=2;
  say('no',h);
  $('#btns').innerHTML=`<button class="btn primary" data-act="check">Nochmal prüfen</button>${(CUR.x.hints||[]).length?`<button class="btn" data-act="hint" id="hintbtn">💡 Tipp (${CUR.hints}/${CUR.x.hints.length})</button>`:''}${showSol?'<button class="btn" data-act="solution">Lösung zeigen</button>':''}`;
  if(CUR.hints>=(CUR.x.hints||[]).length&&$('#hintbtn'))$('#hintbtn').disabled=true;
}
function solutionHtml(){
  const x=CUR.x;
  if(x.typ==='predict')return CUR.expOut!=null?`<pre class="out">${esc(CUR.expOut)}</pre>`:'';
  return `<pre class="code">${esc(refCode(x))}</pre>`;
}
async function showSolution(){
  if(CUR.done)return;
  const exp=await CUR.expP;CUR.expOut=exp[0].out;
  finishTask(0,{});
}
function finishTask(score,res){
  CUR.done=true;CUR.score=score;
  recordAnswer(USER,CUR.t.id,score);persist();SES.res.push({id:CUR.t.id,score});
  const x=CUR.x;
  (async()=>{const exp=await CUR.expP;CUR.expOut=exp[0].out;
    const ok=score>0;
    let h=ok?`<b>✓ ${score>=1?'Richtig – gleich beim ersten Versuch!':'Richtig!'}</b>`:'<b>Lösung</b> (zählt diesmal nicht – versuche es später noch einmal)';
    if(x.typ==='predict')h+=`<br><small>Das Programm gibt aus:</small><pre class="out">${esc(exp[0].out)}</pre>`;
    else if(!ok||x.typ==='code'||x.typ==='bug')h+=`<details ${ok?'':'open'}><summary>${ok?'Musterlösung ansehen':'Lösung'}</summary><pre class="code">${esc(refCode(x))}</pre></details>`;
    if(x.expl)h+=`<div class="tip">${md(x.expl)}</div>`;
    $('#fb').innerHTML=`<div class="fb ${ok?'ok':'no'}">${h}</div>`;
    const last=SES.i>=SES.ids.length-1;
    $('#btns').innerHTML=`<button class="btn primary" data-act="next">${last?'Fertig ▸':'Weiter ▸'}</button>`;
    $$('#app textarea,#app input.gap').forEach(e=>{e.readOnly=true;});
  })();
}
function nextTask(){SES.i++;if(SES.i>=SES.ids.length)return viewSummary();showTask();}
function viewSummary(){
  const pts=SES.res.reduce((a,r)=>a+r.score,0),n=SES.res.length;
  USER.log.push({t:Date.now(),kap:SES.ids.length?TASKBY[SES.ids[0]].kap:0,n,pts,secs:Math.round((Date.now()-SES.t0)/1000)});
  if(USER.log.length>300)USER.log=USER.log.slice(-300);persist();
  const pct=n?pts/n:0;
  setView(`${header(USER)}<div class="panel hero"><h2>Runde geschafft! ${pct>=0.8?'🎉':pct>=0.5?'👍':'💪'}</h2><div class="big">${pts} von ${n} Punkten</div>${bar(pct)}
  <p class="meta">Ganze Punkte gibt es für richtige Lösungen im ersten Versuch, halbe für richtige Lösungen nach einem Fehlversuch.</p></div>
  <div class="panel">${SES.res.map(r=>{const t=TASKBY[r.id];return `<div class="sk"><span>${TYPES[t.typ][0]} ${esc(t.titel)}</span><span class="stat">${r.score>=1?'✓':r.score>0?'◐':'✗'}</span></div>`;}).join('')}</div>
  <div class="actions"><button class="btn primary big-btn" data-act="again">Noch eine Runde ▸</button><button class="btn" data-act="home">Fertig</button></div>`);
  SES.again=SES.lastScope;
}
/* ---------- Spielwiese ---------- */
function viewPlay(){
  let code='print("Hallo Welt")';try{code=localStorage.getItem(LS_KEY+'-play')||code;}catch(e){}
  setView(`${header(USER,'home')}<h2 class="h2">🧪 Spielwiese</h2><p class="meta">Probiere hier frei Python aus. Wenn dein Programm <code>input()</code> benutzt, schreibe die Eingaben unten hinein (eine pro Zeile).</p>
  ${edHtml('pg',code,12)}
  <label>Eingaben für input() (eine pro Zeile)</label><textarea id="pgin" class="ansin" rows="2" spellcheck="false"></textarea>
  <div class="actions"><button class="btn primary" data-act="pgrun">▶ Ausführen</button></div><div id="pgout"></div><p class="meta" id="pystat">Python wird geladen …</p>`);
  wireEd('pg',12);pyStatus();
}
function outHtml(r){
  let h=r.out?`<pre class="out">${esc(r.out)}</pre>`:'<pre class="out"><i>(keine Ausgabe)</i></pre>';
  if(r.err)h+=`<div class="fb no errm">${esc(deErr(r.err))}</div>`;
  return h;
}
/* ---------- Eltern-Bereich ---------- */
function lastDays(u,n){const o=[];for(let i=n-1;i>=0;i--){const d=new Date(Date.now()-i*DAY),k=todayKey(d.getTime());o.push({k,s:u.dtime[k]||0,n:u.days[k]||0,d});}return o;}
function viewParents(){
  const names=Object.keys(DB.users);
  setView(`<div class="top"><span class="logo">🐍</span><div class="ttl">Eltern-Bereich <small>Auswertung je Kind</small></div></div><button class="back" data-act="${USER?'home':'start'}">‹ Zurück</button>
  ${names.map(n=>{const u=DB.users[n],w=lastDays(u,7),k=todayKey();return `<div class="panel"><h3>${esc(u.avatar)} ${esc(n)}</h3><div class="meta">Heute: ${u.days[k]||0} Aufgaben · ${mins(u.dtime[k])} Min. · letzte 7 Tage: ${mins(w.reduce((a,d)=>a+d.s,0))} Min., ${w.reduce((a,d)=>a+d.n,0)} Aufgaben</div><div class="actions"><button class="btn small" data-act="pchild" data-n="${esc(n)}">Auswertung ▸</button></div></div>`;}).join('')||'<p class="meta">Noch niemand angelegt.</p>'}`);
}
function viewParentChild(n){
  const u=DB.users[n];if(!u)return viewParents();
  const w=lastDays(u,14),mx=Math.max(60,...w.map(d=>d.s));
  const weak=TASKS.filter(t=>isWeak(u,t.id));
  setView(`<div class="top"><span class="logo">🐍</span><div class="ttl">${esc(u.avatar)} ${esc(n)} <small>Auswertung</small></div></div><button class="back" data-act="parents">‹ Zurück</button>
  <div class="panel"><h3>Kapitel</h3>${KAPITEL.map(c=>`<div class="sk"><span>${c.icon} ${c.id}. ${esc(c.name)}</span><span>${kapDone(u,c.id)}/${tasksOf(c.id).length} sitzen</span></div>${bar(kapMastery(u,c.id))}`).join('')}</div>
  <div class="panel"><h3>Übungszeit (14 Tage, Minuten)</h3><div class="days">${w.map(d=>`<div class="d"><small>${mins(d.s)}</small><i style="height:${Math.round(d.s/mx*60)}px"></i><small>${d.d.getDate()}.</small></div>`).join('')}</div></div>
  <div class="panel"><h3>Hier lohnt sich Nachfragen</h3>${weak.length?weak.map(t=>{const p=u.tasks[t.id];return `<div class="sk"><span>${TYPES[t.typ][0]} ${esc(t.titel)} <small>(Kap. ${t.kap})</small></span><span>${p.r} richtig · ${p.w} falsch</span></div>`;}).join(''):'<p class="meta">Keine auffälligen Aufgaben.</p>'}</div>
  <div class="panel"><h3>Letzte Runden</h3>${u.log.slice(-8).reverse().map(l=>`<div class="sk"><span>${fmtDate(l.t)} · ${l.n} Aufgaben</span><span>${l.pts} Punkte</span></div>`).join('')||'<p class="meta">Noch keine Runde.</p>'}</div>
  <div class="panel"><h3>Kind löschen</h3><p class="meta">Löscht den Lernstand auf allen Geräten. Zur Bestätigung den Namen eintippen.</p><input id="delname" autocomplete="off" placeholder="${esc(n)}"><div class="actions"><button class="btn danger" data-act="pdel" data-n="${esc(n)}">Endgültig löschen</button></div></div>`);
}
/* ---------- Aktionen ---------- */
let AVSEL=AVATARS[0];
function runScope(kind,k){
  const u=USER,len=u.settings.len;let tasks;
  if(kind==='weak')tasks=TASKS.filter(t=>isWeak(u,t.id)||isDue(u,t.id)).sort(()=>Math.random()-0.5).slice(0,len);
  else tasks=pickTasks(u,kind==='kap'?[k]:KAPITEL.map(c=>c.id),len);
  startSession(tasks);if(SES)SES.lastScope={kind,k};
}
document.addEventListener('click',async e=>{
  const el=e.target.closest('[data-act]');if(!el)return;
  const a=el.dataset.act;
  if(a==='quit'||el.tagName==='A')e.preventDefault();
  switch(a){
    case 'pick-av':AVSEL=el.dataset.a;$$('.av').forEach(b=>b.classList.toggle('sel',b===el));break;
    case 'add-user':{const n=$('#nn').value.trim();if(!n)return;if(DB.users[n]){alert('Den Namen gibt es schon.');return;}DB.users[n]=newUser(n,AVSEL);delete DB.deleted[n];touch(DB.users[n]);USER=DB.users[n];DB.last=n;setLast(n);persist();viewHome();break;}
    case 'pick-user':USER=DB.users[el.dataset.n];DB.last=USER.name;setLast(USER.name);persist();viewHome();break;
    case 'switch':case 'start':if(SES&&CUR&&!CUR.done&&!confirm('Runde abbrechen?'))return;viewStart();break;
    case 'home':viewHome();break;
    case 'len':USER.settings.len=+el.dataset.v;touch(USER);persist();viewHome();break;
    case 'kap':viewKap(+el.dataset.k);break;
    case 'spick':viewSpick(el.dataset.k?+el.dataset.k:0);break;
    case 'train-all':runScope('all');break;
    case 'train-weak':runScope('weak');break;
    case 'train-kap':runScope('kap',+el.dataset.k);break;
    case 'again':{const s=SES&&SES.again||{kind:'all'};runScope(s.kind,s.k);break;}
    case 'play':viewPlay();break;
    case 'pgrun':{const code=$('#pg').value;try{localStorage.setItem(LS_KEY+'-play',code);}catch(x){}
      $('#pgout').innerHTML='<div class="fb tip">Läuft …</div>';bumpTime(USER);
      const r=await pyRun(code,$('#pgin').value.split('\n').filter((l,i,arr)=>!(i===arr.length-1&&l==='')),{echo:true});
      $('#pgout').innerHTML=outHtml(r);break;}
    case 'try':{const code=$('#ed').value;$('#tryout').innerHTML='<div class="fb tip">Läuft …</div>';bumpTime(USER);
      const r=await pyRun(code,testsOf(CUR.x)[0],{});$('#tryout').innerHTML=outHtml(r);break;}
    case 'sym':{const s=SYMBY(+el.dataset.i);insertAt($('#'+el.dataset.ed),s[1],s[2]||0);break;}
    case 'check':doCheck();break;
    case 'hint':if(CUR&&CUR.hints<(CUR.x.hints||[]).length){const h=CUR.x.hints[CUR.hints];CUR.hints++;$('#tips').insertAdjacentHTML('beforeend',`<div class="tip">💡 ${md(h)}</div>`);const b=$('#hintbtn');if(b){b.textContent=`💡 Tipp (${CUR.hints}/${CUR.x.hints.length})`;if(CUR.hints>=CUR.x.hints.length)b.disabled=true;}}break;
    case 'solution':showSolution();break;
    case 'next':nextTask();break;
    case 'quit':if(confirm('Runde beenden? Bisherige Ergebnisse bleiben gespeichert.')){if(SES.res.length)viewSummary();else viewHome();}break;
    case 'pz-add':{const k=+el.dataset.i;CUR.pz.chosen.push(CUR.pz.pool.splice(k,1)[0]);renderPz();break;}
    case 'pz-del':{const k=+el.dataset.i;CUR.pz.pool.push(CUR.pz.chosen.splice(k,1)[0]);renderPz();break;}
    case 'parents':viewParents();break;
    case 'pchild':viewParentChild(el.dataset.n);break;
    case 'pdel':{const n=el.dataset.n;if($('#delname').value.trim()!==n){alert('Name stimmt nicht überein.');return;}deleteUser(n);if(USER&&USER.name===n)USER=null;viewParents();break;}
  }
});
/* ---------- Start ---------- */
async function checkBuild(){
  try{const r=await fetch('api/build',{cache:'no-store'});if(!r.ok)return;const d=await r.json();
    if(d.build&&d.build!==BUILD&&!$('#upd'))document.body.insertAdjacentHTML('afterbegin',`<div class="upd" id="upd"><span>Neue Version verfügbar.</span><button class="btn small" onclick="location.reload()">Neu laden</button></div>`);}catch(e){}
}
(async function init(){
  loadLocal();await initServer();
  const last=getLast();
  if(last&&DB.users[last]){USER=DB.users[last];viewHome();}else viewStart();
  setInterval(checkBuild,300000);document.addEventListener('visibilitychange',()=>{if(!document.hidden)checkBuild();});
})();
