from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных для обучающей и тестовой выборки
train_data = pd.read_csv("train/train_data.csv")
test_data = pd.read_csv("test/x_test.csv")

# Выделение признаков и меток
X_train = train_data.drop(columns=["Date"])  # Удаление столбца "Date" как признака
y_train = train_data['Temperature']  # Использование "Temperature" как целевой переменной
X_test = test_data.drop(columns=["Date"])
y_test = test_data['Temperature']

# Применение предобработки данных с использованием StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Сохранение предобработанных данных в CSV-файлы
pd.DataFrame(X_train).to_csv('train/x_train.csv', index=False)
pd.DataFrame(y_train).to_csv('train/y_train.csv', index=False)
pd.DataFrame(X_test).to_csv('test/x_test.csv', index=False)
pd.DataFrame(y_test).to_csv('test/y_test.csv', index=False)
