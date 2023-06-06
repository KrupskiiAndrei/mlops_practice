from transformers import pipeline as transformer_pipeline
from streamlit import cache as st_cache, slider as st_slider, title as st_title, text_input as st_text_input, button as st_button, success as st_success

# Кэширование загрузки модели для повышения производительности
@st_cache
def get_model_pipeline():
    return transformer_pipeline("text-generation", model="openai-gpt")

# Получение модели
model_pipeline = get_model_pipeline()

# Настройка интерфейса
st_title("Application for Text Generation")
user_input = st_text_input("Type the text here", value="")
output_length = st_slider("Desired output length", 10, 100, 10)
num_repeats = st_slider("Number of iterations", 1, 3, 1)

# Функция для генерации текста
def generate_text(user_input):
    if not user_input or user_input.isdigit():
        return "Please enter some text."
    return model_pipeline(user_input, max_length=output_length, num_return_sequences=num_repeats)

# Обработка нажатия кнопки
if st_button("Generate"):
    output_text = generate_text(user_input)
    st_success(output_text)
