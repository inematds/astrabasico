---
name: economia-tokens
description: Diagnosticar e reduzir desperdício de contexto e tokens em tarefas com ChatGPT, Codex ou API, preservando qualidade e evidências. Use quando o usuário pedir economia de tokens, revisão de consumo ou execução com contexto controlado.
---
# Economia de tokens

Identifique o produto e a tarefa antes de recomendar mudanças. Assinatura, créditos e cobrança da API não são intercambiáveis. Não prometa uso ilimitado nem percentuais fixos de economia.

## Diagnóstico

Use apenas indicadores realmente acessíveis: status da sessão, campos de uso da API, logs delimitados ou números fornecidos pelo usuário. Distinga observado, estimado e indisponível. Perguntar ao modelo não lhe concede acesso ao saldo, limite ou horário de renovação. Não leia históricos privados inteiros quando um registro de uso basta.

Priorize a provável fonte de desperdício: arquivos fora de escopo, saídas excessivas, tentativas repetidas por falta de critérios ou esforço desproporcional. Não remova instruções necessárias para reduzir tokens.

## Execução

- Leia primeiro as instruções aplicáveis ao projeto; restrinja buscas a caminhos e tipos relevantes. Amplie o escopo quando a evidência pedir.
- Preserve logs completos em arquivo quando forem grandes. Mostre erros, contagens, trechos pertinentes e caminho do log. Nunca filtre uma falha para fazê-la parecer sucesso.
- Escolha ou recomende modelo/esforço conforme dificuldade, ambiguidade e custo de errar. Não altere silenciosamente configurações globais nem alegue ter mudado o modelo atual sem confirmação da ferramenta.
- Delegue apenas quando permitido pelas instruções vigentes e quando houver subtask delimitada cujo benefício supere contexto e integração adicionais. Passe entrada, saída e critério de sucesso; não copie todo o histórico.
- Nova tarefa independente pode usar nova sessão com passagem curta. Compactação pode ter custo imediato e benefício posterior; não trate como sempre boa ou sempre ruim.
- Troca de modelo pode alterar cache; isso não prova que a troca custa mais no total. Não generalize perda de cache para qualquer alteração de esforço.
- Texto é adequado quando o conteúdo textual basta; preserve imagens, tabelas e layout essenciais. Não prometa que converter PDF reduz um percentual fixo.
- Verifique a entrega com o teste ou inspeção pertinente. Compare economia por resultado aprovado, sem omitir retrabalho.

## Recursos sob demanda

- Para prompts de diagnóstico, execução e passagem: [prompts.md](references/prompts.md).
- Para estimativa de API: execute `python3 scripts/estimar.py --help`. Usa tarifas em `references/precos.json`, com data e fontes. Revalide os preços oficiais antes de usá-los para uma decisão atual. Não representa fatura nem assinatura.

Ao terminar, relate resultado, evidência, consumo observado quando disponível e limitações. Não invente economia quando não houver comparação equivalente.
