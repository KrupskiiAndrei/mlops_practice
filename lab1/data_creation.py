from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import pandas as pd

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df_train = pd.DataFrame(data=X_train)
df_train['target'] = y_train
df_train.to_csv('lab1/train/data.csv', index=False)

df_test = pd.DataFrame(data=X_test)
df_test['target'] = y_test
df_test.to_csv('lab1/test/data.csv', index=False)
