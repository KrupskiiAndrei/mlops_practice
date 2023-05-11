from sklearn.preprocessing import StandardScaler
import pandas as pd

scaler = StandardScaler()

df_train = pd.read_csv('lab1/train/data.csv')
X_train = df_train.drop('target', axis=1)
y_train = df_train['target']
X_train_scaled = scaler.fit_transform(X_train)

df_test = pd.read_csv('lab1/test/data.csv')
X_test = df_test.drop('target', axis=1)
y_test = df_test['target']
X_test_scaled = scaler.transform(X_test)

df_train_scaled = pd.DataFrame(data=X_train_scaled)
df_train_scaled['target'] = y_train
df_train_scaled.to_csv('lab1/train/data_scaled.csv', index=False)

df_test_scaled = pd.DataFrame(data=X_test_scaled)
df_test_scaled['target'] = y_test
df_test_scaled.to_csv('lab1/test/data_scaled.csv', index=False)
