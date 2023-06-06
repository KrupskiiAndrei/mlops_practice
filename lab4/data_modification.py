import pandas as pd
df = pd.read_csv('datasets/data.csv')
df = df[['Pclass', 'Sex', 'Age']]
df.to_csv('datasets/data_1.csv', index=False)
