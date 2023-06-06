import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error

# Загрузка обученной модели из файла
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

# Загрузка данных для тестирования модели
х_test = pd.read_csv("test/х_test.csv")
y_test = pd.read_csv("test/y_test.csv")

# Прогнозирование на тестовых данных
y_pred = model.predict(х_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)

# Вывод результатов
print(f"Среднеквадратичная ошибка: {mse:.2f}")
