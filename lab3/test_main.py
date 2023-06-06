import main

# Тестирование функции с валидным текстовым вводом.
def test_valid_text():
    input_text = "Hello world."
    output_text = main.text_load(input_text)
    # Убедимся, что текстовый вывод не пуст после удаления пробельных символов.
    assert output_text.strip() != ""

# Тестирование функции с проверкой длины выходного текста.
def test_output_text_length():
    input_text = "Hello world."
    length = 20
    output_text = main.text_load(input_text)
    # Проверка, что длина выходного текста не превышает заданную длину.
    assert len(output_text) <= length

# Тестирование функции на ввод только числовых значений.
def test_input_text_not_numeric():
    numeric_text = "123"
    output_text = main.text_load(numeric_text)
    # Если ввод состоит только из чисел, функция должна вернуть сообщение о вводе текста.
    assert output_text == "Please enter some text."

# Тестирование функции на пустой ввод.
def test_empty_input_text():
    empty_text = ""
    output_text = main.text_load(empty_text)
    # Если ввод пуст, функция должна вернуть сообщение о вводе текста.
    assert output_text == "Please enter some text."
