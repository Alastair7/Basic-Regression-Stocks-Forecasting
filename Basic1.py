import pandas as pd
import quandl
import  numpy as np
quandl.ApiConfig.api_key = 'e6EQQ4ksArJmyPo6YVy5'
Dataframe = quandl.get_table('WIKI/PRICES')

Dataframe=Dataframe[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
print(Dataframe.head())
Dataframe['Percentage']=(Dataframe['adj_high']-Dataframe['adj_close'])/Dataframe['adj_close']*100.0
Dataframe['change']=(Dataframe['adj_close']-Dataframe['adj_open'])/Dataframe['adj_open']*100.0
Dataframe=Dataframe[['adj_open','Percentage','change','adj_close','adj_volume']]

print(Dataframe.head())

