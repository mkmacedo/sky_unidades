

import pandas as pd

df = pd.read_json("jlfile.json")

col = ['brand', 'gtin']
df = df[col]

length = len(df['brand'])
x = df['gtin']
for i in range(length):
    brand = df.loc[i, 'brand']
    gtin = df.loc[i, 'gtin']
    brand = str(brand)
    if(str(gtin) != 'nan'):
        ean = str(gtin[0].get('value'))
        print(brand+' ===========> '+ean)
