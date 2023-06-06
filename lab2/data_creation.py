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
  temperature_train = np.random.normal(20, 5, 711)
  train_data['Temperature'] = temperature_train
# Добовляем аномалии температуры
  train_data.loc[100, 'Temperature'] = -3
  train_data.to_csv('train/train_data.csv', index=False)
# Генерация тренировочных данных 
  test_data = pd.DataFrame(columns=['Date', 'Temperature'])
  date_range_test = pd.date_range(start='2023-01-01', end='2023-05-01', freq='D')
  test_data['Date'] = date_range_test
  temperature_test = np.random.normal(25, 5, 121)
  test_data['Temperature'] = temperature_test
  test_data.to_csv('test/test_data.csv', index=False)
if __name__ == "__main__":
  main()
