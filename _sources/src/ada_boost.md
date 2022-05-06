# Adaptative Boosting (ADABoost)

## Descrição

É um modelo de Random Forest com árvores fracas, com apenas um nó, chamadas de tocos (stumps). Cada toco recebe um fator de correção a partir do toco anterior.

$$
    E_t = \sum_i E[F_{t-1}(x_i) + \alpha_t h(x_i)]
$$

## Pesos dos tocos

O peso de cada toco é corrigido pela sua acurácia.

$$
    \alpha = \eta \frac{1 - TotalErros}{TotalErros}
$$

## Pesos das amostras

Amostras que foram classificadas de maneiro incorreta tem o seu peso aumentado, já as árvoes classificadas corretamnte pelo modelo tem seu peso diminuido.

$$
    \begin{gather}
        Peso = Peso_{t-1}e^{\alpha} \\
        Peso = Peso_{t-1}e^{-\alpha} \\
    \end{gather}
$$
