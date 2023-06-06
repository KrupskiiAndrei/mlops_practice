from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных для обучающей и тестовой выборки
train_data = pd.read_csv("train/train_data.csv")
test_data = pd.read_csv("test/test_data.csv")

# Выделение признаков и меток
х_train = train_data.drop(columns=["Date"])
y_train = train_data['Cost']
х_test = test_data.drop(columns=["Date"])
y_test = test_data['Cost']

# Применение предобработки данных с использованием StandardScaler
scaler = StandardScaler()
х_train = scaler.fit_transform(х_train)
х_test = scaler.transform(х_test)

# Сохранение предобработанных данных
pd.DataFrame(X_train).to_csv('train/X_train.csv', index=False)
pd.DataFrame(y_train).to_csv('train/y_train.csv', index=False)
pd.DataFrame(х_test).to_csv('test/х_test.csv', index=False)
pd.DataFrame(y_test).to_csv('test/y_test.csv', index=False)
