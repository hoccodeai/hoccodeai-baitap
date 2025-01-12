import utils
from bs4 import BeautifulSoup
import requests

def get_content(url):
    res=requests.get(url)

    if res.status_code != 200:
        print("Error: Failed to fetch the content")
        return
    
    soup = BeautifulSoup(res.text, "html.parser")
    main_content = soup.find(id="content")

    if main_content:
        content = main_content.text.strip()
        return content
    else:
        return soup.get_text().strip()



def exercise3():
    want = "Summarize the following content"
    while(True):
        url = utils.require_user_input("Paste your url: ")
        if url == "e" or url == "q":
            break

        content = get_content(url)

        if content is None:
            print("Error: Failed to fetch the content")
            continue

        question = " ".join([want,":",content]) 
        messages = [
            {"role":"system", "content": "You are a guru"},
            {"role": "user", "content": question}
        ]

        stream = utils.client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            stream=True
        )
        print("LLM is thinking...", end="\n\n")

        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")

exercise3()