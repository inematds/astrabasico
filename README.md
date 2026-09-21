# Astra Básico

[Guia prático em português, espanhol e inglês](https://inematds.github.io/astrabasico/guia/)

Roteiro completo em 22 cenas, prompts autorais, skill `economia-tokens` e calculadora local. Baseado no vídeo indicado nas fontes, com correções e exemplos próprios.

**Estado dos vídeos:** prévia visual aprovada, sem narração. Os três avatares narrados (PT/ES/EN) foram enviados ao HeyGen em 21/09/2026 pela rota do estúdio usada no promoavatar3, com Avatar III, voz INEMA TIME e 1080p. A geração está em andamento; a montagem final com ilustrações e legendas ainda está pendente.

## Uso

```sh
python3 kit/economia-tokens/scripts/estimar.py --input 100000 --cached 90000 --output 2000
```

Resultado ilustrativo: US$ 0,29 com tarifas datadas de 20/09/2026. Não mede uma conta ou assinatura. Confira as fontes antes de usar tarifas.

Leia [o kit](kit/COMO-USAR.md), [as fontes e correções](docs/FONTES-E-CORRECOES.md) e os roteiros em `docs/`.

## Composição visual

`video/index.html` é a composição HyperFrames com durações provisórias. `video/previa-visual-pt.mp4` apresenta as 22 cenas em 132 segundos, sem áudio. Para regenerar o HTML português: `python3 scripts/build_video.py`. A guia é gerada com `python3 scripts/build_guide.py`.

Versão 1.0.0.
