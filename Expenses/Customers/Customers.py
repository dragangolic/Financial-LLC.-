import pandas as pd


data = pd.read_csv("Clients.csv")
pd.set_option('display.max_columns', None)

# Importing new columns
billing = ['1200', '3200', '13421', '1789', '4009']
data['billing'] = billing
print(data)

