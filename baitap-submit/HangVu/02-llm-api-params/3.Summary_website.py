import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import openai

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

# Call html from website & parse html

def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(id = 'main-detail')
        if elements:
            data = "".join(element.get_text(strip = True) for element in elements)
            return data
        else:
            return "No element found"
        
    except Exception as e:
        return f"Error:{e}"
# Get summary of website
def answer_question(messages):
    try:
        chat_completion = openai.ChatCompletion.create(
            messages = messages,
            max_tokens = 512,
            n = 1,
            temperature = 0.6,
            model = "gpt-4o-mini-2024-07-18",
        )
        return chat_completion.choices[0].message["content"]
    except Exception as e:
        print(f"Error: {e}")
def main():
    print("Welcome to Onion Summary Chatbot. Enter bye when you want to exit!")
    messages = [
    {
        "role": "system",
        "content": "You are a text summary assistant. Summarize the main ideas of the text. Requirements: Keep the main ideas, do not summarize unnecessary ideas."
    },]
    # print(messages)
    url = input("Enter the link website:")
    data = get_data(url)
    # print(data)
    messages.append(
        {
        "role": "user",
        "content": data
    },)
    # print(messages)
    try:
        while True:
            answer = answer_question(messages)
            messages.append({
                    "role": "assistant",
                    "content": answer
                })
            print(f"Answer: {answer}")
            question = input("Question: ")
            messages.append({
                "role": "user",
                "content": question
            })
            if question.lower() == "bye":
                print("Goodbye. See you soon!")
                break  
    except Exception as e:      
        print(f"Error: {e}")

if __name__ == "__main__":
    main()