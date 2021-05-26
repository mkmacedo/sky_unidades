import pandas as pd
import csv
import re
import numpy as np

df = pd.read_csv(r'paranormalizar.csv')

class Unidades:
    def __init__(self, df):
        self.df = df
        self.col = ['nome', 'unidade']
        self.df = self.df[self.col]

        self.units = self.df['unidade'].unique()
        self.units_list = [u for u in self.units]
        self.units_raw = []

        for u in self.units_list:
            if(type(u) == str):
                x = re.search(r'[a-zA-Z]+', u)
                if x != None:
                    self.units_raw.append(x.group())

        self.df['unidade_encontrada'] = np.nan

    def get_units(self):
        for i in range(1000):
            flag = False
            for un in self.units_raw:
                s = ' '+self.df.loc[i, 'nome']+' '
                r = r' [0-9]*{} | [0-9]* {} |[0-9]+{}|[0-9]* {} '.format(un, un, un, un)
                x = re.search(r, s)
                if x != None:
                    x = x.group()
                    self.df.loc[i, 'unidade_encontrada'] = un
                    flag = True
                    break
            if flag == False:
                self.df.loc[i, 'unidade_encontrada'] = 'UN'

        self.df.head(1000).to_csv("unidades_encontradas.csv")

unid = Unidades(df)
unid.get_units()
