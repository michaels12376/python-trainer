// Syntaxprüfung der JS-Quellen (läuft in node):  node tools/check_syntax.js
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=path.join(__dirname,'..','src');let bad=0,n=0;
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.js'))){n++;try{new vm.Script(fs.readFileSync(path.join(dir,f),'utf8'),{filename:f});}catch(e){bad++;console.log('FEHLER',f,e.message);}}
console.log('Skripte:',n,'Fehler:',bad);process.exit(bad?1:0);
