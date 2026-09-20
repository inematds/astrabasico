# Fontes e decisões editoriais — 20/09/2026

Fonte de partida: transcrição fornecida pelo usuário de [Paste This Into GPT-6 Astra, Never Run Out Of Tokens Again](https://www.youtube.com/watch?v=XgMhU4CE-lQ), Sharbel A. A descrição não pôde ser recuperada integralmente pelo leitor; os três prompts do kit são autorais.

| Tema | Tratamento na aula | Fonte de conferência |
|---|---|---|
| API x assinatura | Tarifas de API não são uma conversão automática do limite do plano | https://learn.chatgpt.com/docs/pricing |
| Astra | Tarifas datadas, contexto longo explicitamente identificado como API | https://developers.openai.com/api/docs/models/gpt-6-astra |
| Cache | Reutilização condicional; não dizer que tudo sempre custa preço cheio | https://developers.openai.com/api/docs/guides/prompt-caching |
| Esforço | Não fixar ganho universal; reconhecer mecanismos compatíveis de atualização de configuração | https://developers.openai.com/api/docs/guides/latest-model |
| Compactação | Custo imediato pode coexistir com economia posterior | https://developers.openai.com/api/docs/guides/compaction |
| Arquivos | PDF/visão pode usar texto e imagens; extração pode perder informação; não prometer redução fixa | https://developers.openai.com/api/docs/guides/file-inputs |
| Velocidade | Multiplicador depende do produto; tabela de créditos consultada indica 2,5x para Astra; não generalizar 2x | https://learn.chatgpt.com/docs/pricing e https://developers.openai.com/api/docs/guides/fast-mode |

## Alegações excluídas como regra geral

- Assistente sempre conhece saldo e horário de renovação: não comprovado sem acesso aos indicadores.
- Todo plugin injeta todo seu manual em toda mensagem: depende da implementação e descoberta de ferramentas.
- Trocar modelo é sempre mais caro: precisa considerar o restante da tarefa.
- Compactar nunca economiza: incorreto como regra geral.
- PDF sempre custa quatro vezes mais: não há proporção universal.
- Benchmark de US$ 0,80 / US$ 3,26 / US$ 7: não usado como dado verificado; nenhuma medição independente foi reproduzida.
- RTK e Headroom: mencionados como opções citadas pela fonte; sem instalação nem endosso de porcentagens de economia.

## Exemplos próprios

A progressão 2 mil → 4 mil → 6 mil é um cenário didático sem cache, e não uma medição. O exemplo US$ 0,29 usa 10 mil tokens de entrada comum, 90 mil de cache lido e 2 mil de saída, sem escrita de cache, ferramentas ou adicionais. A calculadora foi testada no limiar exato de 272 mil e acima dele.
