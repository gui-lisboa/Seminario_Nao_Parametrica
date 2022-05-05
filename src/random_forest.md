# Random Forest

## Descrição

Essencialmente Random Forests são constituidas de um grande conjunto de árvores de decisões. Os conceitos são similares, porém a aplicabilidade, flexibilidade e precisão são diferentes. A motivação por trás do uso do Random Forest está no fato de as árvores de decisão sofrerem com uma elevada variância. Como estabelecem James, Witten, Hastie e Tibshirani (2017), para o caso de separação em amostra de treinamento e teste, as árvores de decisão tendem a ter resultados muito diferentes em termos de desempenho em cada uma das amostras, sendo alguns de seus benefícios a simplicidade de interpretação e análise.

O Random Forest é pensado para solucionar tal problema, combinando a simplicidade das árvores de decisão com uma flexibilidade advinda da utilização de uma série de árvores de decisão não correlacionadas e construídas à partir de conjuntos simulados de dados extraídos do conjunto original denominados "bootstrap".

Um conjunto bootstrap é um amostra (ou conjunto de dados) advinda dos dados originais que poderá ser do mesmo tamanho que dos dados originais e que poderá, inclusive, ter linhas repetidas. Desta forma, a seleção para compor a amostra bootstrap é aleatória com reposição.

Conforme explicam James, Witten, Hastie e Tibshirani (2017) cada vez que uma divisão em uma árvore é considerada uma amostra aleatória de m preditores são escolhidos como candidatos. Conforme estabelecem James, Witten, Hastie e Tibshirani (2017) uma amostra de m preditores é tomada a cada split e, tipicamente, se toma $m=\sqrt(p)$ preditores para compor a amostra de cada split.

Tal procedimento evita que as árvores formadas pelo algoritmo sejam muito parecidas, evitando que as árvores sejam fortemente correlacionadas.

## Criação da floresta

Para criar o Random Forest, para cada conjunto bootstrap retirado dos dados originais será criada uma árvore, utilizando um subconjunto aleatório de variáveis em cada passo da árvore. Usualmente o número de variáveis utilizada inicialmente é a raiz quadrada do número de variáveis do conjunto de dados. Assim, o primeiro nó não considera todas as variáveis presentes no conjunto bootstrap, mas apenas uma fração delas à partir da qual se selecionará a primeira para divisão (split) considerando aquela com melhor desempenho na separação das amostras como o primeiro nó.

A cada "step" são selecionadas aleatoriamente um conjunto de colunas (variáveis) das que "restaram" no subconjunto bootstrap e construidos os "splits" de cada nó até se chegar à folha (critério de parada). O número de variáveis utilizado para decisão em cada nó poderá alterar a estrutura da árvore, resultando em uma alteração da acurácia do Random Forest posteriormente.

Usualmente, são testadas diferentes parâmetros de tunagem para então escolher o Random Forest com maior acurácia.

Tal procedimento resulta em um grande número de diferentes árvores de decisão. Da forma de construção e do número de árvores geradas à partir do processo advém o nome "Random Forest".

## Julgamento e decisão

A forma de estimação de uma resposta desejada em cada uma das árvores é bastante parecida com a da árvore de decisão. Neste caso, cada amostra de teste (ou treinamento) tem sua resposta estimada por cada uma das k árvores de decisão geradas, isto é, os i-ésimo indivíduo terá sua resposta estimada por cada uma das k-ésimas árvores. No caso de um problema de classificação, cada uma dessas árvores gerarão uma resposta única binária positiva ou negativa, sendo os julgamentos de cada árvore somados.

Caso o número de julgamentos positivos seja maior que o número de julgamentos negativos, a resposta estimada para a amostra i será positiva. Caso contrário, a amostra i terá sua resposta estimada como negativa. Dito de outra forma, a opção (positiva ou negativa) que recebeu maior número de votos é declarada a opção vencedora e será aquela estimada para a resposta da amostra.

Este processo é chamado de "Bagging" ou "bootstrap agregation". Tal conceito vem do fato de se utilizar um processo de bootstrap para rearranjar aleatoriamente os dados e utilizar um critério de agregação (votos) para tomada de decisão.

## Acurácia na predição e OOB

Nem todas as amostras presentes no conjunto de dados original serão utilizadas para a formação dos conjuntos de dados bootstrap. O subconjunto das amostras do conjunto original não empregadas para a formação dos conjuntos bootstrap são chamadas de Out of Bagging - OOB. As amostras OOB presentes no conjunto original são, então, empregadas para se estimar as respostas de todas as outras árvores construídas sem tais amostras. Novamente o processo de agregação indicará qual a classe ou resultado estimado para a resposta das amostras OOB.

Uma medida amplamente empregada para se analisar a acurácia do Random Forest é a proporção de OOB corretamente classificadas pelo Random Forest. Já a proporção dos resultados para os quais as amostras OOB foram incorretamente classificadas, isto é, para os quais a agregação dos votos indicou uma classe ou resposta incorreta, dar-se-á o nome de Erro OOB.

É possível utilizar tais medidas para refinamento da estrutura de geração das árvores, empregando um subconjunto de covariáveis de tamanho m distinto do inicial (maior ou menor).

Com isso, a estrutura das árvores será diferente da estrutura inicialmente utilizada, gerando nós e splits distintos, o que, consequentemente resultará em árvores diferentes e em julgamentos diferentes.

## Referências

James, G. Witten, D., Hastie, T., Tibshirani, R. An introduction to Statistical Learning: with applications in R. New York, Springer, 2017.
