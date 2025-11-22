
import pandas as pd
import os
import matplotlib.pyplot as plt

df=pd.read_csv('./sales_data/sales_april_2019.csv')

files= [file for file in os.listdir('./sales_data')]

all_months=pd.DataFrame()

for file in files:
    df=pd.read_csv('./sales_data/'+file)
    all_months=pd.concat([all_months,df])
    
all_months.to_csv('all_data.csv', index=False)
all_data=pd.read_csv('all_data.csv')
all_data=all_data.dropna(how='all')
all_data=all_data[all_data['Order Date'].str[0:2]!='Or']
all_data['Month']=all_data['Order Date'].str[0:2]
all_data['Month']=all_data['Month'].astype('int32')

all_data['Quantity Ordered']=pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each']=pd.to_numeric(all_data['Price Each'])                  
all_data['Sales']= all_data['Quantity Ordered']*all_data['Price Each']                

def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City']=all_data['Purchase Address'].apply(lambda x: get_city(x)+'('+get_state(x)+')')

results=all_data.groupby('City').sum()

cities=[city for city, df in all_data.groupby('City')]
plt.bar(cities,results['Sales'])
plt.xticks(cities,rotation='vertical',size=8)
plt.ylabel('sales in usd')
plt.xlabel('city name')

