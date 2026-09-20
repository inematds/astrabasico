from pathlib import Path
import json,html,shutil
P=Path(__file__).resolve().parents[1]/'video';D=json.loads((P.parent/'docs/lesson-pt.json').read_text())
E=html.escape
css='''@font-face{font-family:Display;src:url('display.ttf')}@font-face{font-family:Data;src:url('mono.ttf')}
*{box-sizing:border-box}html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#171b20}#root{width:100%;height:100%;color:#f7f1e7;font-family:Data,monospace}.clip{position:absolute;inset:0}.scene-shell{height:100%;padding:64px 72px;background:#171b20;position:relative}.topline{display:flex;justify-content:space-between;align-items:center;font-size:24px;letter-spacing:2px;color:#efbe69;border-bottom:2px solid #4f5860;padding-bottom:20px}.layout{display:grid;grid-template-columns:1250px 450px;gap:76px;margin-top:40px}.main-title{font-family:Display,sans-serif;font-size:70px;line-height:1.13;letter-spacing:-2px;margin:0 0 35px;min-height:160px;max-width:1230px}.visual{min-height:430px;display:flex;flex-direction:column;justify-content:center;gap:18px}.node{background:#232a31;border:2px solid #56616c;border-radius:14px;padding:23px 28px;color:#f7f1e7;font-size:31px;line-height:1.3;white-space:pre-line;position:relative}.node b{color:#efbe69;font-weight:400;display:inline-block;min-width:62px}.nodes-flow{display:grid;grid-template-columns:1fr 1fr;gap:22px}.flow-node{min-height:140px;display:flex;align-items:center}.compare-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.compare-grid .node{min-height:300px;padding:35px 24px;display:flex;align-items:center;line-height:1.6;font-size:31px;border-top:6px solid #efbe69}.avatar-panel{margin-top:15px}.avatar-panel img{display:block;width:450px;height:254px;object-fit:cover;border-radius:18px;border:2px solid #56616c}.avatar-name{font-family:Display,sans-serif;font-size:36px;margin:24px 0 12px}.avatar-desc{color:#c5cbd0;font-size:24px;line-height:1.65}.badge{border:2px solid #efbe69;color:#efbe69;font-size:23px;padding:16px;margin-top:28px;line-height:1.5}.takeaway{position:absolute;left:72px;right:72px;bottom:140px;border-top:2px solid #56616c;padding-top:22px;font-size:30px;line-height:1.45;max-width:1776px;color:#efbe69}.footer{position:absolute;bottom:56px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:23px;color:#c5cbd0}.progress-track{position:absolute;left:0;right:0;bottom:0;height:8px;background:#303942}.progress-fill{height:8px;width:100%;background:#efbe69;transform-origin:left center}.bar-row{display:grid;grid-template-columns:390px 1fr;gap:20px;align-items:center;font-size:30px;margin:16px 0}.bar-track{height:54px;background:#303942;border-radius:4px;overflow:hidden}.bar-fill{height:100%;background:#efbe69;transform-origin:left}.threshold-number{font-family:Display,sans-serif;font-size:100px;color:#efbe69;margin:0}.threshold-rule{height:24px;background:#4f5860;position:relative;margin:35px 0}.threshold-rule:after{content:'';position:absolute;left:65%;top:-20px;width:5px;height:64px;background:#efbe69}.terminal{background:#101419;border:2px solid #56616c;border-radius:18px;padding:35px}.terminal .node{border:0;background:none;font-size:34px;padding:22px 10px}.cost-total{font-family:Display,sans-serif;font-size:78px;color:#efbe69;margin:12px 0}.stack .node{border-left:8px solid #efbe69}.scene-note{font-size:24px;color:#c5cbd0;margin-top:22px}
'''
css += '.kind-threshold .node{padding:12px 22px;font-size:28px}.kind-threshold .threshold-number{font-size:82px}.kind-threshold .threshold-rule{margin:18px 0;height:16px}.kind-threshold{gap:12px}'
(P/'assets/style.css').write_text(css)
def visual(s):
 labels=s['labels'];kind=s['kind']
 def node(x,i,cls=''):return f'<div class="node item {cls}"><b>{i+1:02d}</b>{E(x)}</div>'
 if kind=='flow':return '<div class="nodes-flow">'+''.join(node(x,i,'flow-node') for i,x in enumerate(labels))+'</div>'
 if kind=='compare':return '<div class="compare-grid">'+''.join(f'<div class="node item">{E(x)}</div>' for x in labels)+'</div>'
 if kind=='bars':return ''.join(f'<div class="bar-row item"><span>{E(x)}</span><div class="bar-track"><div class="bar-fill" style="width:{v*100}%"></div></div></div>' for x,v in zip(labels,s['values']))+'<div class="scene-note">Cenário didático · entrada por solicitação · sem cache</div>'
 if kind=='threshold':return '<p class="threshold-number item">272.000</p><div class="threshold-rule item"></div>'+''.join(node(x,i) for i,x in enumerate(labels))
 if kind=='cost':return ''.join(node(x,i) for i,x in enumerate(labels))+'<p class="cost-total item">US$ 0,29</p>'
 tag='terminal' if kind=='terminal' else 'stack' if kind=='stack' else 'steps'
 return f'<div class="{tag}">'+''.join(node(x,i) for i,x in enumerate(labels))+'</div>'
