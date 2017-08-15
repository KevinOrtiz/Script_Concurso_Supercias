
# coding: utf-8

# In[1]:
import os
os.chdir('C:/Users/pablo/Google Drive/ESPOL/Concurso Supercias/fb_data')
    
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fb_functions as fb
import seaborn as sns


# In[2]:

lista_empresas = ['claroecua', 'movistarecu', 'marathonsportsec', 'cntecuador',
                  'chevroletecuador', 'cocacolaec', 'directvla', 'latamecuador',
                  'quicentroshopping', 'sanmarinogye', 'galletasamorecuador', 'nescafe.ec',
                  'almacenesdeprati', 'tiaec', 'bancoguayaquil', 'bancopacificoec',
                  'bancobolivariano', 'kfcecuador', 'mcdonaldsecuador', 'bancopichinchaecuador',
                  'NissanEcuador', 'pronacatqma', 'aviancaenecuador', 'cinemarkecuador',
                  'supercines', 'pilsenerec', 'clubpremiumec', 'grupotvcableec',
                  'netlife.ecuador', 'pepsiecuador', 'yanbal.ec', 'huaweimobileec']

data_empresas={}
for empresa in lista_empresas:
    data_empresas[empresa] = fb.data_post_empresa(empresa)


# In[3]:

hola = fb.comment_empresa('claroecua')
hola.tail()


# In[4]:

finance = pd.read_csv('empresa_finance.csv')
finance.drop(['Expediente', 'CIIU', 'Fecha constitucion'], axis=1, inplace=True)
finance.set_index(keys='Nombre', inplace=True)
finance.tail()


# In[103]:

df_suma = pd.DataFrame(columns=['Likes', 'Shares', 'Comments'])
for empresa in data_empresas:
    serie_suma = data_empresas[empresa].sum(axis=0)
    serie_trans = serie_suma.to_frame().unstack().unstack()
    serie_trans.drop('Post_id', axis=1, inplace=True)
    serie_trans['empresa'] = empresa
    serie_trans.set_index(keys='empresa', inplace=True)
    df_suma = pd.concat([df_suma, serie_trans])

data_fb = df_suma.join(finance)


# In[104]:

corr = data_fb.corr('spearman')

cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)

def magnify():
    return [dict(selector="th",
                 props=[("font-size", "7pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])
]

corr.style.background_gradient(cmap, axis=1)    .set_properties(**{'max-width': '80px', 'font-size': '10pt'})    .set_caption("Hover to magify")    .set_precision(2)    .set_table_styles(magnify())

