# %% 
import pandas as pd

df = pd.read_excel("dados_frutas.xlsx")
df
# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier()
y = df['Fruta']

caracteristicas = ["Arredondada","Suculenta", "Vermelha", "Doce"]

X = df[caracteristicas]
arvore.fit(X, y)