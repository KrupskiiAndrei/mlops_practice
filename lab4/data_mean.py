import pandas as pd
df = pd.read_csv('datasets/data_1.csv')
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
df.to_csv('datasets/data_2.csv', index=False)
