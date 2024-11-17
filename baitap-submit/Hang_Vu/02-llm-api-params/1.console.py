import os
from dotenv import load_dotenv
import openai

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
def answer_question(question):
    try:
        chat_completion = openai.ChatCompletion.create(
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens = 50,
            n = 1,
            temperature = 0.6,
            model = "gpt-3.5-turbo",

        )
        return chat_completion.choices[0].message["content"]
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"
def main():
    print("Welcome to Onion Chatbot. Enter bye when you want to exit")
    
    while True:
        question = input("Question:")
        if question.lower() == "bye":
            print("Goodbye. See you soon!")
            break
        else:
            answer = answer_question(question)
            print(f"Answer: {answer}")

if __name__ == "__main__":
    main()

