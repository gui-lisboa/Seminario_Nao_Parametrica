#!/usr/bin/env python
# coding: utf-8

# # Regressão

# In[1]:


from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn import metrics
from utils import carrega_dataset_boston_housing
import seaborn.apionly as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import graphviz

data = carrega_dataset_boston_housing()
data.drop(['Unnamed: 0'], axis=1, inplace=True)

data


# In[2]:


corr = data.corr()

corr


# In[3]:


sns.set_theme()
sns.set_theme("notebook")
sns.set(rc={"figure.figsize": [10, 6]})

sns.heatmap(corr);


# ## Separação de dados em treino e teste, e seleção de variáveis

# In[4]:


y = data[["medv"]]
X = data.loc[:,['indus','tax','ptratio', 'lstat', 'rm']]
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=999)


# # Algoritmo de árvores de decisão

# In[5]:


treereg = DecisionTreeRegressor(random_state=999, max_depth = 3, criterion = "squared_error")


# In[6]:


treereg.fit(X_train, y_train)

dot_data = export_graphviz(treereg, feature_names=list(X.columns),  
                           filled=True, rounded=True)  

graph = graphviz.Source(dot_data)
graph.render("tree")
graph


# In[7]:


y_pred_tree = treereg.predict(X_test)

df=pd.DataFrame({'Actual':y_test.iloc[:,0], 'Predicted':y_pred_tree})

treemse = metrics.mean_squared_error(y_test, y_pred_tree)
treemae = metrics.mean_absolute_error(y_test, y_pred_tree)

print('Mean Squared Error:', treemse)
print('Mean Absolute Error:', treemae)



# # Random Forest

# In[8]:


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 999, max_depth = 3)

# Train the model on training data
rf.fit(X_train, y_train.iloc[:,0])

predictions = rf.predict(X_test)

rfmse =  metrics.mean_squared_error(y_test, predictions)
rfmae = metrics.mean_absolute_error(y_test, predictions)

print('Mean Squared Error:', rfmse)
print('Mean Absolute Error:', rfmae, "\n")
print('Mean Squared Error Reduction ratio:', 1 - (rfmse/treemse))
print('Mean Absolute Error Reduction ratio:', 1 - (rfmae/treemae))

