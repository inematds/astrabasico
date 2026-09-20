# GPT-6 Astra: controle de tokens

Roteiro autoral para avatar do Nei. Status: conteúdo preparado; voz e vídeo aguardam acesso HeyGen.

## 01. Inteligência com controle

Você abre uma conversa, pede uma tarefa aparentemente simples e percebe que o limite caiu mais do que esperava. Antes de culpar o modelo, precisamos entender o trabalho que aconteceu por trás daquela resposta. Nesta aula, vamos transformar o assunto tokens em decisões práticas. Você vai aprender a observar o consumo, organizar o contexto, escolher o esforço de raciocínio e dividir tarefas quando isso fizer sentido. Também vamos analisar algumas dicas populares que parecem universais, mas dependem do produto e da configuração. Ao final, você terá prompts prontos, uma calculadora e uma skill para aplicar o método. A proposta não é prometer uso ilimitado. É conseguir resultados bons com menos desperdício e com evidências do que realmente funcionou.

**Tela:** O objetivo é gastar melhor, mantendo a qualidade.

## 02. Três contas diferentes

Primeiro, separe três ambientes. No ChatGPT, você utiliza os recursos e limites do seu plano. No Codex, o consumo depende também do trabalho do agente, das ferramentas e das condições da conta. Na API, aplicações enviam solicitações que são cobradas conforme as tarifas aplicáveis. A mesma palavra, consumo, pode representar coisas diferentes nesses ambientes. Por isso, um exemplo em dólares na API não prova quanto da sua assinatura será gasto. A data da consulta também importa: modelos, preços e regras mudam. Nesta aula, números de preço serão identificados como exemplos da API, e indicadores de assinatura serão tratados separadamente. Essa distinção evita começar a economizar usando uma conta que não representa o seu caso.

**Tela:** Não transfira automaticamente preços da API para a assinatura.

## 03. A resposta é só uma parte

Tokens são unidades em que o conteúdo é dividido para o processamento. Uma palavra pode ocupar mais de um token, e código, imagens e outros formatos têm regras próprias. O texto que você digita é apenas parte da entrada. Instruções, trechos de conversa e resultados de ferramentas também podem fazer parte dela. Na saída, além do texto visível, modelos de raciocínio podem consumir tokens de processamento que não aparecem como uma explicação completa na tela. Pense em uma oficina: você vê a peça entregue, mas houve preparação, consulta e trabalho para produzi-la. Assim, uma resposta curta não garante uma tarefa barata. Precisamos observar a entrada, a saída e as operações que foram necessárias.

**Tela:** Tokens são unidades de processamento; não equivalem sempre a palavras.

## 04. Histórico: o efeito acumulado

Vamos visualizar uma conversa simplificada. Na primeira rodada entram dois mil tokens. Na segunda, o material acumulado leva a entrada para quatro mil. Na terceira, ela chega a seis mil. Somando essas entradas, são doze mil tokens processados ao longo das três solicitações, embora a última tenha seis mil. Este é um exemplo didático, não uma medição da sua conta. Aplicações podem selecionar, resumir ou compactar o histórico, e o cache pode mudar o custo. Portanto, a frase tudo é sempre reenviado pelo preço cheio é forte demais. A conclusão prática continua útil: conversas que acumulam assuntos, arquivos e saídas desnecessárias podem aumentar o trabalho das próximas rodadas. Manter contexto relevante ajuda tanto a clareza quanto o controle.

**Tela:** Exemplo didático sem cache: 12 mil tokens processados em três rodadas.

## 05. Reutilizar pode custar menos

Cache é o reaproveitamento de processamento de uma parte compatível da entrada. Imagine que você precisa consultar repetidamente o mesmo manual. Se o sistema consegue reutilizar uma parte já processada, essa parte pode ter tarifa menor. Na API, a documentação distingue entrada comum, entrada em cache e, em alguns modelos, escrita de cache. A existência de uma conversa longa não garante um acerto de cache, porque a compatibilidade do prefixo e outras condições importam. Também não significa que a resposta nova será grátis. Na prática, mantenha instruções estáveis quando elas forem úteis, evite reorganizações sem necessidade e consulte os campos de uso disponíveis. Não tente deduzir a economia somente pelo tamanho que aparece na janela.

**Tela:** Cache reaproveita processamento; não torna toda a conversa gratuita.

## 06. Trocar de modelo: faça a conta

