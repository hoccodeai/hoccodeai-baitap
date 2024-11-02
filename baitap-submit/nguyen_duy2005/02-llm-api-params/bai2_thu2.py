import os

from openai import OpenAI


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

# de cho Ai ghi nho nhung gi minh da viet
memory_ai = [{"role": "system", "content": "you are my assistance"}]
# code de cho chuong trinh chay lien tuc

running = True
while running:
    user_input = str(input("Message Mybot:"))

    stream = client.chat.completions.create(
        messages=create_prompt(user_input),
        model="gemma2-9b-it",
        stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    if user_input.lower() == "quit":
        print("good_bye")
        break
