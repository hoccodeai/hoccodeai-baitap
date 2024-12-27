import os
from openai import OpenAI

client = OpenAI(
    base_url= "https://api.openai.com/v1",
    api_key= ""
)

a = input("Nhập câu hỏi của bạn: ")
while a != "exit":
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user", 
                "content": a
            }
        ],
        model="gpt-4o-mini",
        stream=True
    )     
    for message in chat_completion:
        print(message.choices[0].delta.content or "", end="")
    a = input("\nNhập câu hỏi của bạn: ")