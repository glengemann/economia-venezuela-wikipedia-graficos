import pandas as pd
import matplotlib.pyplot as plt

file = '/home/prometeo/ProyectoGit/bcv/xls/tasas_sistema_bancario_full.xls'
df = pd.read_html(
    file,
    thousands='.',
    decimal=',',
)[0]

df.dtypes
df['Fecha del Indicador'] = pd.to_datetime(df['Fecha del Indicador'], format='%d-%m-%Y', utc=True)

df['Promedio'] = df.mean(axis=1)

# ['Fecha del Indicador', 'Banco', 'Compra', 'Venta']
df[0:10].set_index('Fecha del Indicador')[['Banco','Promedio']].plot(kind='line')
df[0:10]

## Line
date_mean = df.groupby('Fecha del Indicador', axis=0).mean()
date_mean['Promedio'].plot(kind='line')

## Banks
banks = df['Banco'].tolist()
banks = list(dict.fromkeys(banks))

# Bar
df.groupby('Fecha del Indicador', axis=0).plot(kind='bar')

## filter
filter = df['Banco'] == 'Banesco'
df_banesco = df[filter]

df_banesco.set_index('Fecha del Indicador', inplace=True)
df_banesco.sort_index(ascending=True, inplace=True)
df_banesco.plot(kind='bar')


df.set_index('Fecha del Indicador', inplace=True)
df.reset_index(inplace=True)
df[['Fecha del Indicador','Banco','Promedio']].transpose()
