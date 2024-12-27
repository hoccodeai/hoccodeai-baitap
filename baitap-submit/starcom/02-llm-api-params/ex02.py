import os
from openai import OpenAI

client = OpenAI(
    base_url= "https://api.openai.com/v1",
    api_key= ""
)

def chat_with_gpt4o_mini(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model="gpt-4o-mini"
    )
    return response.choices[0].message.content

# Lưu trữ lịch sử chat
chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt4o_mini(user_input)
    print("GPT-4o-mini:", response)
    chat_history.append(f"You: {user_input}\nGPT-4o-mini: {response}\n")

# Lưu lịch sử chat vào file
with open("chat_history.txt", "w") as f:
    f.writelines(chat_history)