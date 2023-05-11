import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

with open('lab1/model.pkl', 'rb') as f:
    model = pickle.load(f)

df_test = pd.read_csv('lab1/test/data_scaled.csv')
X_test = df_test.drop('target', axis=1)
y_test = df_test['target']

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f'Model test accuracy is: {accuracy:.3f}')
