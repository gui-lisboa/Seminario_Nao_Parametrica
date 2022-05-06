# Árvores de Decisão

## Definição

Diagrama que representa uma sequência de decisões binárias com o objetivo de obter uma resposta. Apesar de ter interpetração fácil, uma única árvore de decisão tem ótimo desempenho com os dados usados na sua contrução, mas é, quando comparada com outros métodos de classificação ou regressão, consideravelmente imprecisa.

## Sequências de decisões

Para decidir qual atributo deve ser usado como critério de decisão em um nó, devemos mensurar o grau de impureza de Gini.

$$
    Gini(D) = 1 - \sum_{i=1}^{k}p_{i}^{2}
$$

O atributo escolhido deve ser aquele com menor índice de impureza, ou seja, aquele que melhor sapara a resposta. Ao dividr o fluxo usando uma variável qualquer $A$, é possível que o número de observações que sejam levadas aos subgrupos $D_1$ e $D_2$ seja diferente. Nestes casos, devemos aplicar um peso no índice de impureza, onde $n$ é o total de observações sob a variável $A$ e $n_1$ e $n_2$ são o número de observações que serão colocadas nos subgrupos $D_1$ e $D_2$

$$
    Gini_{A}(D) = \frac{n_1}{n}Gini(D_1) + \frac{n_2}{n}Gini(D_2)
$$

Ganho de Gini

$$
    \Delta Gini(A) = Gini(D) - Gini_{A}(D)
$$
