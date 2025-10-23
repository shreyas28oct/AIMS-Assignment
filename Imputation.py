import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Person': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Age': [17, 17, 18, 18, 19, np.nan],
    'Rank': [5000, 6000, np.nan, 21000, 3400, 7500],
    'Branch': ['IT', 'MnC', np.nan, 'EP', 'CSE', 'MnC']  
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print()

# FInding mean for age

mean_age = df['Age'].mean()
for i in range(len(df)):
    if pd.isna(df.loc[i, 'Age']):
        df.loc[i, 'Age'] = mean_age

print("After Mean Imputation for Age:")
print(df)
print()

# Finding median for rank

median_rank = df['Rank'].median()
for i in range(len(df)):
    if pd.isna(df.loc[i, 'Rank']):
        df.loc[i, 'Rank'] = median_rank

print("After Median Imputation for Rank:")
print(df)
print()

#Finding mode for branch

mode_branch = df['Branch'].mode()[0]

for i in range(len(df)):
    if pd.isna(df.loc[i, 'Branch']):
        df.loc[i, 'Branch'] = mode_branch

print("After Mode Imputation for Branch:")
print(df)
