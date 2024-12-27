import os
from openai import OpenAI

client = OpenAI(
    base_url= "https://api.openai.com/v1",
    api_key= ""
)

def create_prompt(question):
    prompt = f"""
    Please solve the following programming problem using Python:
    {question}
    
    Solution:
    """
    return prompt

def chat_with_gpt4o_mini(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": create_prompt(prompt)},
        ],
        model="gpt-4o-mini"
    )
    return response.choices[0].message.content

while True:
    question = input("Enter the programming problem: ")
    if question.lower() == "exit":
        break
    response = chat_with_gpt4o_mini(question)
    print("GPT-4o-mini:", response)
