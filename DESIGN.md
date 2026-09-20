---
name: Astra Básico
description: Guia educativo INEMA para compreender contexto e consumo e simular custos.
colors:
  bg: "#0c0c10"
  bg2: "#14141b"
  card: "#16161e"
  line: "#272730"
  txt: "#e9e9ee"
  mut: "#9a9aa6"
  amb: "#E2A23B"
  amb2: "#f0c070"
  sky: "#38bdf8"
  pro: "#cbd5e1"
  button-text: "#1a1206"
  light-bg: "#f6f7f9"
  light-bg2: "#eceef2"
  light-card: "#ffffff"
  light-line: "#e1e3ea"
  light-txt: "#1a1a22"
  light-mut: "#5b5b68"
  light-amb: "#b9791d"
  light-amb-text: "#965b10"
  light-amb2: "#a16207"
  light-sky: "#0369a1"
  light-pro: "#b45309"
typography:
  display:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(2.2rem,5vw,3.5rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(1.5rem,3.4vw,2.1rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.02em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "16px"
    lineHeight: 1.65
  label:
    fontFamily: "Sora, sans-serif"
    fontSize: ".72rem"
    fontWeight: 600
    letterSpacing: ".14em"
  code:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: ".86rem"
    lineHeight: 1.6
rounded:
  input: "8px"
  button: "10px"
  code: "12px"
  card: "14px"
  hero: "16px"
spacing:
  compact: "8px"
  control: "12px"
  grid: "16px"
  card: "20px"
  gutter: "22px"
  hero-gap: "40px"
  section: "62px"
components:
  button-primary:
    backgroundColor: "{colors.amb}"
    textColor: "{colors.button-text}"
    rounded: "{rounded.button}"
    padding: ".6em 1.05em"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.txt}"
    rounded: "{rounded.button}"
    padding: ".6em 1.05em"
  input:
    backgroundColor: "{colors.bg2}"
    textColor: "{colors.txt}"
    rounded: "{rounded.input}"
    padding: "12px"
  card:
    backgroundColor: "{colors.card}"
    rounded: "{rounded.card}"
    padding: "20px"
---

# Design System: Astra Básico

## Overview

**Creative North Star: "INEMA dark âmbar"**

A identidade é a do padrão projetos-landing-guia: INEMA dark âmbar com tema claro opcional, Sora, Inter e JetBrains Mono. O guia privilegia leitura (Read); a calculadora acrescenta uma operação delimitada (Operate). A documentação registra o código existente, sem propor outra identidade.

**Key Characteristics:**
- Âmbar para identidade e ação; azul para INEMA.CLUB e foco.
- Leitura por seções, tópicos expansíveis e código com quebra de linha.
- Tema escuro inicial e claro persistido localmente.

## Colors

O âmbar organiza a marca e a ação sobre superfícies quase pretas; o tema claro usa papel cinza e superfícies brancas. Os valores normativos estão no frontmatter, extraídos de `scripts/guide-style.css` e dos complementos em `scripts/build_guide.py`.

`bg`, `bg2`, `card` e `line` definem fundo, superfície secundária, cartão e divisória. `txt` é texto principal e `mut` é secundário. `amb` permanece como preenchimento de botões; `amb-text` acompanha `amb` no escuro e usa `light-amb-text` no claro para texto e links. `sky` identifica INEMA.CLUB e o foco; `pro` identifica PRO. Os tokens prefixados com `light-` correspondem às substituições de `body.light`.

## Typography

Sora nos títulos, marca, rótulos e links de ação; Inter no texto; JetBrains Mono nos prompts e comandos. O corpo usa 16px/1.65; título de hero e títulos de seção são fluidos conforme o frontmatter. A introdução do hero usa 1.18rem e 34ch; explicações dos tópicos têm largura máxima de 78ch. Resumos expansíveis usam Sora em 1.12rem. Rótulos `.chip` são pequenos, em caixa alta com espaçamento entre letras. O botão de cálculo herda a fonte do corpo pela regra geral de `button`; links `.btn` conservam Sora.

## Layout

Contêiner de 1160px com margens automáticas e 22px laterais. Hero em duas colunas 1.1fr/.9fr, vão de 40px e 74px verticais; abaixo de 780px vira uma coluna com 48px verticais. Seções usam 62px verticais e divisórias. Navegação sticky com 60px e âncoras compensadas por `scroll-margin-top:70px`.

A calculadora usa quatro colunas, duas até 820px e uma até 540px. Links secundários da navegação somem até 760px; até 620px a navegação permite quebra e usa 16px laterais. Passos têm coluna numerada de 46px e texto flexível. Prompts e comandos quebram linhas longas para caber no celular.

## Elevation & Depth

As superfícies se distinguem por tom e bordas de 1px. A imagem do hero tem sombra `0 30px 80px -30px #000`. O hero inclui brilho radial âmbar decorativo; o tema claro reduz sua opacidade. A navegação escura usa transparência e `backdrop-filter:blur(12px)`; a clara usa o fundo do tema. Não há animação contínua: apenas rolagem suave, desativada em `prefers-reduced-motion:reduce`.

## Shapes

Cantos de 8px em inputs, 10px em botões e alternador de tema, 12px nos blocos de código e números de passos, 14px em cartões e vídeo, 16px na imagem do hero. Pills do rodapé têm raio de 999px. Os tópicos são linhas expansíveis com divisória inferior, sem cartões elevados individuais.

## Components

- **Navegação:** marca Astra Básico, INEMA.CLUB/PRO, links de seção e alternador de tema. Links de seção mudam de texto secundário para principal no hover. INEMA.CLUB/PRO aumentam brilho no hover. O tema persiste em `localStorage` sob `astrabasico-theme`.
- **Idiomas:** links Português, Español e English; o idioma atual usa `aria-current="page"` e sublinhado com deslocamento de 6px. Cada idioma contém 22 tópicos completos e roteiro correspondente.
- **Ações:** ação primária âmbar e download ghost com borda. Padding `.6em 1.05em`. Foco global: contorno de 3px em `sky`, afastado 4px. O alternador de tema muda a borda para âmbar no hover.
- **Tópicos:** `details`/`summary` nativos, padding vertical de 22px, texto integral e nota final; abertura independente por tópico.
- **Calculadora:** quatro inputs numéricos rotulados para entrada, cache, escrita e saída; botão de cálculo e `output` com `aria-live="polite"`. Cálculo estático no navegador, sem API, com parcelas e mensagem de faixa; entradas inválidas substituem o resultado por mensagem textual. Não representa cobrança nem limite da assinatura.
- **Prompts e kit:** prompts em blocos de código e passos numerados; ZIP baixável sem conta. Python é necessário apenas para executar a calculadora local do kit.
- **Vídeo:** player nativo com controles, poster e `preload="metadata"`; largura total, altura máxima de 650px. O arquivo disponível é prévia silenciosa PT de 132 segundos e 22 cenas. Avatar e narração finais PT/ES/EN continuam pendentes.
- **Cartões:** a folha base contém `.card` para superfícies de apoio com borda e padding de 20px; não converte os tópicos da página atual em cartões.

## Do's and Don'ts

- Do preservar a identidade INEMA e os links INEMA.CLUB e PRO.
- Do distinguir o âmbar de fundo de botão do âmbar de texto no tema claro.
- Do manter rótulos, foco visível, conteúdo completo dos tópicos e erros da calculadora legíveis.
- Do identificar a prévia como silenciosa em PT e os vídeos finais como pendentes.
- Don't prometer economia garantida, franquia ilimitada ou consulta de cobrança real.
- Don't descrever roteiros PT/ES/EN como vídeos finais disponíveis.
- Don't esconder evidências, ressalvas ou a composição do custo simulado.
