from transformers import pipeline as pl
from streamlit import cache, slider as sl, title as ttl, text_input as ti, button as btn, success as succ


@cache
def load_pipeline():
    return pl("text-generation", model="openai-gpt")


text_gen_pipe = load_pipeline()

ttl("Text generation application")
user_prompt = ti("Enter the text", value="")
text_len = sl("Text length", 10, 100, 10)
num_iter = sl("How many iterations", 1, 3, 1)


def gen_text(prompt):
    if not prompt or str(prompt).isdigit():
        return "Please enter some text."
    return text_gen_pipe(
        prompt, max_length=text_len, num_return_sequences=num_iter
    )


if btn("Output"):
    res_text = gen_text(user_prompt)
    succ(res_text)
