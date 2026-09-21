# Astra Básico

[Guia prático em português, espanhol e inglês](https://inematds.github.io/astrabasico/guia/)

Roteiro completo em 22 cenas, prompts autorais, skill `economia-tokens` e calculadora local. Baseado no vídeo indicado nas fontes, com correções e exemplos próprios.

**Estado dos vídeos:** produção em andamento pela assinatura do HeyGen, com avatar Nei, voz INEMA TIME e Avatar III. Roteiros divididos em 13 blocos de até 4.500 caracteres. O primeiro bloco foi baixado, transcrito e montado com ilustrações e legendas; as seis cenas passaram nas verificações e na revisão visual. Envio dos demais blocos, download, montagem e publicação são acompanhados por processos persistentes. Os vídeos completos serão vinculados ao guia somente depois das verificações finais.

## Uso

```sh
python3 kit/economia-tokens/scripts/estimar.py --input 100000 --cached 90000 --output 2000
```

Resultado ilustrativo: US$ 0,29 com tarifas datadas de 20/09/2026. Não mede uma conta ou assinatura. Confira as fontes antes de usar tarifas.

Leia [o kit](kit/COMO-USAR.md), [as fontes e correções](docs/FONTES-E-CORRECOES.md) e os roteiros em `docs/`.

## Composição visual

`video/index.html` é a composição HyperFrames com durações provisórias. `video/previa-visual-pt.mp4` apresenta as 22 cenas em 132 segundos, sem áudio. Para regenerar o HTML português: `python3 scripts/build_video.py`. A guia é gerada com `python3 scripts/build_guide.py`.

Versão 1.0.0.
