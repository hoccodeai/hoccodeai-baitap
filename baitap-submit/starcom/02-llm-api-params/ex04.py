import os
from openai import OpenAI
import requests

client = OpenAI(
    base_url= "https://api.openai.com/v1",
    api_key= "sk-svcacct-Ew3KAKxZyJlMgdnWRCE2R-UZjHyWhMe_62vSRqzncTqCmczvdpC-7dqT4HUcuwxbeOLIT3BlbkFJPNHZTY51B7VqjFtRn7g1WQ6bT7jR8rZSNTPnpWzHdOFXoRtaJLpcYn_JHwjY6J-OeosA"
)

def parse_article(url):
    url = 'https://r.jina.ai/' + url
    headers = {
        'Authorization': 'Bearer jina_ff2838511747408bb71cac36c9573002x1EkAJOazb5u1oSmTiisH3tAFqtc'
    }
    return requests.get(url, headers=headers).text

def create_prompt(url):
    prompt = f"""
    Please summarize the article and translate it to Vietnamese: """ + parse_article(url) + """
    Summary:
    """
    return prompt

def chat_with_gpt4o_mini(url):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant."
            },
            {
                "role": "user", 
                "content": create_prompt(url)
            },
        ],
        model="gpt-4o-mini"
    )
    return response.choices[0].message.content


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt4o_mini(user_input)
    print("GPT-4o-mini:", response)