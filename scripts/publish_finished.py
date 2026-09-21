"""Publish all three verified final lessons. Refuses incomplete production."""
from pathlib import Path
import json,subprocess,urllib.request
ROOT=Path('/home/nmaldaner/projetos/output/astrabasico');REPO=Path(__file__).resolve().parents[1]
def run(args,**kw):return subprocess.run(args,cwd=REPO,check=True,**kw)
def publish():
 receipts={lang:json.loads((ROOT/f'verification/assembled-{lang}.json').read_text()) for lang in ['pt','es','en']}
 production=json.loads((ROOT/'verification/production.json').read_text());assert len(production)==13 and all(s['status']=='rendered' for s in production.values())
 for lang,r in receipts.items():
  assert Path(r['file']).stat().st_size==r['bytes'] and r['duration']>600
  assert len(r['chapters'])==22
  assert (ROOT/f'verification/decode-full-{lang}.log').read_text()==''
 tag='v1.1.0';repo='inematds/astrabasico'
 notes=ROOT/'final/RELEASE.md';notes.write_text('Aula completa em português, espanhol e inglês:22tópicos ilustrados, avatar e voz do Nei, legendas SRT e kit prático.\n\n'+ '\n'.join(f"- {lang.upper()}: {int(r['duration']//60)}min{int(r['duration']%60):02d}s" for lang,r in receipts.items())+'\n\nGuia: https://inematds.github.io/astrabasico/guia/\n')
 existing=subprocess.run(['gh','release','view',tag,'--repo',repo],cwd=REPO,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 if existing.returncode:run(['gh','release','create',tag,'--repo',repo,'--draft','--title','Astra Básico — aulas completas PT, ES e EN','--notes-file',str(notes)])
 assets=[]
 for lang in receipts:assets.extend([str(ROOT/f'final/astra-basico-{lang}.mp4'),str(ROOT/f'final/astra-basico-{lang}.srt')])
 run(['gh','release','upload',tag,'--repo',repo,'--clobber',*assets])
 delivery={lang:{'url':f'https://github.com/{repo}/releases/download/{tag}/astra-basico-{lang}.mp4','srt':f'https://github.com/{repo}/releases/download/{tag}/astra-basico-{lang}.srt','duration':r['duration'],'chapters':r['chapters']} for lang,r in receipts.items()}
 (REPO/'docs/video-delivery.json').write_text(json.dumps(delivery,ensure_ascii=False,indent=2)+'\n')
 run(['python3','scripts/build_guide.py'])
 readme=REPO/'README.md';text=readme.read_text();begin=text.index('**Estado dos vídeos:**');end=text.index('\n\n',begin)
 text=text[:begin]+'**Estado dos vídeos:** aulas completas em português, espanhol e inglês, com22tópicos ilustrados, avatar e voz do Nei e legendas. Assista no guia ou baixe osMP4 eSRT na [release v1.1.0](https://github.com/inematds/astrabasico/releases/tag/v1.1.0).'+text[end:];text=text.replace('Versão 1.0.0.','Versão 1.1.0.');readme.write_text(text)
 for lang,item in delivery.items():
  path=REPO/'guia'/('' if lang=='pt' else lang)/'index.html';page=path.read_text()
  assert item['url'] in page and item['srt'] in page and page.count('<details>')==22
 run(['git','config','user.name','inematds']);run(['git','config','user.email','inematds@gmail.com'])
 run(['git','add','README.md','docs/video-delivery.json','guia/index.html','guia/es/index.html','guia/en/index.html','kit-economia-tokens.zip'])
 changed=subprocess.run(['git','diff','--cached','--quiet'],cwd=REPO).returncode
 if changed:run(['git','commit','-m','feat: publish narrated illustrated lessons in three languages'])
 run(['git','push','origin','main'])
 run(['gh','release','edit',tag,'--repo',repo,'--draft=false'])
 (ROOT/'verification/publication.json').write_text(json.dumps({'release':f'https://github.com/{repo}/releases/tag/{tag}','videos':delivery},indent=2))
 print('Published release and pushed guide',flush=True)
if __name__=='__main__':publish()
