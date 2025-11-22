# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 08:59:02 2025

@author: B MACHOLA
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Get list of all files inside sales_data folder
files = [file for file in os.listdir('./sales_data')]

all_months = pd.DataFrame()

# Read and merge all monthly sales data
for file in files:
    df = pd.read_csv('./sales_data/' + file)
    all_months = pd.concat([all_months, df])

# Save combined data into one CSV
all_months.to_csv('all_data.csv', index=False)

# Load the merged data
all_data = pd.read_csv('all_data.csv')

# Drop rows with missing values
all_data = all_data.dropna(how='all')

# Remove invalid 'Order Date' rows
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Extract day from 'Order Date'
all_data['date'] = all_data['Order Date'].str[3:5]
all_data['date'] = all_data['date'].astype('int32')


# Convert columns to numeric
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# Create a new column: Sales = Quantity × Price
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

# Group by date to calculate total sales per day
results = all_data.groupby('date').sum()

# Plot results
dates = range(1, 32)  # Days in a month
plt.bar(dates, results['Sales'])
plt.xlabel('Date of the month')
plt.ylabel('Sales in USD')
plt.show()

