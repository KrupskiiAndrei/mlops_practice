import numpy as np
import pandas as pd
import datetime
import os

def main():
    os.makedirs("train", exist_ok=True)
    os.makedirs("test", exist_ok=True)

    # Генерация обучающих данных
    train_data = pd.DataFrame(columns=['Date', 'Temperature'])
    date_range_train = pd.date_range(start='2022-01-01', end='2023-12-12', freq='D')
    train_data['Date'] = date_range_train
    
    # Генерация случайных значений температуры
    temperature_train = np.random.normal(20, 5, 711)
    train_data['Temperature'] = temperature_train
    
    # Добавление аномалий в данные о температуре
    train_data.loc[100, 'Temperature'] = -3

    # Сохранение обучающих данных в CSV-файл
    train_data.to_csv('train/train_data.csv', index=False)

    # Генерация тестовых данных
    test_data = pd.DataFrame(columns=['Date', 'Temperature'])
    date_range_test = pd.date_range(start='2023-01-01', end='2023-05-01', freq='D')
    test_data['Date'] = date_range_test

    # Генерация случайных значений температуры для тестирования
    temperature_test = np.random.normal(25, 5, 121)
    test_data['Temperature'] = temperature_test

    # Сохранение тестовых данных в CSV-файл
    test_data.to_csv('test/x_test.csv', index=False)

if __name__ == "__main__":
    main()
