import os

import requests
from bs4 import BeautifulSoup
from openai import OpenAI


def take_info_fromhtml(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = [p.text for p in soup.find_all("p")]
    new_paragraphs = "\n".join(paragraphs[:15])
    return str(new_paragraphs)


def create_prompt(user_input):
    global memory_ai
    messages = {
        "role": "user",
        "content": user_input,
    }
    memory_ai.append(messages)

    return memory_ai


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)
bot_answer = []
memory_ai = [
    {
        "role": "system",
        "content": "you are my assistance",
    }
]
running = True
while running:
    user_input = input("message mybot:")
    if "summarize" in user_input.lower():
        url = input("Please re-enter the url :")
        user_input = user_input + take_info_fromhtml(url)
    stream = client.chat.completions.create(
        messages=create_prompt(user_input),
        model="gemma2-9b-it",
        stream=True,
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        bot_answer.append(content)
    if user_input.lower() == "quit":
        print("bye")
        break
with open("bot_responses.txt", "w", encoding="utf-8") as file:
    for line in bot_answer:
        file.write(line)