def build(short=False):
 folder=P/'compositions';hosts=[];story=[];t=0
 for i,s in enumerate(D):
  ident=f'scene-{i+1:02d}'+('-short' if short else '')
  duration=6 if short else round(len(s['speech'].split())/145*60+2,2)
  parts=visual(s);n=len(s['labels'])
  markup=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"></head><body><template><style>#root{{position:absolute;inset:0;width:100%;height:100%;}}</style><div id="root" data-composition-id="{ident}" data-width="1920" data-height="1080" data-duration="{duration}"><div class="scene-shell"><header class="topline"><span>{E(s['chapter'])}</span><span>INEMA · GUIA PRÁTICO</span></header><div class="layout"><main><h1 class="main-title">{E(s['title'])}</h1><div class="visual kind-{s['kind']}">{parts}</div></main><aside class="avatar-panel"><img src="assets/nei-template.jpg" alt="Nei — fotografia de referência do TEMPLATE-AVATAR16"><p class="avatar-name">Nei Maldaner</p><div class="avatar-desc">Avatar e voz do template original do promoavatar.</div><div class="badge">PRÉVIA VISUAL<br>Sem narração<br>Foto de referência</div></aside></div><div class="takeaway">{E(s['takeaway'])}</div><footer class="footer"><span>GPT-6 ASTRA · CONTROLE DE TOKENS</span><span>{i+1:02d} / {len(D):02d}</span></footer><div class="progress-track"><div class="progress-fill"></div></div></div></div><script>
(function(){{const root=document.querySelector('[data-composition-id="{ident}"]');const tl=gsap.timeline({{paused:true}});const q=s=>root.querySelectorAll(s);
tl.fromTo(q('.main-title'),{{y:45,opacity:0}},{{y:0,opacity:1,duration:0.55,ease:'power3.out'}},0.12);
tl.fromTo(q('.avatar-panel'),{{scale:0.96,opacity:0}},{{scale:1,opacity:1,duration:0.65,ease:'power2.out'}},0.2);
tl.fromTo(q('.item'),{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.55,stagger:0.12,ease:'power3.out'}},0.6);
if(q('.bar-fill').length)tl.fromTo(q('.bar-fill'),{{scaleX:0}},{{scaleX:1,duration:1.2,stagger:0.1,ease:'power2.out'}},1);
tl.fromTo(q('.progress-fill'),{{scaleX:0}},{{scaleX:1,duration:{duration},ease:'none'}},0);
q('.node').forEach((el,i)=>{{const a=1.8+i*{max(0.5,(duration-4)/max(n,1))};tl.fromTo(el,{{borderColor:'#56616c'}},{{borderColor:'#efbe69',duration:0.4,ease:'sine.out'}},a);}});
window.__timelines['{ident}']=tl;}})();</script></template></body></html>'''
  (folder/f'{ident}.html').write_text(markup)
  (folder/f'{ident}.motion.json').write_text(json.dumps({'duration':duration,'assertions':[{'kind':'appearsBy','selector':'.main-title','bySec':1},{'kind':'staysInFrame','selector':'.main-title'}]}))
  hosts.append(f'<div id="{ident}" class="clip" data-composition-id="{ident}" data-composition-src="compositions/{ident}.html" data-start="{t:.2f}" data-duration="{duration}" data-width="1920" data-height="1080" data-track-index="1"></div>')
  story.append(f"## Frame {i+1}\nstatus: animated\nsrc: compositions/{ident}.html\nstart: {t:.2f}\nduration: {duration}\nrules: spring-pop-entrance; stat-bars-and-fills\n\n{s['title']} — {s['takeaway']}\n\nNarração: {s['speech']}\n")
  t+=duration
 name='preview-short.html' if short else 'index.html';root_id='short' if short else 'main'
 (P/name).write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="assets/style.css"><script src="assets/gsap.min.js"></script></head><body><div id="root" data-composition-id="{root_id}" data-duration="{t:.2f}" data-width="1920" data-height="1080">'+''.join(hosts)+f'</div><script>window.__timelines["{root_id}"]=gsap.timeline({{paused:true}});</script></body></html>')
 if not short:(P/'STORYBOARD.md').write_text('# Storyboard — tempos provisórios\n\nPrévia visual sem áudio. Durações estimadas a 145 palavras/minuto + 2 segundos por cena. Substituir pelos tempos reais após HeyGen.\n\n'+'\n'.join(story))
 return t
print('Long preview seconds:',build())
