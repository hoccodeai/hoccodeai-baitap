import os

import requests
from bs4 import BeautifulSoup
from docx import Document
from openai import OpenAI


def create_prompt(user_input):
    message = {
        "role": "user",
        "content": user_input,
    }
    memory_Ai.append(message)
    return memory_Ai


def take_info_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = [p.text for p in soup.find_all("p")]
    new_paragraphs = "\n".join(paragraphs[:15])
    return str(new_paragraphs)


def docx_to_txt(file_docx, file_txt):
    doc = Document(file_docx)
    with open(file_txt, "w", encoding="utf-8") as file:
        for para in doc.paragraphs:
            sentensces = para.text.split(".")
            for sentence in sentensces:
                if sentence.strip():
                    file.write(sentence.strip() + ".\n")


def translate_file_txt(file):
    docx_to_txt(file, "new_file_txt.txt")
    with open("new_file_txt.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return content


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)
response_AI = []
voice = "you are my assistant"
memory_Ai = [
    {
        "role": "system",
        "content": voice,
    },
    {
        "role": "user",
        "content": "my name is Duy",
    },
]


running = True
while running:
    user_input = input("message mybot :")

    if "summarize" in user_input and "link" in user_input:
        voice = "you are summarizer"
        url = input("re-enter your url :")
        user_input += take_info_from_html(url)
    elif "translate" in user_input and "file" in user_input:
        voice = "you are translator"
        re_enter_file = input("re_enter your file :")
        user_input += translate_file_txt(re_enter_file)
    elif "solve" in user_input and "python language" in user_input:
        voice = "you are developer of python "
        create_prompt(
            "Read the whole passage I gave you and analyze it. Then write me the code to solve the exercise using python language."
        )
        re_enter_question = input("file dox :")
        user_input += translate_file_txt(re_enter_question)

    stream = client.chat.completions.create(
        messages=create_prompt(user_input),
        model="llama3-groq-70b-8192-tool-use-preview",
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        response_AI.append(content)
    if "quit" in user_input:
        print("\n bye ")
        running = False
    if "solve" in user_input and "python language" in user_input:
        with open("bot_response_demo.py", "w", encoding="utf-8") as file:
            for line in response_AI:
                file.write(line)
    elif "translate" in user_input and "file" in user_input:
        with open("bot_response_demo.txt", "w", encoding="utf-8") as file:
            for line in response_AI:
                file.write(line)