Trocar o modelo durante uma tarefa pode alterar o reaproveitamento de contexto. Mudar configurações também exige atenção, mas isso não permite afirmar que qualquer troca será a decisão mais cara. Imagine que ainda faltam cem operações simples. Mesmo havendo um custo inicial de mudança, um modelo adequado e mais econômico pode compensar nas operações seguintes. Em outro caso, trocar perto do final talvez acrescente trabalho sem benefício. A documentação do Astra também descreve mecanismos específicos para atualizar o esforço preservando o prefixo em solicitações compatíveis da API. O aplicativo que você usa pode não expor esse mecanismo. A regra prática é planejar a divisão cedo, considerar o que ainda falta e comparar o custo total para chegar ao resultado correto.

**Tela:** Uma troca pode compensar; perder cache não prova prejuízo total.

## 07. Comece pelas evidências

Antes de alterar configurações, faça um diagnóstico. No Codex, consulte o status e os indicadores disponíveis na sua versão. Na API, examine os dados de uso retornados e o painel correspondente. No ChatGPT, consulte os limites que a interface realmente mostra. Perguntar ao assistente quanto já foi gasto não concede acesso automático à cobrança da conta. Ele deve distinguir o que conseguiu observar daquilo que não está disponível. Nosso primeiro prompt faz exatamente isso: pede evidências, identifica o ambiente e evita inventar percentuais ou horários de renovação. Registre uma pequena referência inicial, como a tarefa realizada, o modelo escolhido, o esforço e o uso observado. Depois você terá uma base honesta para comparar uma mudança.

**Tela:** Sem acesso ao indicador, o assistente deve dizer: não disponível.

## 08. Procure o maior desperdício

Nem todo usuário tem o mesmo problema. Para uma pessoa, o maior custo é carregar arquivos enormes. Para outra, é pedir explicações longas em todas as etapas. Uma terceira repete a tarefa porque o objetivo estava mal definido. Por isso, escolha a maior fonte de desperdício antes de instalar ferramentas. Pegue duas tarefas semelhantes, mantenha os critérios de qualidade e altere uma variável por vez. Por exemplo, limite a saída do terminal preservando erros e execute novamente uma tarefa equivalente. Compare consumo, tempo e resultado. Se o consumo cair, mas a solução perder informações essenciais, a mudança precisa de ajuste. Economizar é reduzir o custo por resultado aprovado, e não apenas produzir um número menor de tokens.

**Tela:** Altere uma variável por vez e compare tarefas equivalentes.

## 09. O esforço deve servir à tarefa

O esforço de raciocínio controla quanto processamento o modelo dedica ao problema dentro das opções disponíveis. Mais esforço pode ajudar em tarefas difíceis, mas não garante uma resposta melhor em toda situação. Para um trabalho intermediário, começar em médio é uma hipótese prática que você pode testar. Para uma extração simples, talvez seja suficiente um modelo mais econômico com esforço baixo. Para uma investigação complexa, pode valer começar acima disso. Defina primeiro o que torna a resposta aceitável. Depois aumente o esforço quando houver uma falha concreta que justifique o custo. Nesta aula, não vamos apresentar valores de benchmarks como se fossem sua fatura. Um teste público compara um conjunto específico de tarefas; seu trabalho pode ter outra distribuição de dificuldade.

**Tela:** Use dificuldade, ambiguidade e verificação para decidir.

## 10. Rapidez também tem preço

Velocidade e esforço são escolhas diferentes. O modo rápido busca reduzir a espera; o esforço orienta o processamento do problema. É possível pagar mais pela velocidade sem estar pedindo um raciocínio mais profundo. A transcrição original fala em dobrar o preço, mas isso não deve ser repetido como regra para todos os ambientes. Na documentação consultada, há condições específicas por produto, e a tabela de créditos apresenta um multiplicador próprio para o Astra. Antes de ativar o modo rápido, veja a tarifa aplicável e avalie a urgência. Uma resposta durante uma reunião pode justificar o adicional. Uma análise que pode terminar alguns minutos depois talvez não precise dele. A decisão depende do valor do tempo naquele trabalho.

**Tela:** Confira o multiplicador do seu produto e da sua conta.

## 11. Delegue uma tarefa definida

Uma estratégia útil é reservar modelos mais capazes para as decisões que realmente exigem essa capacidade. Imagine a produção de um relatório. Uma etapa organiza arquivos e extrai campos. Outra verifica inconsistências. Uma terceira resolve as questões ambíguas e redige a conclusão. Essas etapas podem usar recursos diferentes quando a ferramenta permitir. Mas delegar não significa abrir vários agentes sem necessidade. Cada agente pode carregar contexto, consumir tokens e produzir trabalho de integração. Escreva uma tarefa delimitada: quais arquivos ler, o que entregar e como conferir o resultado. Só faça a divisão se houver benefício provável. Uma tarefa pequena pode ser mais barata e mais rápida com um único agente que recebe uma instrução clara.

