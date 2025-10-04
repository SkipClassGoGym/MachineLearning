import pandas as pd 
df =pd.read_json("data_set\SalesTransactions\SalesTransactions.json",
                encoding ='utf-8', dtype='unicode')

print(df)
