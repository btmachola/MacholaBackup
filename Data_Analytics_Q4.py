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

df=all_data[all_data['Order ID'].duplicated(keep=False)]  
df['Grouped']=df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

from itertools import combinations
from collections import Counter

count=Counter()
for row in df['Grouped']:
    row_list=row.split(',')
    count.update(Counter(combinations(row_list,2)))
    
print(count)



