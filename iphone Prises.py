# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:10:53 2025

@author: B MACHOLA
"""

import pandas as pd
import os
import matplotlib.pyplot as plt


# -- coding: utf-8 --
"""
Created on Thu Sep  4 12:13:11 2025

@author: phyo
"""
'''
Question => About the gain of iPhone selling. In a condition is that at the day from 26th to 31st 
in one month, iPhone price is 10% discount but at the day from 1st to 25th in one month, 
iPhone price is 4% increase. For example, if iPhone price is $1200, so from 26th to 31st is $1080 and 
from 1st to 25th is $1248. So please write codes for iPhone gain by python.
'''

df = pd.read_csv('all_data.csv')

iphone_df = df[df['Product'].str.contains("iPhone", case = False, na = False)].copy()# Keep only iPhone sales

iphone_df['Order Date'] = pd.to_datetime(iphone_df['Order Date'], format="mixed")## Convert Order Date to datetime

iphone_df['Day'] = iphone_df['Order Date'].dt.day#extract day

iphone_df['Quantity Ordered'] = pd.to_numeric(iphone_df['Quantity Ordered'],errors='coerce')#convert to numeric
iphone_df['Price Each'] = pd.to_numeric(iphone_df['Price Each'], errors='coerce')

def adjust_price(row): #apply price rules
    if 1 <= row['Day'] <= 25:
        return row['Price Each'] * 1.04   # 4% increase
    else:
        return row['Price Each'] * 0.90   # 10% discount

iphone_df['Adjusted Price'] = iphone_df.apply(adjust_price, axis=1)

# Compute gain
iphone_df['Gain'] = (iphone_df['Adjusted Price'] - iphone_df['Price Each']) * iphone_df['Quantity Ordered']
total_gain = iphone_df['Gain'].sum()#total gain

print(f"Total iPhone gain: ${total_gain:,.2f}")