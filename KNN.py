#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier
from warnings import simplefilter
from sklearn.ensemble import GradientBoostingClassifier
from pandas import DataFrame

simplefilter(action='ignore', category=FutureWarning)

header_names=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
df = pd.read_csv('crx.data',names=header_names)
        
df.head()   


# In[17]:


df.describe()


# In[32]:


df = df.replace('?',np.nan)

def fix_missing_mean(df,col):
    df[col] = pd.to_numeric(df[col], errors = 'coerce')
    df[col].fillna(df[col].mean(), inplace = True)    

def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill') 


fix_missing_ffill(df,'A')
fix_missing_ffill(df,'B')
fix_missing_ffill(df,'D')
fix_missing_ffill(df,'E')
fix_missing_ffill(df,'F')
fix_missing_ffill(df,'G')
fix_missing_mean(df,'N')


y = df['P']
features = df.drop(['P'], axis=1)

object_cols = ['A','B','D','E','F','G','I','J','L','M','N']

X = features.copy()
ordinal_encoder = OrdinalEncoder()
X[object_cols] = ordinal_encoder.fit_transform(features[object_cols])
      

# Inicio do uso KNN

train_acc=[]
test_acc=[]
list_score=[]

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.30, random_state=2)

for i in range(2, 20):
    knn = KNeighborsClassifier(n_neighbors=i)

    knn.fit(xTrain,yTrain)

    train_predict = knn.predict(xTrain)
    test_predict = knn.predict(xTest)

    test_acc = accuracy_score(yTest, test_predict)
    train_acc = accuracy_score(yTrain, train_predict)
    print('Pontuação de Treino:',train_acc,'Pontuação de Teste:',test_acc)
    print(i,'Pontuação de Treino:',train_acc,'Pontuação de Teste:',test_acc)

    list_score.append([i,accuracy_score(train_predict, yTrain),accuracy_score(test_predict, yTest)]) 
    

df3 = DataFrame (list_score,columns=['n_neighbors','Train Accuracy','Test Accuracy'])
plt.plot(df3['n_neighbors'],df3['Test Accuracy'],label='Test Accuracy')
plt.plot(df3['n_neighbors'],df3['Train Accuracy'],label='Train Accuracy')
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.legend()  


# In[ ]:




