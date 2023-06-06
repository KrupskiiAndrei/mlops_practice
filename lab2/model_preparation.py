import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

# Загрузка данных для обучения модели
х_train = pd.read_csv("train/x_train.csv")
y_train = pd.read_csv('train/y_train.csv')

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Сохранение модели в файл с помощью pickle
with open("trained_model.pkl", "wb") as f:
    pickle.dump(model, f)
