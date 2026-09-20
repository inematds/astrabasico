# Kit prático — Economia de tokens

Instale a pasta `economia-tokens` em `~/.codex/skills/` (revise qualquer instalação existente antes de substituir). Em uma nova sessão do Codex, use:

```text
$economia-tokens Faça um diagnóstico desta tarefa e execute com contexto controlado: [objetivo].
```

Não altera o modelo ou a cobrança. Não garante economia percentual. O agente continua sujeito às permissões do ambiente.

## Prompts sem instalar nada

Abra `economia-tokens/references/prompts.md`. Há diagnóstico, execução e passagem de sessão. São prompts autorais INEMA, não os prompts originais do vídeo citado.

## Calculadora local

Na pasta deste kit:

```bash
python3 economia-tokens/scripts/estimar.py --input 100000 --cached 90000 --output 2000
```

Resultado esperado: **US$ 0,29**, usando as tarifas datadas fornecidas. `--input` inclui os tokens em cache. A saída deve incluir todos os tokens faturáveis, inclusive raciocínio quando aplicável. Se não sabe quantos tokens atingiram cache, use zero para esse campo; não presuma acerto.

O JSON de preços é editável e registra data e fonte. Confira as tarifas oficiais antes de uma decisão de gasto. Esta calculadora não mede sua sessão, não lê sua conta e não usa API.

## Exercício de comparação

Escolha duas tarefas equivalentes, registre modelo/esforço, consumo observado e critério de qualidade. Mude uma variável. Compare também retrabalho. Sem medição comparável, registre a economia como desconhecida.
