# Imputação de dados

## Dados para treinamento incompletos

Inicialmente, imputamos um valor esperado para um atributo faltante considerando apenas qual o valor esperado dada a resposta, por exemplo:

```{figure} ./imagens/dados_incompletos_treinamento_antes.PNG
---
height: 500px
name: directive-fig
---
Dados de treinamento faltantes.
```

```{figure} ./imagens/dados_incompletos_treinamento_chute_inicial.PNG
---
height: 500px
name: directive-fig
---
"Chute" inicial utilizando valores esperados para os atributos considerando a variável resposta.
```

Após executar todas as árvores novamente, agora utilizando os chutes iniciais, contamos quais outras linhas foram categorizadas na mesma folha e usamos essa proximidade como pesos para definir quais valores devem ser imputados.

```{figure} ./imagens/matriz_de_proximidade_10_arvores.PNG
---
height: 500px
name: directive-fig
---
Matriz de proximidade. Linha 3 deve ter peso maior na decisão de valores que devem ser atribuídos a linha 4.
```

Assim, podemos rodar o modelo quantas vezes forem necessárias até que os valores imputados não sofram variações significativas.

## Dados de classificação incompletos

Caso seja necessário fazer imputação de dados que desejamos classificar, uma opção é duplicar o dado e avaliar com qual imputação o modelo é mais preciso.

```{figure} ./imagens/dados_incompletos_durante_classificação_copia1.PNG
---
height: 200px
name: directive-fig
---
Cópia com resposta Yes
```

```{figure} ./imagens/dados_incompletos_durante_classificação_copia2.PNG
---
height: 200px
name: directive-fig
---
Cópia com resposta No
```