**Tela:** Cada agente precisa de entrada, saída e critério de sucesso.

## 12. Exemplo: revisar um relatório

Vamos aplicar a ideia. Você tem um relatório de vendas com três tabelas e quer encontrar divergências. A etapa de extração recebe somente as tabelas necessárias e devolve números com a origem de cada um. A revisão confere somas e marca os casos que não fecham. O modelo mais capaz recebe as divergências, as evidências e a pergunta de negócio. Ele não precisa receber páginas irrelevantes para decidir. Se a conclusão depender de algo que foi omitido, deve buscar essa informação. O kit inclui um modelo de instrução para essa passagem. A skill não finge que mudou o modelo nem promete roteamento invisível: ela usa a capacidade real do ambiente e respeita sua autorização para delegar.

**Tela:** O modelo mais caro não precisa reler tudo em todas as etapas.

## 13. Menos ruído, mesma evidência

Ferramentas podem acrescentar instruções e resultados à conversa. O quanto disso é carregado depende da integração; algumas ferramentas são descobertas apenas quando necessárias. Por isso, não é correto dizer que todo plugin sempre injeta seu manual inteiro a cada mensagem. Ainda assim, vale manter as integrações pertinentes ao trabalho. Outro alvo claro são as saídas enormes de comandos. Em vez de colocar milhares de linhas no chat, preserve o log completo em arquivo e traga um resumo com erros, contagens e trechos importantes. Em buscas de código, restrinja diretórios e tipos de arquivo. A economia não pode esconder uma falha de build ou um aviso relevante. O resumo precisa manter a evidência necessária para a próxima decisão.

**Tela:** Filtre o que entra no contexto, sem esconder falhas.

## 14. RTK e Headroom: medir antes

O vídeo de referência cita RTK e Headroom como recursos para reduzir saídas ou contexto. Eles entram aqui como opções a avaliar, e não como requisito para economizar. Antes de instalar qualquer um, confira a documentação do projeto, a integração com sua versão e o que exatamente será filtrado. Faça um teste pequeno que inclua um comando com sucesso e outro com erro. Confirme que o agente continua percebendo o erro e que o relatório de economia mede aquilo que afirma medir. Reduzir caracteres de uma listagem não equivale automaticamente a reduzir a fatura na mesma proporção. Nosso kit funciona sem essas ferramentas: começa com escopo de busca, limite de saída e preservação do log completo.

**Tela:** Percentuais anunciados não são garantia para o seu projeto.

## 15. Novo assunto, contexto próprio

Quando uma tarefa termina e começa um assunto independente, uma nova conversa pode evitar carregar material desnecessário. Mas não jogue fora as decisões de que o próximo trabalho depende. Prepare uma passagem curta com objetivo, estado atual, arquivos relevantes, verificações feitas e próximo passo. Imagine que você terminou o roteiro de um vídeo e vai iniciar a publicação. O próximo agente precisa do arquivo aprovado e das instruções de publicação, não de todas as tentativas de redação. Para tarefas que ainda dependem do mesmo contexto, permanecer na conversa pode ser adequado. A escolha não deve ser automática. Nosso terceiro prompt cria uma passagem que você consegue ler e corrigir antes de iniciar a nova sessão.

**Tela:** Leve um resumo útil; não copie todo o histórico.

## 16. Compactar tem custo e benefício

Compactar significa reduzir o contexto mantendo informações necessárias para continuar. Pode haver custo no momento dessa operação, mas ela também pode diminuir o contexto das rodadas seguintes. Portanto, dizer que compactação nunca economiza é uma conclusão incorreta. Pense em organizar uma mesa cheia de documentos: a organização dá trabalho, mas pode facilitar muitas consultas futuras. O benefício depende de quanto trabalho ainda resta, do tamanho reduzido, do cache e da qualidade do estado preservado. Depois de compactar, confira se objetivos, restrições e decisões importantes continuam presentes. Quando o assunto já acabou, uma passagem para outra conversa pode ser mais adequada. Quando precisa continuar uma investigação longa, a compactação pode ser parte normal de uma estratégia de continuidade.

**Tela:** Avalie a continuidade e quantas rodadas ainda faltam.

## 17. Capacidade não é faixa de preço

Uma janela grande de contexto diz quanto cabe, mas não garante que toda a capacidade tenha o mesmo preço. Na documentação consultada para o Astra na API, solicitações com mais de duzentos e setenta e dois mil tokens de entrada passam a uma faixa maior. As tarifas de entrada e cache são multiplicadas por dois, e a de saída por um e meio, para a solicitação inteira. É acima do limite, e não a partir de qualquer valor próximo dele. Essa regra não deve ser usada como cálculo automático da sua assinatura. Antes de enviar material grande pela API, estime a entrada e veja se tudo é necessário. Use a calculadora do kit para simular a faixa com as tarifas registradas e atualize essas tarifas quando a documentação mudar.

