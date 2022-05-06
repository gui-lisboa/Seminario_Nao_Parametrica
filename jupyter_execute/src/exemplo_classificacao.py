#!/usr/bin/env python
# coding: utf-8

# # Classificação

# ## Nível de Adaptação de Estudantes no EAD
# 
# https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education

# In[1]:


from utils import carrega_dataset_EAD

dataset = carrega_dataset_EAD()
dataset


# ## Codificação
# 

# In[2]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder

codificadores = {coluna: LabelEncoder() for coluna in dataset.columns}
dataset_codificado = pd.DataFrame()

for coluna in dataset:
    dataset_codificado[coluna] = codificadores[coluna].fit_transform(dataset[coluna])

dataset_codificado


# ## Modelo

# In[3]:


from sklearn.ensemble import RandomForestClassifier

X = dataset_codificado.iloc[:, 1:13]
modelo = RandomForestClassifier(oob_score=True)
fit = modelo.fit(X, dataset_codificado['Adaptivity Level'])


# ## Importâncias

# In[4]:


import numpy as np
import seaborn as sns

sns.set_theme()
sns.set_theme("notebook")
sns.set(rc={"figure.figsize": [10, 6]})

desvio_padrao_estimadores = np.std(
    [arvore.feature_importances_ for arvore in modelo.estimators_], axis=0)

importancias = pd.Series(modelo.feature_importances_,
                         index=modelo.feature_names_in_)
importancias.plot.bar(yerr=desvio_padrao_estimadores);


# # Visualização de uma única árvore

# In[5]:


from sklearn import tree

tree.plot_tree(modelo.estimators_[0],
               feature_names=modelo.feature_names_in_.tolist(),
               class_names='Adaptivity Level',
               filled=True);


# In[6]:


texto = tree.export_text(modelo.estimators_[0],
                         feature_names=modelo.feature_names_in_.tolist())

print(texto)

