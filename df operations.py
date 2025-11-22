# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 08:40:18 2025

@author: B MACHOLA
"""

import pandas
df = pandas.read_csv("cars.csv")
'''print(df[['Car','Model','Volume']][10:14])
print(df.iloc[21:26])
print(df.iloc[[0,2,4,7]])
print(df.iloc[10,3])'''

'''print (df.loc[df.Car=='Audi'])
''df1=df.loc[df.Car=='Audi']
''df1.to_csv("C:/Users/B MACHOLA/Desktop/oact36/Cars1.csv")'''

for index, row in df.iterrows():
    if (row['Car']=='Audi'):
        print(row)
        
'''df2=df.sort_values('Volume')'''

''''df3=df.sort_values('Volume', ascending=False)'''
'''df1=df.drop(columns=['CO2'])'''
df['Total'] =df.iloc[:,2:4].sum(axis=1)
print(df.sort_values(['Car','Volume'],ascending=[1,0]))

'''OR OPERATOR'''
df3=df.loc[(df['Car']=='Ford')| (df['Volume']==1600)]

'''replace or Add new'''
df.loc[8]=['TATA','NEXON',2000,1800,125,3800]
df.loc[36]=['MAHESH','Citigo',1000,929,95,1929]

'''DELETE A GIVEN RW'''
df= df.drop([36])


'''APPEND A NEW ROW'''
