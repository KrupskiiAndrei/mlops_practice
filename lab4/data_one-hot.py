import pandas as pd
df = pd.read_csv('datasets/data_2.csv')
one_hot = pd.get_dummies(df['Sex'])
df = pd.concat([df, one_hot], axis=1)
df.to_csv('datasets/data_3.csv', index=False)
