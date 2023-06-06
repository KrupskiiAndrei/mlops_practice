import numpy as np
import pandas as pd
import os

def main():
    # Создаем каталоги для хранения данных
    os.makedirs("train", exist_ok=True)
    os.makedirs("test", exist_ok=True)
    
    # Генерируем данные для обучения 
    train_data = pd.DataFrame(columns=['Date', 'Cost'])
    date_range_train = pd.date_range(start='2022-01-01', end='2023-12-12', freq='D')
    train_data['Date'] = date_range_train
    cost_train = np.random.normal(20, 5, 711)
    train_data['Cost'] = cost_train
    # Добавляем аномалии стоимости
    train_data.loc[100, 'Cost'] = -3
    train_data.to_csv('train/train_data.csv', index=False)
    
    # Генерируем тестовые данные 
    test_data = pd.DataFrame(columns=['Date', 'Cost'])
    date_range_test = pd.date_range(start='2023-01-01', end='2023-05-01', freq='D')
    test_data['Date'] = date_range_test
    cost_test = np.random.normal(25, 5, 121)
    test_data['Cost'] = cost_test
    test_data.to_csv('test/test_data.csv', index=False)

if __name__ == "__main__":
    main()
