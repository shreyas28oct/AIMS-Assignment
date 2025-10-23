import pandas as pd
import numpy as np

#Sample dataset
snacks = ['Samosa', 'Pani Puri', 'Vada Pav', 'Chaat', 'Kachori', 'Samosa', 'Vada Pav']
df = pd.DataFrame({'Snack': snacks})
print("Original Data:")
print(df)
print()
unique_snacks = df['Snack'].unique()
print("Unique Snacks:")
print(unique_snacks)
print()
#Creating empty columns for each snack
for snack in unique_snacks:
 df[snack] = 0 
#Filling 1 where snack matches
for i in range(len(df)):
    for snack in unique_snacks:
        if df.loc[i, 'Snack'] == snack:
            df.loc[i, snack] = 1
print("After One-Hot Encoding:")
print(df)
