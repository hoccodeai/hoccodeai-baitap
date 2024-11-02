import os

from docx import Document
from openai import OpenAI


def create_prompt(user_input):
    messages = {
        "role": "user",
        "content": user_input,
    }
    memory_AI.append(messages)
    return memory_AI


def docx_to_txt(file_docx, file_txt):
    doc = Document(file_docx)
    with open(file_txt, "w", encoding="utf-8") as file:
        for para in doc.paragraphs:
            if para.text.strip():
                sentenses = para.text.split(".")
                for sentense in sentenses:
                    if sentense.strip():
                        file.write(sentense.strip() + ".\n")


def translate_file(file):
    docx_to_txt(file, "new_file.txt")
    with open("new_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return str(content)


memory_AI = [
    {
        "role": "system",
        "content": "you are translator",
    },
    {
        "role": "user",
        "content": "my name is Duy,translate another language into vietnamese",
    },
]
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)
bot_answer = []
running = True
while running:
    user_input = input("message mybot :")
    if ("translate" and "file") in user_input:
        enter_file = input("re-enter your file :")
        user_input = user_input + translate_file(enter_file)
    stream = client.chat.completions.create(
        messages=create_prompt(user_input),
        model="gemma2-9b-it",
        stream=True,
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        bot_answer.append(content)

    if "quit" in user_input:
        print("bye")
        running = False

with open("bot_response.txt", "w", encoding="utf-8") as file:
    for line in bot_answer:
        file.write(line)
