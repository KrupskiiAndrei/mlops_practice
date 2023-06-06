from catboost.datasets import titanic
import pandas as pd

train_df, test_df = titanic()
train_df.to_csv('datasets/data.csv', index=False)
