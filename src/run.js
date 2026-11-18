/* ===== Python im Browser (Pyodide im Web Worker; Endlosschleifen werden nach 5 s abgebrochen) ===== */
'use strict';
const PY={worker:null,ready:null,seq:0,pending:{},failed:false};
const PY_PROG=`
import sys, io, builtins
class _Out:
    def __init__(s): s.p=[]; s.n=0
    def write(s,t):
        s.n+=len(t)
        if s.n>20000: raise RuntimeError("Zu viel Ausgabe")
        s.p.append(t); return len(t)
    def flush(s): pass
    def getvalue(s): return "".join(s.p)
def _run(code, lines, echo):
    out=_Out(); it=iter(lines)
    def _input(prompt=""):
        if echo: out.write(str(prompt))
        try: v=next(it)
        except StopIteration: raise EOFError("Das Programm wollte noch etwas einlesen, aber es gab keine weitere Eingabe.")
        if echo: out.write(v+"\\n")
        return v
    g={"__name__":"__main__","input":_input}
    so=sys.stdout; sys.stdout=out; err=None
    try:
        exec(compile(code,"<dein Code>","exec"),g)
    except BaseException as e:
        line=None; tb=e.__traceback__
        while tb:
            if tb.tb_frame.f_code.co_filename=="<dein Code>": line=tb.tb_lineno
            tb=tb.tb_next
        if isinstance(e,SyntaxError): line=e.lineno
        msg=e.msg if isinstance(e,SyntaxError) else str(e)
        err=[type(e).__name__,msg,line]
    finally: sys.stdout=so
    return [out.getvalue(),err]
`;
const PY_WORKER=`
let py=null;
async function init(base){
  importScripts(base+'pyodide.js');
  py=await loadPyodide({indexURL:base});
  py.runPython(${JSON.stringify(PY_PROG)});
  postMessage({t:'ready'});
}
onmessage=async e=>{
  const d=e.data;
  if(d.t==='init'){try{await init(d.base);}catch(x){postMessage({t:'fail',m:String(x)});}return;}
  try{
    const fn=py.globals.get('_run');
    const lst=py.toPy(d.stdin||[]);
    const res=fn(d.code,lst,!!d.echo);
    const r=res.toJs();res.destroy();lst.destroy();fn.destroy();
    postMessage({t:'res',id:d.id,out:r[0],err:r[1]||null});
  }catch(x){postMessage({t:'res',id:d.id,out:'',err:['InternalError',String(x),null]});}
};`;
function pyStart(){
  if(PY.ready)return PY.ready;
  PY.failed=false;
  PY.ready=new Promise(res=>{
    try{
      const w=new Worker(URL.createObjectURL(new Blob([PY_WORKER],{type:'text/javascript'})));
      PY.worker=w;
      w.onmessage=e=>{
        const d=e.data;
        if(d.t==='ready')res(true);
        else if(d.t==='fail'){PY.failed=true;res(false);}
        else if(d.t==='res'){const p=PY.pending[d.id];if(p){delete PY.pending[d.id];clearTimeout(p.timer);p.resolve({out:d.out,err:d.err,timeout:false});}}
      };
      w.onerror=()=>{PY.failed=true;res(false);};
      w.postMessage({t:'init',base:new URL('pyodide/',document.baseURI).href});
    }catch(x){PY.failed=true;res(false);}
  });
  return PY.ready;
}
function pyKill(){
  if(PY.worker)PY.worker.terminate();
  PY.worker=null;PY.ready=null;
  for(const id in PY.pending){clearTimeout(PY.pending[id].timer);PY.pending[id].resolve({out:'',err:['Timeout','Das Programm läuft zu lange (Endlosschleife?).',null],timeout:true});}
  PY.pending={};
}
/* Führt Code aus. Ergebnis: {out, err:[Typ,Meldung,Zeile]|null, timeout} */
async function pyRun(code,stdin,opt){
  opt=opt||{};
  const ok=await pyStart();
  if(!ok)return {out:'',err:['InternalError','Python konnte nicht geladen werden.',null],timeout:false,failed:true};
  const id=++PY.seq;
  return new Promise(resolve=>{
    const timer=setTimeout(()=>{if(PY.pending[id]){const p=PY.pending[id];delete PY.pending[id];pyKill();p.resolve({out:'',err:['Timeout','Das Programm läuft zu lange – vielleicht hast du eine Endlosschleife gebaut.',null],timeout:true});pyStart();}},opt.timeout||5000);
    PY.pending[id]={resolve,timer};
    PY.worker.postMessage({id,code,stdin:stdin||[],echo:!!opt.echo});
  });
}
/* Verständliche deutsche Fehlermeldung */
function deErr(e){
  if(!e)return '';
  const [typ,msg,line]=e,at=line?` (Zeile ${line})`:'';
  let m;
  switch(typ){
    case 'IndentationError':m='Einrückungsfehler: Die Zeile ist falsch eingerückt. Alles, was zu if, for oder while gehört, wird mit 4 Leerzeichen eingerückt.';break;
    case 'SyntaxError':
      if(/expected ':'|invalid syntax/.test(msg)&&/Perhaps you forgot a comma/.test(msg))m='Syntaxfehler: Zwischen zwei Teilen fehlt ein Komma oder ein +.';
      else if(/was never closed|unterminated|unclosed/i.test(msg))m='Syntaxfehler: Eine Klammer oder ein Anführungszeichen wurde nicht geschlossen.';
      else if(/expected ':'/.test(msg))m='Syntaxfehler: Nach der Bedingung bzw. dem Schleifenkopf fehlt ein Doppelpunkt.';
      else if(/cannot assign|Maybe you meant '=='/.test(msg))m='Syntaxfehler: Zum Vergleichen braucht man zwei Gleichheitszeichen (==).';
      else m='Syntaxfehler: Der Code ist so nicht erlaubt. Prüfe Doppelpunkte, Klammern und Anführungszeichen.';break;
    case 'NameError':{const n=(/name '(.+?)'/.exec(msg)||[])[1];m=n?`NameError: „${n}“ kennt Python nicht. Hast du den Namen vorher angelegt oder falsch geschrieben (Groß-/Kleinschreibung)?`:'NameError: Python kennt einen Namen nicht.';break;}
    case 'TypeError':m='TypeError: Das passt nicht zusammen – zum Beispiel Text und Zahl mit + verbinden. Wandle mit int(), float() oder str() um. ('+msg+')';break;
    case 'ValueError':m='ValueError: Der Wert passt nicht, z. B. wurde aus Text keine Zahl. ('+msg+')';break;
    case 'ZeroDivisionError':m='ZeroDivisionError: Durch 0 kann man nicht teilen.';break;
    case 'EOFError':m=msg;break;
    case 'Timeout':return msg;
    case 'RuntimeError':m=msg;break;
    default:m=typ+': '+msg;
  }
  return m+at;
}
