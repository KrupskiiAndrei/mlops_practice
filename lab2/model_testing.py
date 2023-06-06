import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error

# Загрузка обученной модели из файла
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

# Загрузка данных для тестирования модели
х_test = pd.read_csv("test/x_test.csv")
y_test = pd.read_csv("test/y_test.csv")

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)

# Вывод результатов
print("Mean squared error: %.2f" % mse)
