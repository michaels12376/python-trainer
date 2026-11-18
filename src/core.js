/* ===== Kern: Speicher, Nutzer, Zusammenführen, Lernlogik ===== */
'use strict';
const LS_KEY='python-trainer-v1';
const DAY=86400000;
const INTERVALS=[0,1,2,4,8,16,32];
const AVATARS=['🐍','🦉','🦊','🐼','🦁','🐯','🐸','🦄','🐙','🚀','⚽','🎸'];
const TASKBY={};TASKS.forEach(t=>TASKBY[t.id]=t);
const KAPBY={};KAPITEL.forEach(k=>KAPBY[k.id]=k);
const TYPES={predict:['🔮','Ausgabe vorhersagen'],gap:['🧩','Lückencode'],bug:['🐞','Fehler finden'],puzzle:['🧱','Zeilen ordnen'],code:['⌨️','Programmieren']};
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $=(s,r)=>(r||document).querySelector(s);
const $$=(s,r)=>Array.from((r||document).querySelectorAll(s));
const rnd=n=>Math.floor(Math.random()*n);
const pick=a=>a[rnd(a.length)];
function todayKey(t){const d=new Date(t||Date.now());return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function fmtDate(t){const d=new Date(t);return d.getDate()+'.'+(d.getMonth()+1)+'.'+String(d.getFullYear()).slice(2);}
const tasksOf=k=>TASKS.filter(t=>t.kap===k);
/* ---------- Speicher ---------- */
let DB={v:1,updated:0,last:null,users:{},deleted:{}};
let STORAGE_OK=true,SERVER=false,syncTimer=null,syncStatus='lokal';
function loadLocal(){try{const s=localStorage.getItem(LS_KEY);if(s){const d=JSON.parse(s);if(d&&d.users)DB=d;for(const n in DB.users)migrateUser(DB.users[n]);}}catch(e){STORAGE_OK=false;}}
function saveLocal(){try{localStorage.setItem(LS_KEY,JSON.stringify(DB));STORAGE_OK=true;}catch(e){STORAGE_OK=false;}}
function touch(u){const t=Date.now();DB.updated=t;if(u)u.updated=t;}
function persist(){saveLocal();if(SERVER){clearTimeout(syncTimer);syncTimer=setTimeout(pushServer,600);}}
async function pushServer(){
  try{
    try{const r0=await fetch('api/state',{cache:'no-store'});if(r0.ok){const rs=await r0.json();if(rs&&rs.users)mergeIntoLocal(rs);}}catch(e){}
    const r=await fetch('api/state',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(DB)});
    syncStatus=r.ok?'Server ✓':'Server-Fehler';
  }catch(e){syncStatus='offline (lokal)';}
  const el=$('#syncstat');if(el)el.textContent=syncStatus;
}
async function initServer(){
  try{const r=await fetch('api/state',{cache:'no-store'});if(r.ok){const rs=await r.json();SERVER=true;if(rs&&rs.users)mergeIntoLocal(rs);syncStatus='Server ✓';}}catch(e){}
}
function mergeIntoLocal(remote){
  const cur=(typeof USER!=='undefined'&&USER)?USER.name:null;
  DB=mergeDB(DB,remote);for(const n in DB.users)migrateUser(DB.users[n]);
  if(cur){if(DB.users[cur])USER=DB.users[cur];else USER=null;}
  saveLocal();
}
const getLast=()=>{try{return localStorage.getItem(LS_KEY+'-last');}catch(e){return null;}};
const setLast=n=>{try{if(n)localStorage.setItem(LS_KEY+'-last',n);else localStorage.removeItem(LS_KEY+'-last');}catch(e){}};
/* Zusammenführen: nichts geht verloren (Aufgabenstände einzeln nach „zuletzt geübt“, Zähler jeweils das Maximum) */
const lastOf=p=>(p&&p.last)||0;
function mergeMap(x,y,f){const o=Object.assign({},x||{});for(const[k,v]of Object.entries(y||{})){o[k]=k in o?f(o[k],v):v;}return o;}
function mergeUser(x,y){
  if(!x)return y;if(!y)return x;
  const rx=x.resetAt||0,ry=y.resetAt||0;
  if(rx!==ry){const w=rx>ry?x:y,l=w===x?y:x;if((l.updated||0)<=Math.max(rx,ry))return w;}
  const newer=(x.updated||0)>=(y.updated||0)?x:y,older=newer===x?y:x;
  const out=Object.assign({},older,newer);
  out.settings=Object.assign({},older.settings||{},newer.settings||{});
  out.created=Math.min(x.created||Infinity,y.created||Infinity);if(!isFinite(out.created))out.created=newer.created;
  out.updated=Math.max(x.updated||0,y.updated||0);
  out.tasks=mergeMap(x.tasks,y.tasks,(a,b)=>lastOf(a)>=lastOf(b)?a:b);
  out.days=mergeMap(x.days,y.days,Math.max);out.dtime=mergeMap(x.dtime,y.dtime,Math.max);out.dright=mergeMap(x.dright,y.dright,Math.max);
  const seen=new Set(),log=[];
  for(const l of[].concat(x.log||[],y.log||[]).sort((p,q)=>p.t-q.t)){const k=l.t+'|'+l.kap;if(seen.has(k))continue;seen.add(k);log.push(l);}
  out.log=log.slice(-300);
  return out;
}
const isGone=(del,n,u)=>{const t=(del||{})[n];return !!t&&!!u&&(u.created||0)<=t;};
function mergeDB(a,b){
  const del=mergeMap(a.deleted,b.deleted,Math.max);
  const out={v:1,updated:Math.max(a.updated||0,b.updated||0),last:b.last||a.last,users:{},deleted:del};
  for(const n of new Set([...Object.keys(a.users||{}),...Object.keys(b.users||{})])){
    const ua=isGone(del,n,(a.users||{})[n])?null:(a.users||{})[n],ub=isGone(del,n,(b.users||{})[n])?null:(b.users||{})[n];
    if(ua||ub)out.users[n]=mergeUser(ua,ub);
  }
  if(out.last&&!out.users[out.last])out.last=null;
  return out;
}
function migrateUser(u){
  if(!u)return u;u.settings=u.settings||{};
  if(u.settings.len==null)u.settings.len=10;
  ['tasks','days','dtime','dright'].forEach(k=>{if(!u[k])u[k]={};});
  if(!u.log)u.log=[];
  return u;
}
function newUser(name,avatar){const t=Date.now();return migrateUser({name,avatar,created:t,updated:t,settings:{len:10}});}
function deleteUser(name){DB.deleted[name]=Date.now();delete DB.users[name];if(DB.last===name)DB.last=null;DB.updated=Date.now();persist();}
/* ---------- Aktive Zeit, Zähler ---------- */
let lastAct=0;
function bumpTime(u){const t=Date.now();if(lastAct&&t-lastAct<120000){const k=todayKey();u.dtime[k]=(u.dtime[k]||0)+Math.round((t-lastAct)/1000);}lastAct=t;}
function bumpDay(u,right){const k=todayKey();u.days[k]=(u.days[k]||0)+1;if(right)u.dright[k]=(u.dright[k]||0)+1;}
/* ---------- Lernstand je Aufgabe (Leitner) ---------- */
const taskState=(u,id)=>u.tasks[id]||(u.tasks[id]={box:0,r:0,w:0,last:0,due:0});
/* score: 1 = auf Anhieb richtig, 0.5 = nach Fehlversuch richtig, 0 = falsch / Lösung angesehen */
function recordAnswer(u,id,score){
  const p=taskState(u,id),now=Date.now();p.last=now;
  if(score>=1){p.r++;p.box=Math.min(6,p.box+1);}
  else if(score>0){p.r++;}
  else{p.w++;p.box=Math.max(0,p.box-1);}
  p.due=now+INTERVALS[p.box]*DAY;
  bumpTime(u);bumpDay(u,score>=1);touch(u);
}
const taskMastery=(u,id)=>{const p=u.tasks[id];return p&&(p.r+p.w)?Math.min(1,p.box/4):0;};
const kapMastery=(u,k)=>{const t=tasksOf(k);return t.reduce((a,x)=>a+taskMastery(u,x.id),0)/(t.length||1);};
const kapDone=(u,k)=>tasksOf(k).filter(t=>(u.tasks[t.id]||{box:0}).box>=3).length;
const kapSolved=(u,k)=>tasksOf(k).filter(t=>(u.tasks[t.id]||{box:0}).box>=1).length;
/* Kapitel gelten für die gemischte Runde als „dran“, wenn das vorige geschafft ist (oder man darin schon geübt hat); antippen kann man jedes */
const kapOpen=(u,k)=>k===1||kapSolved(u,k-1)>=6||tasksOf(k).some(t=>u.tasks[t.id]&&(u.tasks[t.id].r+u.tasks[t.id].w)>0);
const isWeak=(u,id)=>{const p=u.tasks[id];return !!p&&p.w>0&&p.w>=p.r;};
const isDue=(u,id)=>{const p=u.tasks[id];return !!p&&p.due&&p.due<=Date.now()&&(p.r+p.w)>0;};
/* Schwierigkeitsstufen schalten sich frei: Stufe 2 nach 3 gelösten Aufgaben der Stufe 1 im Kapitel, Stufe 3 nach 3 der Stufe 2 */
function lvlOpen(u,k,lvl){
  if(lvl<=1)return true;
  const prev=tasksOf(k).filter(t=>t.lvl===lvl-1),total=prev.length;
  const solved=prev.filter(t=>(u.tasks[t.id]||{box:0}).box>=1).length;
  return solved>=Math.min(3,total);
}
/* Auswahl für eine Übungsrunde: fällige/schwache zuerst, dann neue Aufgaben (freigeschaltete Stufen), dann Wiederholung; Typen gemischt */
function pickTasks(u,kaps,n){
  const now=Date.now(),pool=TASKS.filter(t=>kaps.includes(t.kap));
  const w=t=>{
    const p=u.tasks[t.id];
    if(!p||!(p.r+p.w)){return lvlOpen(u,t.kap,t.lvl)?(t.lvl===1?3:t.lvl===2?2.4:2):0.15;}
    let x=0.4+(6-p.box)*0.25;if(p.due&&p.due<=now)x+=2;if(p.w>=p.r)x+=1.2;return x;
  };
  const out=[],rest=pool.slice();let lastTyp=null;
  while(out.length<n&&rest.length){
    const ws=rest.map(t=>w(t)*(t.typ===lastTyp?0.4:1));
    let tot=ws.reduce((a,b)=>a+b,0),r=Math.random()*tot,i=0;
    for(;i<rest.length-1;i++){r-=ws[i];if(r<=0)break;}
    const t=rest.splice(i,1)[0];out.push(t);lastTyp=t.typ;
  }
  return out;
}
