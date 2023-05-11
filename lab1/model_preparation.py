from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

df_train = pd.read_csv('lab1/train/data_scaled.csv')
X_train = df_train.drop('target', axis=1)
y_train = df_train['target']

model = LogisticRegression()
model.fit(X_train, y_train)

with open('lab1/model.pkl', 'wb') as f:
    pickle.dump(model, f)
