%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pip3 install xlrd
file_2001 = '/home/prometeo/ProyectoGit/ine/2001/csv/migracion.csv'
df_2001 = pd.read_csv(file_2001)
df_2001.rename(columns={'Casos':'2001'}, inplace=True)

file_2011 = '/home/prometeo/ProyectoGit/ine/2011/xls/migracion.xls'
df_2011 = pd.read_excel(
    file_2011,
    skiprows=3,
    skipfooter=7,
    usecols=['Pais de Nacimiento','Casos']
    # nrows=10
)
df_2011.rename(columns={'Casos':'2011'}, inplace=True)

merge = pd.merge(df_2001, df_2011, on='Pais de Nacimiento', how='outer')

merge['Total'] = merge.sum(axis=1)
merge.set_index('Pais de Nacimiento', inplace=True)
merge.sort_values(['Total'], ascending=False, axis=0, inplace=True)


#### Line
years = [map(str, range(2001,2011))]
df_colombia = merge['Pais de Nacimiento']=='Colombia'
df_colombia = merge[df_colombia]
df_colombia.rename(columns={'2001_x':'2001', '2001_y':'2011' }, inplace=True)

df_colombia.loc['Colombia']

df_colombia.loc['Colombia',['2011','2011']]
df_colombia.plot(kind='line')
plt.title('Immigration from Colombia')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()

### Area Plots
merge.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = merge.head()
years = ['2001', '2011']
df_top5 = df_top5[years].transpose()
ax = df_top5.plot(
    kind='area',
    alpha=.35,
    figsize=(20,10),
    stacked=False    
)

ax.set_title('Immigrant trend of top 5 countries')
ax.set_ylabel('Numbers of imigrants')
ax.set_xlabel('Years')

### Histograms
merge['2001']
merge['2011'].dropna(inplace=True)
count, bin_edges = np.histogram(merge['2011'])

merge['2011'].plot(
    kind='hist',
    figsize=(8, 5),
    xticks=bin_edges
)

plt.title('Histogram of Immigration from  countries in ') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()

## 
years
dfTop4 = merge.loc[['Colombia','Espa�a','Portugal','Italia'], years]
dfTop4 = merge.loc[['Espa�a','Portugal','Italia'], years]
dfTop4Trans =  dfTop4.transpose()

count, bin_edges = np.histogram(dfTop4Trans, 3)
xmin = bin_edges[0] - 1000
xmax = bin_edges[-1] + 1000

dfTop4Trans.plot(
    # figsize=(10,6),
    kind='hist',
    alpha=0.3,
    bins=4,
    color=['coral', 'darkslateblue', 'mediumseagreen'],
    stacked=True,
    xlim=(xmin, xmax),
    xticks=bin_edges
)
plt.title('Histogram of Immigration from Colombia, Spain, Portugal and Italy from 2001 - 2011')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

import matplotlib
for name, hex in matplotlib.colors.cnames.items():
    print(name, hex)

### Bar Charts
merge.sort_values(['Total'], ascending=False, axis=0, inplace=True)
bar = merge[2:].drop('Total', axis=1).dropna().head()

bar.plot(kind='bar')

plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')


##
bar = merge.dropna()
bar.loc[['Colombia','Espa�a'], ['2001','2011']].transpose().plot(
    kind='bar',
    figsize=(10, 6)
)
# bar.loc[['Colombia'], ['2001','2011']].transpose().plot(
#     kind='bar',
#     figsize=(10, 6)
# )
# Annotate arrow
plt.annotate(
    '',
    xy=(1,700000),
    xytext=(0,600000),
    xycoords='data',
    arrowprops=dict(
        arrowstyle='->',
        connectionstyle='arc3',
        color='blue',
        lw=2
    )
)
# Annotate Text
plt.annotate(
    'Crisis',
    xy=(0,650000),
    rotation='15',
    va='bottom',
    ha='left'
)
plt.show()


### Bar Horizontal
barh = merge.dropna().head(15)
barh[['2001','2011']].plot(
    kind='barh',
    figsize=(12, 12),
)

barh['Total'][1:].plot(
    kind='barh',
    figsize=(12, 12),
    # color='steelblue'
)

for index, value in enumerate(barh['Total'][1:]):
    label = format(int(value), ',')
    # print("{}".format(index))
    # print("{}".format(label))
    plt.annotate(label, xy=(value - 13000, index - 0.10))

# plt.annotate('144000', xy=(144000-13000, 0-0.1))
plt.show()

### Pie Charts
merge['2011'].head().plot(
    kind='pie',
    autopct='%1.2f%%',
    startangle=90
)

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen','pink','maroon','navy','slategrey','black']
explode_list = [0, 0.2, 0.3, 0.3, 0.3,0.3,0.3,0.3,0.3,0.3] # ratio for each continent with which to offset each wedge.

merge['Total'].head(8).plot(
    kind='pie',
    figsize=(15,6),
    autopct='%1.2f%%',
    startangle=90,
    shadow=True,
    labels=None,
    pctdistance=1.12,
    # explode=explode_list,
    # colors=colors_list
)
plt.axis('equal')
plt.legend(labels=merge.head(8).index, loc='upper left')


### Box Plot
df_colombia = merge.loc['Colombia', ['2001','2011']].transpose()
# merge.loc['Colombia', ['2001','2011']].transpose()

df_colombia.plot(kind='box')


### Scatter Plot
df_total = pd.DataFrame(merge[['2001','2011']].sum(axis=0))
df_total.index = map(int, df_total.index)
df_total.reset_index(inplace=True)
df_total.columns = ['year', 'total']
# df_total = merge[['Total']]

x = df_total['year']
y = df_total['total']
fit = np.polyfit(x, y, deg=1)
plt.plot(x, fit[0] * x + fit[1], color='red')

fit[0] * 2012 + fit[1]

df_total.plot(kind='scatter', x='year', y='total', color='darkblue')