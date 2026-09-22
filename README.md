# Astra Básico

[Guia prático em português, espanhol e inglês](https://inematds.github.io/astrabasico/guia/)

Roteiro completo em 22 cenas, prompts autorais, skill `economia-tokens` e calculadora local. Baseado no vídeo indicado nas fontes, com correções e exemplos próprios.

**Estado dos vídeos:** aulas completas em português, espanhol e inglês, com 22 tópicos ilustrados, avatar e voz do Nei e legendas. Assista no guia ou baixe os MP4 e SRT na [release v1.1.0](https://github.com/inematds/astrabasico/releases/tag/v1.1.0).

## Uso

```sh
python3 kit/economia-tokens/scripts/estimar.py --input 100000 --cached 90000 --output 2000
```

Resultado ilustrativo: US$ 0,29 com tarifas datadas de 20/09/2026. Não mede uma conta ou assinatura. Confira as fontes antes de usar tarifas.

Leia [o kit](kit/COMO-USAR.md), [as fontes e correções](docs/FONTES-E-CORRECOES.md) e os roteiros em `docs/`.

## Composição visual

`video/index.html` é a composição HyperFrames com durações provisórias. `video/previa-visual-pt.mp4` apresenta as 22 cenas em 132 segundos, sem áudio. Para regenerar o HTML português: `python3 scripts/build_video.py`. A guia é gerada com `python3 scripts/build_guide.py`.

Versão 1.1.0.
