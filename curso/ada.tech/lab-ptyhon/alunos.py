import pandas as pd
import random
df = pd.read_csv('doc/alunos.csv', sep=';')
lis  = df['Nome'].tolist()
print(lis)

df["Prova_5"] = [random.randint(0, 10) for _ in range(df.shape[0])]
df["Prova_5"]
print(df)