**Tela:** Regra consultada para GPT-6 Astra na API, em 20/09/2026.

## 18. Uma conta que você pode conferir

Aqui está um exemplo verificável, usando as tarifas padrão consultadas. Suponha uma entrada total de cem mil tokens, dos quais noventa mil foram efetivamente lidos do cache. Sobram dez mil tokens de entrada comum. A dez dólares por milhão, essa parte custa dez centavos. Os noventa mil em cache, a um dólar por milhão, custam nove centavos. Com dois mil tokens de saída, a cinquenta dólares por milhão, temos mais dez centavos. O total é vinte e nove centavos de dólar. É uma simulação com cache confirmado, sem escrita de cache, ferramentas ou outros adicionais. Não é previsão da sua conta. A calculadora deixa cada parcela visível para você conferir e comparar cenários.

**Tela:** Total ilustrativo: US$ 0,29. Sem ferramentas ou escrita de cache.

## 19. Texto quando o texto basta

Se a tarefa é revisar um parágrafo, normalmente faz sentido enviar o texto. Se é avaliar a aparência de uma tela, a imagem carrega informação que o texto não preserva. Em PDFs enviados a modelos com visão por determinados caminhos da API, o processamento pode incluir texto extraído e imagens das páginas. Isso ajuda a interpretar diagramas, mas também influencia o consumo. Converter tudo para texto pode eliminar tabelas, fórmulas e relações visuais importantes. Por isso, não prometemos uma economia fixa de setenta e cinco por cento. Extraia texto quando ele for suficiente, selecione as páginas necessárias e preserve as imagens que forem essenciais. Depois confira a extração: uma coluna trocada ou um número perdido pode custar mais retrabalho do que a economia inicial.

**Tela:** Escolha o formato pela informação necessária à tarefa.

## 20. Clareza evita retrabalho

Escrever menos palavras nem sempre é o melhor caminho. Um pedido curto demais pode omitir o objetivo e gerar várias tentativas. Por outro lado, instruções repetidas e exemplos irrelevantes também ocupam contexto. Procure a menor instrução que mantenha objetivo, escopo, restrições e critérios de conclusão claros. Por exemplo: revise estas duas funções, corrija o erro demonstrado por este teste e apresente o resultado da verificação. Isso costuma orientar melhor do que simplesmente dizer melhore tudo. O kit traz três prompts autorais: diagnóstico, execução com contexto controlado e passagem de sessão. São recursos novos preparados para esta aula; não estamos atribuindo a eles a autoria dos prompts que o vídeo original menciona sem mostrar na transcrição.

**Tela:** Um bom prompt é suficiente e preciso; não apenas curto.

## 21. A skill ajuda a aplicar o método

A skill economia de tokens reúne as decisões práticas para você não precisar repetir todas as instruções. Ao acioná-la, o agente identifica o ambiente, trabalha com dados observáveis e procura reduzir contexto irrelevante. Ela recomenda uma divisão proporcional à tarefa, preserva os erros importantes e verifica o resultado. Não aumenta a franquia, não inventa um orçamento disponível e não altera silenciosamente o modelo da sessão. Se a plataforma não permite determinada configuração, a orientação informa essa limitação. Junto dela, você recebe a calculadora de custo da API, que roda localmente e não envia seus textos para outro serviço. Os valores são estimativas parametrizadas, e a data e a origem das tarifas ficam registradas para atualização.

**Tela:** Skill é orientação reutilizável; não desbloqueia tokens nem altera cobrança.

## 22. Teste, compare, mantenha o que funciona

Agora aplique o método a uma tarefa real e pequena. Defina o resultado esperado e os arquivos necessários. Veja o modelo, o esforço e o modo de velocidade disponíveis. Registre os indicadores que você consegue observar. Execute com saídas proporcionais e confira a entrega. Na próxima tarefa equivalente, teste uma mudança e compare. Se a divisão entre modelos fizer sentido, use instruções delimitadas e preserve as evidências na passagem. Se o contexto estiver grande, decida entre continuidade, compactação e uma nova sessão. O importante é manter um processo que você consiga explicar e repetir. Você não precisa decorar todas as tarifas: precisa saber onde conferir e como medir. Use o kit, ajuste ao seu ambiente e avalie sempre o resultado completo.

**Tela:** Economia útil = menos desperdício por resultado aprovado.