/* ===== Oberfläche: Start, Lernpfad, Erklärungen, Aufgaben, Spielwiese, Spickzettel, Eltern-Bereich ===== */
'use strict';
let USER=null,SES=null,CUR=null;
/* ---------- Icons (Linien-SVG) ---------- */
const IC={
 home:'<path d="M4 11l8-7 8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z"/>',
 star:'<path d="M12 3l2.6 5.6 6 .8-4.4 4.2 1.1 6L12 16.7 6.7 19.6l1.1-6L3.4 9.4l6-.8z"/>',
 code:'<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
 book:'<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
 flame:'<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 .3 1.5 1.2 2.3 2 2.5C10.5 8.5 11 6 12 3z"/>',
 check:'<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 lock:'<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 play:'<path d="M8 5.5v13a1 1 0 0 0 1.5.9l10.5-6.5a1 1 0 0 0 0-1.8L9.5 4.6A1 1 0 0 0 8 5.5z"/>',
 x:'<path d="M6 6l12 12M18 6L6 18"/>',
 bulb:'<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 chevL:'<path d="M15 5l-7 7 7 7"/>',
 warn:'<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18.5v.1"/>',
 eye:'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 gap:'<path d="M9 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h3M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3M9 12h6"/>',
 bug:'<path d="M8 8h8v6a4 4 0 0 1-8 0zM9 5l1.5 2M15 5l-1.5 2M4 11h4M16 11h4M5 18l3-2M19 18l-3-2M12 8v12"/>',
 list:'<path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/>'
};
const ic=(n,s=22)=>`<svg class="ic" width="${s}" height="${s}" viewBox="0 0 24 24" fill="${n==='play'?'currentColor':'none'}" stroke="${n==='play'?'none':'currentColor'}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${IC[n]}</svg>`;
const TICON={predict:'eye',gap:'gap',bug:'bug',puzzle:'list',code:'code'};
const LOGO=`<span class="logo eltern-hit" data-act="parents">${ic('code',22)}</span>`;
const bar=p=>`<div class="bar"><i style="width:${Math.round(p*100)}%"></i></div>`;
const dots=n=>'●'.repeat(n)+'○'.repeat(3-n);
const norm=s=>String(s||'').replace(/\r/g,'').split('\n').map(l=>l.replace(/\s+$/,'')).join('\n').replace(/^\n+|\n+$/g,'');
function md(s){
  return String(s||'').split(/```\n?/).map((p,i)=>i%2?`<pre class="blk">${esc(p.replace(/\n$/,''))}</pre>`:esc(p).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\n/g,'<br>')).join('');
}
const codeBlock=c=>`<pre class="code">${esc(c).split('\n').map((l,i)=>`<span class="ln">${i+1}</span>${l}`).join('\n')}</pre>`;
function pyStatus(){pyStart().then(ok=>{const el=$('#pystat');if(el)el.textContent=ok?'Python bereit ✓':'Python konnte nicht geladen werden – bitte Seite neu laden.';});}
/* ---------- Rückmeldungs-Blatt, Navigation, Grundgerüst ---------- */
function closeSheet(){['scrim','sheet'].forEach(i=>{const e=document.getElementById(i);if(e)e.remove();});}
function openSheet(kind,html,btns){
  closeSheet();
  document.body.insertAdjacentHTML('beforeend',`<div class="scrim" id="scrim" data-act="sheetclose"></div><div class="sheet ${kind}" id="sheet" role="dialog" aria-live="polite"><div class="sheetin">${html}<div class="sheetbtns">${btns}</div></div></div>`);
}
const NAVS=[['home','home','Lernpfad'],['practice','star','Üben'],['play','code','Spielwiese'],['spick','book','Spickzettel']];
function renderNav(active){
  const n=$('#nav');
  if(!active||!USER){n.hidden=true;document.body.classList.remove('hasnav');return;}
  n.hidden=false;document.body.classList.add('hasnav');
  n.innerHTML=`<div class="brand">${LOGO}<span>Python-Trainer<small>Programmieren lernen</small></span></div>
  ${NAVS.map(([id,i,l])=>`<button class="nb ${id===active?'on':''}" data-act="${id}" ${id===active?'aria-current="page"':''}>${ic(i,24)}${l}</button>`).join('')}
  <div class="sp"></div><div class="side-user" data-act="switch" role="button" tabindex="0"><span class="av2">${esc(USER.avatar)}</span><span><b>${esc(USER.name)}</b><br><small>Wechseln</small></span></div>
  <div class="side-ver"><span class="syncstat">${syncStatus}</span> · Version ${APP_VERSION}</div>`;
}
function setView(h,nav){closeSheet();$('#app').innerHTML=h;window.scrollTo(0,0);renderNav(nav);}
function header(u,back){
  return `<div class="top">${LOGO}<div class="ttl">Python-Trainer<small>Programmieren lernen</small></div>${u?`<button class="who" data-act="switch"><span class="av2">${esc(u.avatar)}</span>${esc(u.name)}</button>`:''}</div>${back?`<button class="back" data-act="${back}">${ic('chevL',18)}Zurück</button>`:''}`;
}
const ringHtml=(done,goal,size=84,r=34,col='var(--btn)',track='var(--pri-t)',inner)=>{
  const c=2*Math.PI*r,p=Math.min(1,goal?done/goal:0),s=size/84*r*2+0;
  return `<div class="ring" style="width:${size}px;height:${size}px"><svg width="${size}" height="${size}" viewBox="0 0 84 84" aria-hidden="true"><circle cx="42" cy="42" r="${r}" fill="none" stroke="${track}" stroke-width="9"/><circle cx="42" cy="42" r="${r}" fill="none" stroke="${col}" stroke-width="9" stroke-linecap="round" stroke-dasharray="${(c*p).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 42 42)"/></svg><div class="rc">${inner||`${done}<small>von ${goal}</small>`}</div></div>`;
};
/* ---------- Start (Wer übt heute?) ---------- */
function viewStart(){
  USER=null;const names=Object.keys(DB.users);
  setView(`<div class="top">${LOGO}<div class="ttl">Python-Trainer<small>Programmieren lernen</small></div></div>
  <h2 class="h2">Wer übt heute?</h2>
  <div class="users">${names.map(n=>`<button class="user" data-act="pick-user" data-n="${esc(n)}"><span class="av2">${esc(DB.users[n].avatar)}</span>${esc(n)}</button>`).join('')||'<p class="meta">Noch niemand angelegt.</p>'}</div>
  <div class="panel"><h3>Neu anlegen</h3><label for="nn">Name</label><input id="nn" maxlength="20" autocomplete="off"><label>Symbol</label><div class="avs">${AVATARS.map((a,i)=>`<button class="av ${i===0?'sel':''}" data-act="pick-av" data-a="${a}" aria-label="Symbol ${a}">${a}</button>`).join('')}</div>
  <div class="actions"><button class="btn primary" data-act="add-user">Anlegen</button></div></div>
  <p class="meta foot"><span id="syncstat" class="syncstat">${syncStatus}${STORAGE_OK?'':' · Speicher im Browser gesperrt!'}</span> · <span id="appver">Version ${APP_VERSION}</span></p>`);
}
/* ---------- Lernpfad (Startseite) ---------- */
const mins=s=>Math.round((s||0)/60);
const nextLesson=u=>LERNEN.find(l=>!lessonRead(u,l.id)&&kapOpen(u,l.kap))||null;
function kapState(u,id){
  const tot=tasksOf(id).length,att=tasksOf(id).some(t=>u.tasks[t.id]&&(u.tasks[t.id].r+u.tasks[t.id].w)>0);
  if(kapDone(u,id)>=Math.ceil(tot*0.75))return 'done';
  if(!kapOpen(u,id)&&!att)return 'later';
  return 'open';
}
function viewHome(){
  const u=USER,k=todayKey(),goal=goalOf(u),done=u.days[k]||0,st=streakOf(u),nl=nextLesson(u);
  const due=TASKS.filter(t=>isDue(u,t.id)).length;
  const cur=KAPITEL.find(c=>kapState(u,c.id)==='open');
  const cont=nl?{act:'lesson',d:`data-l="${nl.id}"`,l:'Weiter lernen',t:nl.titel,s:`Kapitel ${nl.kap} · Erklärung · ${nl.min} Min.`,i:'book'}:{act:'train-all',d:'',l:'Weiter üben',t:due?`${due} Aufgaben zur Wiederholung`:'Gemischte Runde',s:`${u.settings.len} Aufgaben`,i:'play'};
  setView(`${header(u)}
  <div class="hello"><div class="t">Hallo ${esc(u.name)}!<small>${st?`Du übst schon ${st} ${st===1?'Tag':'Tage'} in Folge – weiter so.`:'Schön, dass du da bist.'}</small></div>${st?`<span class="streak">${ic('flame',20)}${st} ${st===1?'Tag':'Tage'}</span>`:''}</div>
  <div class="panel goalcard">${ringHtml(done,goal)}<div><div class="gt">Tagesziel</div><div class="gs">${done>=goal?'Geschafft! Weiter üben macht trotzdem schlauer.':`Noch ${goal-done} ${goal-done===1?'Aufgabe':'Aufgaben'} – heute schon ${mins(u.dtime[k])} Min. geübt.`}</div></div></div>
  <button class="cont" data-act="${cont.act}" ${cont.d}><span class="ci">${ic(cont.i,26)}</span><span><span class="cl">${cont.l}</span><br><span class="ct">${esc(cont.t)}</span><br><span class="cs">${cont.s}</span></span></button>
  <div class="sec"><span class="st">Dein Lernpfad</span><small>${KAPITEL.length} Kapitel</small></div>
  <div class="path">${KAPITEL.map(c=>{const s=kapState(u,c.id),isCur=cur&&cur.id===c.id;
    return `<button class="pi ${s==='done'?'done':''} ${isCur?'cur':''} ${s==='later'?'later':''}" data-act="kap" data-k="${c.id}"><span class="pn">${s==='done'?ic('check',22):s==='later'?ic('lock',20):c.id}</span><span class="pt"><b>${c.id} · ${esc(c.name)}</b><small>${kapDone(u,c.id)} von ${tasksOf(c.id).length} gemeistert · ${kapLessonsRead(u,c.id)}/${lessonsOf(c.id).length} Erklärungen${s==='later'?' · kommt später':''}</small></span><span class="pb"><i style="width:${Math.round(kapMastery(u,c.id)*100)}%"></i></span></button>`;}).join('')}</div>
  <p class="meta foot" id="pystat">Python wird geladen …</p><p class="meta foot"><span id="syncstat" class="syncstat">${syncStatus}</span> · <span id="appver">Version ${APP_VERSION}</span></p>`,'home');
  pyStatus();
}
function viewPractice(){
  const u=USER,weak=TASKS.filter(t=>isWeak(u,t.id)||isDue(u,t.id)).length;
  setView(`${header(u)}<h2 class="h2">Üben</h2>
  <button class="cont" data-act="train-all"><span class="ci">${ic('play',26)}</span><span><span class="cl">Empfohlen</span><br><span class="ct">Gemischte Runde</span><br><span class="cs">${u.settings.len} Aufgaben aus deinen Kapiteln</span></span></button>
  ${weak?`<div class="panel"><h3>Wackelaufgaben</h3><p class="meta">${weak} Aufgaben sind fällig oder haben noch nicht gesessen.</p><div class="actions"><button class="btn" data-act="train-weak">Wackelaufgaben üben</button></div></div>`:''}
  <div class="panel"><h3>Aufgaben pro Runde</h3><div class="seg">${[6,10,15].map(n=>`<button class="${u.settings.len===n?'sel':''}" data-act="len" data-v="${n}">${n}</button>`).join('')}</div>
  <label>Tagesziel (Aufgaben pro Tag)</label><div class="seg">${[5,10,15,20].map(n=>`<button class="${goalOf(u)===n?'sel':''}" data-act="goal" data-v="${n}">${n}</button>`).join('')}</div></div>
  <div class="panel"><h3>Kapitel wählen</h3>${KAPITEL.map(c=>`<button class="lrow" data-act="train-kap" data-k="${c.id}"><span class="li">${c.id}</span><span class="lt2">${esc(c.name)}</span><small>${tasksOf(c.id).length} Aufgaben</small></button>`).join('')}</div>`,'practice');
}
function viewKap(id){
  const u=USER,c=KAPBY[id],ts=tasksOf(id),ls=lessonsOf(id),nextL=ls.find(l=>!lessonRead(u,l.id));
  setView(`${header(u,'home')}
  <div class="kaphero"><div class="kt"><div class="kl">Kapitel ${id}</div><div class="kn">${esc(c.name)}</div><div class="ki">${esc(c.info)}</div></div>${ringHtml(kapDone(u,id),ts.length,88,36,'var(--yel)','rgba(255,255,255,.25)')}</div>
  <div class="sec" style="margin-top:6px"><span class="st">Erst verstehen</span><small>${kapLessonsRead(u,id)} von ${ls.length} gelesen</small></div>
  ${ls.map(l=>`<button class="lrow ${lessonRead(u,l.id)?'read':''} ${nextL&&nextL.id===l.id?'next':''}" data-act="lesson" data-l="${l.id}"><span class="li">${lessonRead(u,l.id)?ic('check',18):nextL&&nextL.id===l.id?ic('play',16):ic('book',18)}</span><span class="lt2">${esc(l.titel)}</span><small>${l.min} Min.</small></button>`).join('')}
  <div class="sec"><span class="st">Dann üben</span><small>${ts.length} Aufgaben</small></div>
  <div class="panel"><div class="chips">${Object.keys(TYPES).map(k=>{const n=ts.filter(t=>t.typ===k).length;return n?`<span class="chip">${ic(TICON[k],14)}${TYPES[k][1]} · ${n}</span>`:'';}).join('')}</div>
   <p class="meta" style="margin:8px 0 0">Stufe 2 und 3 schalten sich frei, sobald du ein paar Aufgaben der Stufe davor gelöst hast.</p>
   <details><summary>Alle Aufgaben anzeigen</summary>${[1,2,3].map(l=>{const open=lvlOpen(u,id,l),list=ts.filter(t=>t.lvl===l);if(!list.length)return '';
    return `<h3 style="margin-top:12px">Stufe ${l} <span class="dots">${dots(l)}</span>${open?'':' <small>(noch gesperrt)</small>'}</h3>${list.map(t=>{const p=u.tasks[t.id];const s=!p||!(p.r+p.w)?'neu':p.box>=3?'ok':isWeak(u,t.id)?'weak':'mid';
      return `<div class="sk st-${s}"><span>${ic(TICON[t.typ],16)}${esc(t.titel)}</span><span class="stat">${s==='ok'?'✓ sitzt':s==='weak'?'✗ üben':s==='mid'?'◐ läuft':'·'}</span></div>`;}).join('')}`;}).join('')}</details></div>
  <div class="actions"><button class="btn" data-act="spick" data-k="${id}">${ic('book',18)}Spickzettel</button></div>
  <div class="stickbar"><div class="stickin"><button class="btn primary grow big-btn" data-act="train-kap" data-k="${id}">Aufgaben üben</button></div></div>`,'home');
}
function viewSpick(k){
  const list=SPICK.filter(s=>!k||s.kap===k);
  setView(`${header(USER,k?'kap-'+k:null)}<h2 class="h2">Spickzettel</h2>${list.map(s=>`<div class="panel card"><h3>${s.kap}. ${esc(s.titel)}</h3>${s.html}</div>`).join('')}`,'spick');
}
/* ---------- Editor ---------- */
const SYMS=[['⇥','    '],['( )','()',1],['[ ]','[]',1],['{ }','{}',1],['" "','""',1],["' '","''",1],[':',':'],['=','='],['#','#'],['\\','\\']];
function edHtml(id,code,rows,nosyms){
  return `<div class="ed"><pre class="lnum" id="${id}-ln"></pre><textarea id="${id}" class="codein" rows="${rows}" wrap="off" spellcheck="false" autocapitalize="off" autocorrect="off" autocomplete="off" aria-label="Code">${esc(code)}</textarea></div>
  ${nosyms?'':`<div class="syms">${SYMS.map((s,i)=>`<button class="sym" data-act="sym" data-ed="${id}" data-i="${i}">${esc(s[0])}</button>`).join('')}</div>`}`;
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
/* ---------- Erklär-Abschnitte ---------- */
const LEX={},LQ={};
function lessonHtml(l,pre){
  return l.blocks.map((b,i)=>{
    if(b.t==='t')return `<div class="lt">${b.h}</div>`;
    if(b.t==='tip')return `<div class="callout tip">${ic('bulb',22)}<div>${b.h}</div></div>`;
    if(b.t==='warn')return `<div class="callout warn">${ic('warn',22)}<div>${b.h}</div></div>`;
    const id=`${pre}-${l.id}-${i}`;LEX[id]=b;const rows=Math.max(3,b.code.split('\n').length+1);
    return `<div class="ex"><div class="exh">${ic('play',12)} Probier es aus${b.in.length?` <small>· Eingabe: ${b.in.map(v=>'<code>'+esc(v)+'</code>').join(' · ')}</small>`:''}${b.err?' <small>· enthält absichtlich einen Fehler</small>':''}</div>${edHtml(id,b.code,rows,true)}<div class="actions" style="margin-top:10px"><button class="btn small primary" data-act="exrun" data-id="${id}">${ic('play',14)}Ausführen</button><button class="btn small" data-act="exreset" data-id="${id}">Zurücksetzen</button></div><div id="${id}-out"></div></div>`;
  }).join('');
}
function wireLesson(l,pre){l.blocks.forEach((b,i)=>{if(b.t==='c')wireEd(`${pre}-${l.id}-${i}`,Math.max(3,b.code.split('\n').length+1));});}
const quizHtml=l=>`<div class="panel"><h3>Kurz-Check</h3>${l.quiz.map((q,qi)=>`<div class="quiz" id="q-${l.id}-${qi}"><div class="qq">${qi+1}. ${q.q}</div>${q.o.map((o,oi)=>`<button class="qopt" data-act="lq" data-l="${l.id}" data-q="${qi}" data-o="${oi}">${o}</button>`).join('')}<div class="qwhy"></div></div>`).join('')}<div id="q-${l.id}-res"></div></div>`;
function viewLesson(id){
  const l=LESSONBY[id],u=USER,c=KAPBY[l.kap],list=lessonsOf(l.kap),idx=list.findIndex(x=>x.id===id),next=list[idx+1];
  LQ[id]={};pyStart();
  setView(`<div class="tasktop"><button class="roundbtn" data-act="kap-${l.kap}" aria-label="Zurück zum Kapitel">${ic('x',20)}</button><div class="pw">${bar((idx+1)/list.length)}<small>Abschnitt ${idx+1} von ${list.length} · ${lessonRead(u,id)?'schon gelesen':'noch nicht gelesen'}</small></div></div>
  <div class="chips"><span class="chip">Kapitel ${l.kap} · ${esc(c.name)}</span><span class="chip g">ca. ${l.min} Min.</span></div>
  <h2 class="h2" style="margin-top:4px">${esc(l.titel)}</h2>
  <div class="lesson">${lessonHtml(l,'ex')}</div>${quizHtml(l)}
  <div class="stickbar"><div class="stickin"><button class="btn" data-act="ltrain" data-l="${id}">Dazu üben <small>${l.tasks.length}</small></button><button class="btn primary grow" data-act="ldone" data-l="${id}">Verstanden</button></div></div>`);
  wireLesson(l,'ex');
}
function answerQuiz(el){
  const l=LESSONBY[el.dataset.l],qi=+el.dataset.q,oi=+el.dataset.o,q=l.quiz[qi],box=$('#q-'+l.id+'-'+qi);
  if(!box||box.dataset.done)return;box.dataset.done='1';
  const right=oi===q.a;LQ[l.id][qi]=right;
  $$('.qopt',box).forEach((b,i)=>{b.disabled=true;if(i===q.a)b.classList.add('right');else if(i===oi)b.classList.add('wrong');if(i===q.a)b.insertAdjacentText('afterbegin','✓ ');else if(i===oi)b.insertAdjacentText('afterbegin','✗ ');});
  $('.qwhy',box).innerHTML=`<div class="tip">${right?'Richtig! ':'Nicht ganz. '}${q.why}</div>`;
  if(Object.keys(LQ[l.id]).length===l.quiz.length){
    const sc=Object.values(LQ[l.id]).filter(Boolean).length;markRead(USER,l.id,sc,l.quiz.length);persist();
    $('#q-'+l.id+'-res').innerHTML=`<div class="fb ${sc===l.quiz.length?'ok':'no'}"><b>${sc===l.quiz.length?'✓ Alles richtig!':sc+' von '+l.quiz.length+' richtig'}</b> – ${sc===l.quiz.length?'du bist bereit für die Aufgaben.':'lies die Stellen oben noch einmal durch, dann klappt es.'}</div>`;
  }
}
/* ---------- Aufgaben vorbereiten ---------- */
function inst(t){
  const v=t.vars;if(!v)return JSON.parse(JSON.stringify(t));
  const ks=Object.keys(v),i=rnd(v[ks[0]].length);
  const sub=x=>typeof x==='string'?x.replace(/<<(\w+)>>/g,(m,k)=>v[k][i]):Array.isArray(x)?x.map(sub):x&&typeof x==='object'?Object.fromEntries(Object.entries(x).map(([k,y])=>[k,k==='vars'?y:sub(y)])):x;
  return sub(JSON.parse(JSON.stringify(t)));
}
const testsOf=x=>x.typ==='predict'?[x.stdin||[]]:(x.tests&&x.tests.length?x.tests:[[]]);
const fillGap=(code,ans)=>{let c=code;ans.forEach(a=>{c=c.replace('___',()=>a);});return c;};
const withApp=(x,c)=>x.append?c+'\n'+x.append:c;   // Testaufrufe, die nach dem Schülercode laufen (z. B. bei Funktionen)
function refCode(x){return withApp(x,x.typ==='predict'?x.code:x.typ==='gap'?fillGap(x.code,x.ans):x.typ==='puzzle'?x.lines.join('\n'):x.ref);}
async function expectedOf(x){const code=refCode(x),o=[];for(const tl of testsOf(x))o.push(await pyRun(code,tl));return o;}
async function evalCode(x,code,exp){
  const tests=testsOf(x);
  for(let i=0;i<tests.length;i++){
    const r=await pyRun(withApp(x,code),tests[i]);
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
  return `<div class="expl"><b>Erwartete Ausgabe${tl.length?' (Beispiel)':''}</b>${tl.length?`<br><small>Eingabe: ${tl.map(v=>'<code>'+esc(v)+'</code>').join(' · ')}</small>`:''}<pre class="out">${esc(o)||' '}</pre></div>`;
}
function renderBtns(){
  const el=$('#btns');if(!el||!CUR)return;const hl=CUR.x.hints||[];
  if(CUR.done){const last=SES.i>=SES.ids.length-1;el.innerHTML=`<button class="btn primary grow big-btn" data-act="next">${last?'Fertig':'Weiter'}</button>`;return;}
  el.innerHTML=`${hl.length?`<button class="btn" data-act="hint" id="hintbtn" ${CUR.hints>=hl.length?'disabled':''}>${ic('bulb',20)}Tipp <small>${CUR.hints}/${hl.length}</small></button>`:''}${CUR.tries>=2?'<button class="btn" data-act="solution">Lösung</button>':''}<button class="btn primary grow big-btn" data-act="check">Prüfen</button>`;
}
function renderTask(){
  const x=CUR.x,t=CUR.t,n=SES.ids.length,i=SES.i;
  const tn=TYPES[x.typ][1];let body='';
  const stdin=x.typ==='predict'?(x.stdin||[]):[];
  if(x.typ==='predict'){
    body=`${codeBlock(x.code)}${stdin.length?`<div class="meta">Eingabe(n): ${stdin.map(v=>'<code>'+esc(v)+'</code>').join(' · ')}</div>`:''}<label for="ans">Was gibt das Programm aus? (jede Zeile genau so, wie sie erscheint)</label><textarea id="ans" class="ansin" rows="4" spellcheck="false" autocapitalize="off" autocorrect="off"></textarea>`;
  }else if(x.typ==='gap'){
    const parts=x.code.split('___');let h='';
    parts.forEach((p,k)=>{h+=esc(p);if(k<parts.length-1)h+=`<input class="gap" id="g${k}" size="${Math.max(5,(x.ans[k]||'').length+3)}" spellcheck="false" autocapitalize="off" autocorrect="off" autocomplete="off" aria-label="Lücke ${k+1}">`;});
    body=`<pre class="code gapcode">${h}</pre><div id="expbox"></div>`;
  }else if(x.typ==='puzzle'){
    body=`<div id="pzbox"></div><div id="expbox"></div>`;
  }else{
    const rows=Math.max(8,(x.typ==='bug'?x.code:x.start||'').split('\n').length+3);
    body=`${edHtml('ed',x.typ==='bug'?x.code:(x.start||''),rows)}${x.append?`<div class="meta" style="margin-top:10px">Nach deinem Code wird automatisch ausgeführt:</div>${codeBlock(x.append)}`:''}<div id="expbox"></div><div class="actions"><button class="btn small" data-act="try">${ic('play',14)}Ausprobieren</button></div><div id="tryout"></div>`;
  }
  setView(`<div class="tasktop"><button class="roundbtn" data-act="quit" aria-label="Runde beenden">${ic('x',20)}</button><div class="pw">${bar(i/n)}<small>Aufgabe ${i+1} von ${n}</small></div></div>
  <div class="task"><div class="chips"><span class="chip">${ic(TICON[x.typ],14)}${tn}</span><span class="chip">Stufe ${t.lvl}</span><span class="chip g">${t.kap} · ${esc(KAPBY[t.kap].name)}</span></div>
  ${(x.typ==='bug'||x.typ==='predict')?'':`<h2 class="h2" style="margin-top:2px">${esc(t.titel)}</h2>`}
  <div class="q">${md(x.text||(x.typ==='predict'?'Lies den Code genau. Was gibt dieses Programm aus?':''))}</div>
  ${body}
  ${TASKLESSON[t.id]?`<details class="nl" id="nl"><summary>${ic('book',16)} Nachlesen: ${esc(LESSONBY[TASKLESSON[t.id]].titel)}${lessonRead(USER,TASKLESSON[t.id])?'':' <small>(noch nicht gelesen)</small>'}</summary><div id="nlbody"></div></details>`:''}
  <div id="tips"></div><div id="fb"></div><p class="meta foot" id="pystat">Python wird geladen …</p></div>
  <div class="stickbar"><div class="stickin" id="btns"></div></div>`);
  renderBtns();
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
  CUR.busy=false;$('#fb')&&($('#fb').innerHTML='');
  CUR.tries++;
  if(res.ok)finishTask(CUR.tries===1?1:0.5,res);else{renderBtns();wrong(res);}
}
function say(kind,html){const el=$('#fb');if(el)el.innerHTML=`<div class="fb ${kind}">${html}</div>`;}
function wrong(res){
  const x=CUR.x;let sub='',det='';
  if(res.msg)sub=esc(res.msg);
  else if(res.needMsg)sub='Die Ausgabe stimmt, aber: '+esc(res.needMsg);
  else if(res.predict){
    const a=norm(res.predict.got).split('\n'),b=norm(res.predict.exp).split('\n');
    sub=a.length!==b.length?`Deine Antwort hat ${a.length} Zeile(n), die Ausgabe hat eine andere Zeilenzahl.`:'Die Zeilenzahl passt – prüfe jede Zeile genau (Leerzeichen, Groß-/Kleinschreibung, Zahlen).';
    if(CUR.tries>=2)det=`<div class="box"><b class="l">Die richtige Ausgabe wäre</b><pre class="out">${esc(res.predict.exp)}</pre></div>`;
  }else if(res.err){
    sub=esc(deErr(res.err));
  }else{
    sub='Die Ausgabe passt noch nicht – fast!';
    const tl=res.input||[];
    det=`<div class="cmp"><div class="box"><b class="l">Erwartet${tl.length?' (Eingabe '+tl.map(v=>esc(v)).join(' · ')+')':''}</b><pre class="out">${esc(res.exp)||' '}</pre></div><div class="box"><b class="l">Dein Programm gibt aus</b><pre class="out">${esc(res.got)||'(nichts)'}</pre></div></div>`;
  }
  const hl=CUR.x.hints||[];
  openSheet('no',`<div class="sheethead"><span class="sheeticon">${ic('x',24)}</span><div><div class="sheettitle">Noch nicht ganz</div><div class="sheetsub">${sub}</div></div></div><div class="sheetbody">${det}</div>`,
    `${CUR.hints<hl.length?`<button class="btn" data-act="sheethint">${ic('bulb',20)}Tipp</button>`:''}${CUR.tries>=2?'<button class="btn" data-act="solution">Lösung zeigen</button>':''}<button class="btn primary grow big-btn" data-act="sheetclose">Nochmal versuchen</button>`);
}
function doHint(){
  if(!CUR||CUR.done)return;const hl=CUR.x.hints||[];
  if(CUR.hints<hl.length){const h=hl[CUR.hints];CUR.hints++;$('#tips').insertAdjacentHTML('beforeend',`<div class="tip">${ic('bulb',18)} ${md(h)}</div>`);renderBtns();}
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
    let body='';
    if(x.typ==='predict')body+=`<div class="box"><b class="l">Das Programm gibt aus</b><pre class="out">${esc(exp[0].out)}</pre></div>`;
    else if(!ok||x.typ==='code'||x.typ==='bug')body+=`<details ${ok?'':'open'}><summary>${ok?'Musterlösung ansehen':'Lösung'}</summary><pre class="code">${esc(refCode(x))}</pre></details>`;
    if(x.expl)body+=`<div class="tip">${md(x.expl)}</div>`;
    const last=SES.i>=SES.ids.length-1;
    const head=ok?`<div class="sheethead"><span class="sheeticon">${ic('check',24)}</span><div><div class="sheettitle">${score>=1?'Richtig – gleich beim ersten Mal!':'Richtig!'}</div></div><span class="pts">${score>=1?'+1 Punkt':'+½ Punkt'}</span></div>`
      :`<div class="sheethead"><span class="sheeticon">${ic('bulb',24)}</span><div><div class="sheettitle">Hier die Lösung</div><div class="sheetsub">Zählt diesmal nicht – versuche es später noch einmal.</div></div></div>`;
    renderBtns();
    $$('#app textarea,#app input.gap').forEach(e=>{e.readOnly=true;});
    openSheet(ok?'ok':'no',head+`<div class="sheetbody">${body}</div>`,`<button class="btn primary grow big-btn" data-act="next">${last?'Fertig':'Weiter'}</button>`);
  })();
}
function nextTask(){SES.i++;if(SES.i>=SES.ids.length)return viewSummary();showTask();}
function viewSummary(){
  const pts=SES.res.reduce((a,r)=>a+r.score,0),n=SES.res.length;
  USER.log.push({t:Date.now(),kap:SES.ids.length?TASKBY[SES.ids[0]].kap:0,n,pts,secs:Math.round((Date.now()-SES.t0)/1000)});
  if(USER.log.length>300)USER.log=USER.log.slice(-300);persist();
  const pct=n?pts/n:0,k=todayKey(),goal=goalOf(USER),st=streakOf(USER),secs=Math.round((Date.now()-SES.t0)/60000);
  setView(`<div class="done"><svg class="medal" width="112" height="112" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="56" fill="var(--pri-t)"/><path d="M60 22l10.5 21.3 23.5 3.4-17 16.6 4 23.4L60 75.6 39 86.7l4-23.4-17-16.6 23.5-3.4z" fill="#FFC83D" stroke="#B88A00" stroke-width="3" stroke-linejoin="round"/><circle cx="60" cy="58" r="9" fill="#FFF4D1"/></svg>
  <h2 class="h2" style="font-size:30px;margin:0">Runde geschafft!</h2><p class="meta">${n} Aufgaben · ${Math.max(1,secs)} Min.</p></div>
  <div class="panel" style="text-align:center"><div class="big">${String(Math.round(pts*10)/10).replace('.',',')} <small>von ${n} Punkten</small></div>${bar(pct)}
   <div class="two">${st?`<div class="y">${ic('flame',18)}${st} ${st===1?'Tag':'Tage'} in Folge</div>`:''}<div class="b">${(USER.days[k]||0)>=goal?'Tagesziel erreicht':`Tagesziel: ${USER.days[k]||0} von ${goal}`}</div></div></div>
  <div class="panel">${SES.res.map(r=>{const t=TASKBY[r.id];return `<div class="sk"><span>${ic(TICON[t.typ],16)}${esc(t.titel)}</span><span class="stat" style="color:${r.score>0?'var(--ok)':'var(--no)'}">${r.score>=1?'beim 1. Versuch ✓':r.score>0?'nach 2 Versuchen ✓':'noch üben ✗'}</span></div>`;}).join('')}</div>
  <p class="meta">Ganze Punkte gibt es für richtige Lösungen im ersten Versuch, halbe für richtige Lösungen nach einem Fehlversuch.</p>
  <div class="stickbar"><div class="stickin"><button class="btn" data-act="home">Fertig</button><button class="btn primary grow big-btn" data-act="again">Noch eine Runde</button></div></div>`);
  SES.again=SES.lastScope;
}
/* ---------- Spielwiese ---------- */
function viewPlay(){
  let code='print("Hallo Welt")';try{code=localStorage.getItem(LS_KEY+'-play')||code;}catch(e){}
  setView(`${header(USER)}<h2 class="h2">Spielwiese</h2><p class="meta">Probiere hier frei Python aus. Wenn dein Programm <code>input()</code> benutzt, schreibe die Eingaben unten hinein (eine pro Zeile).</p>
  ${edHtml('pg',code,12)}
  <label for="pgin">Eingaben für input() (eine pro Zeile)</label><textarea id="pgin" class="ansin" rows="2" spellcheck="false"></textarea>
  <div class="actions"><button class="btn primary" data-act="pgrun">${ic('play',16)}Ausführen</button></div><div id="pgout"></div><p class="meta foot" id="pystat">Python wird geladen …</p>`,'play');
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
  setView(`<div class="top"><span class="logo">${ic('code',22)}</span><div class="ttl">Eltern-Bereich<small>Auswertung je Kind</small></div></div><button class="back" data-act="${USER?'home':'start'}">${ic('chevL',18)}Zurück</button>
  ${names.map(n=>{const u=DB.users[n],w=lastDays(u,7),k=todayKey();return `<div class="panel"><h3>${esc(u.avatar)} ${esc(n)}</h3><div class="meta">Heute: ${u.days[k]||0} Aufgaben · ${mins(u.dtime[k])} Min. · letzte 7 Tage: ${mins(w.reduce((a,d)=>a+d.s,0))} Min., ${w.reduce((a,d)=>a+d.n,0)} Aufgaben · ${streakOf(u)} Tage in Folge</div><div class="actions"><button class="btn small" data-act="pchild" data-n="${esc(n)}">Auswertung</button></div></div>`;}).join('')||'<p class="meta">Noch niemand angelegt.</p>'}`);
}
function viewParentChild(n){
  const u=DB.users[n];if(!u)return viewParents();
  const w=lastDays(u,14),mx=Math.max(60,...w.map(d=>d.s));
  const weak=TASKS.filter(t=>isWeak(u,t.id));
  setView(`<div class="top"><span class="logo">${ic('code',22)}</span><div class="ttl">${esc(u.avatar)} ${esc(n)}<small>Auswertung</small></div></div><button class="back" data-act="parents">${ic('chevL',18)}Zurück</button>
  <div class="panel"><h3>Kapitel</h3>${KAPITEL.map(c=>`<div class="sk"><span>${c.id}. ${esc(c.name)}</span><span>${kapDone(u,c.id)}/${tasksOf(c.id).length} sitzen · ${kapLessonsRead(u,c.id)}/${lessonsOf(c.id).length} Erklärungen</span></div>${bar(kapMastery(u,c.id))}`).join('')}</div>
  <div class="panel"><h3>Übungszeit (14 Tage, Minuten)</h3><div class="days">${w.map(d=>`<div class="d"><small>${mins(d.s)}</small><i style="height:${Math.round(d.s/mx*60)}px"></i><small>${d.d.getDate()}.</small></div>`).join('')}</div></div>
  <div class="panel"><h3>Hier lohnt sich Nachfragen</h3>${weak.length?weak.map(t=>{const p=u.tasks[t.id];return `<div class="sk"><span>${ic(TICON[t.typ],16)}${esc(t.titel)} <small>(Kap. ${t.kap})</small></span><span>${p.r} richtig · ${p.w} falsch</span></div>`;}).join(''):'<p class="meta">Keine auffälligen Aufgaben.</p>'}</div>
  <div class="panel"><h3>Letzte Runden</h3>${u.log.slice(-8).reverse().map(l=>`<div class="sk"><span>${fmtDate(l.t)} · ${l.n} Aufgaben</span><span>${l.pts} Punkte</span></div>`).join('')||'<p class="meta">Noch keine Runde.</p>'}</div>
  <div class="panel"><h3>Kind löschen</h3><p class="meta">Löscht den Lernstand auf allen Geräten. Zur Bestätigung den Namen eintippen.</p><input id="delname" autocomplete="off" placeholder="${esc(n)}" aria-label="Name zur Bestätigung"><div class="actions"><button class="btn danger" data-act="pdel" data-n="${esc(n)}">Endgültig löschen</button></div></div>`);
}
/* ---------- Aktionen ---------- */
let AVSEL=AVATARS[0];
function runScope(kind,k){
  const u=USER,len=u.settings.len;let tasks;
  if(kind==='weak')tasks=TASKS.filter(t=>isWeak(u,t.id)||isDue(u,t.id)).sort(()=>Math.random()-0.5).slice(0,len);
  else tasks=pickTasks(u,kind==='kap'?[k]:KAPITEL.map(c=>c.id).filter(id=>kapOpen(u,id)),len);
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
    case 'practice':viewPractice();break;
    case 'len':USER.settings.len=+el.dataset.v;touch(USER);persist();viewPractice();break;
    case 'goal':USER.settings.goal=+el.dataset.v;touch(USER);persist();viewPractice();break;
    case 'kap':viewKap(+el.dataset.k);break;
    case 'lesson':viewLesson(el.dataset.l);break;
    case 'lq':answerQuiz(el);break;
    case 'exrun':{const id=el.dataset.id,b=LEX[id],out=$('#'+id+'-out');out.innerHTML='<div class="fb tip">Läuft …</div>';bumpTime(USER);
      const r=await pyRun($('#'+id).value,b.in,{echo:true});out.innerHTML=outHtml(r);break;}
    case 'exreset':{const id=el.dataset.id,ta=$('#'+id);ta.value=LEX[id].code;ta.dispatchEvent(new Event('input'));$('#'+id+'-out').innerHTML='';break;}
    case 'ldone':{const l=LESSONBY[el.dataset.l];markRead(USER,l.id,0,0);persist();const list=lessonsOf(l.kap),next=list[list.findIndex(x=>x.id===l.id)+1];if(next)viewLesson(next.id);else viewKap(l.kap);break;}
    case 'ltrain':{const l=LESSONBY[el.dataset.l];markRead(USER,l.id,0,0);persist();startSession(l.tasks.map(id=>TASKBY[id]).sort(()=>Math.random()-0.5).slice(0,USER.settings.len));break;}
    case 'nlread':{const id=el.dataset.l;markRead(USER,id,0,0);persist();el.outerHTML='<span class="meta">✓ als gelesen gespeichert</span>';break;}
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
      const r=await pyRun(withApp(CUR.x,code),testsOf(CUR.x)[0],{});$('#tryout').innerHTML=outHtml(r);break;}
    case 'sym':{const s=SYMBY(+el.dataset.i);insertAt($('#'+el.dataset.ed),s[1],s[2]||0);break;}
    case 'check':doCheck();break;
    case 'hint':doHint();break;
    case 'sheethint':closeSheet();doHint();break;
    case 'sheetclose':closeSheet();break;
    case 'solution':closeSheet();showSolution();break;
    case 'next':closeSheet();nextTask();break;
    case 'quit':if(confirm('Runde beenden? Bisherige Ergebnisse bleiben gespeichert.')){if(SES.res.length)viewSummary();else viewHome();}break;
    case 'pz-add':{const k=+el.dataset.i;CUR.pz.chosen.push(CUR.pz.pool.splice(k,1)[0]);renderPz();break;}
    case 'pz-del':{const k=+el.dataset.i;CUR.pz.pool.push(CUR.pz.chosen.splice(k,1)[0]);renderPz();break;}
    case 'parents':viewParents();break;
    case 'pchild':viewParentChild(el.dataset.n);break;
    case 'pdel':{const n=el.dataset.n;if($('#delname').value.trim()!==n){alert('Name stimmt nicht überein.');return;}deleteUser(n);if(USER&&USER.name===n)USER=null;viewParents();break;}
    default:if(/^kap-\d+$/.test(a))viewKap(+a.slice(4));
  }
});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeSheet();if((e.key==='Enter'||e.key===' ')&&e.target&&e.target.classList&&e.target.classList.contains('side-user')){e.preventDefault();viewStart();}});
document.addEventListener('toggle',e=>{
  const d=e.target;if(!d||d.id!=='nl'||!d.open||!CUR)return;const body=$('#nlbody');if(!body||body.dataset.on)return;body.dataset.on='1';
  const l=LESSONBY[TASKLESSON[CUR.t.id]];pyStart();
  body.innerHTML=`<div class="lesson">${lessonHtml(l,'nl')}</div><div class="actions"><button class="btn small" data-act="nlread" data-l="${l.id}">Habe ich gelesen</button></div>`;wireLesson(l,'nl');
},true);
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
