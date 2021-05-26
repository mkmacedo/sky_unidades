import pandas as pd
import csv
import re
import numpy as np

df = pd.read_csv(r'paranormalizar.csv')

#df.to_csv(r'paranormalizar.csv', index=None, header=True)

col = ['nome', 'unidade']
df = df[col]
print(df.head())

#print(df['nome'])
#df = df.unique()
#print(df)
df['id'] = df['unidade'].factorize()[0]


for i in range(50):
    data = df.loc[i,['unidade', 'id']]
    print(data)

units = df['unidade'].unique()
print(units)
units_list = [u for u in units]
print(units_list)
units_raw = []

for u in units_list:
    if(type(u) == str):
        x = re.search(r'[a-zA-Z]+', u)
        if x != None:
            units_raw.append(x.group())

print(units_raw)

df['unidade_encontrada'] = np.nan
for i in range(1000):
    flag = False
    for un in units_raw:
        s = ' '+df.loc[i, 'nome']+' '
        r = r' [0-9]*{} | [0-9]* {} |[0-9]+{}|[0-9]* {} '.format(un, un, un, un)
        x = re.search(r, s)
        if x != None:
            x = x.group()
            df.loc[i, 'unidade_encontrada'] = un
            flag = True
            break
    if flag == False:
        df.loc[i, 'unidade_encontrada'] = 'UN'
print(df)
df.head(1000).to_csv("final.csv")

#pattern = r' KG| UN| '

#x = re.search(r' KG
#print(df.head(100))

