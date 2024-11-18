import os
from dotenv import load_dotenv
import openai

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
def answer_question(messages):
    try:
        chat_completion = openai.ChatCompletion.create(
            messages = messages,
            max_tokens = 50,
            n = 1,
            temperature = 0.6,
            model = "gpt-4o-mini-2024-07-18",

        )
        return chat_completion.choices[0].message["content"]
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"
def main():
    print("Welcome to Onion Chatbot. Enter bye when you want to exit")
    messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },]
    while True:
        question = input("Question:")
        messages.append({
            "role": "user",
            "content": question
        })
        if question.lower() == "bye":
            print("Goodbye. See you soon!")
            break
        else:
            answer = answer_question(messages)
            messages.append({
                "role": "assistant",
                "content": answer
            })
            print(f"Answer: {answer}")

if __name__ == "__main__":
    main()

