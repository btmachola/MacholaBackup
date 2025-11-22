import pandas as pd
import os
import matplotlib.pyplot as plt

files= [file for file in os.listdir('./sales_data')]

all_months=pd.DataFrame()

for file in files:
    df=pd.read_csv('./sales_data/'+file)
    all_months=pd.concat([all_months,df])
    
all_months.to_csv('all_data.csv', index=False)

all_data=pd.read_csv('all_data.csv')
all_data=all_data.dropna(how='all')
all_data=all_data[all_data['Order Date'].str[0:2]!='Or']
all_data['Order Date']=pd.to_datetime(all_data['Order Date'])
all_data['Hour']=all_data['Order Date'].dt.hour
hours=[hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours,all_data.groupby(['Hour']).count())
plt.ylabel('number of sales')
plt.xlabel('hour number')


