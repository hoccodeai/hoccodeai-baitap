import os

from openai import OpenAI

# khoi tao client va goi ra api
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)

user_input = input("input your question:")
stream = client.chat.completions.create(
    messages=[
        {
            "role":"system"
            "content" :"you are my assistant "
        }
        {   
             "role": "user",
            "content": user_input,
        }
        
    ],
    model="gemma2-9b-it",
    stream=True,
)


print(stream.choices[0].delta.content or "" , end="")