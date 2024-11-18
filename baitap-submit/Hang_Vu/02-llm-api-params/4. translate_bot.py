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
            max_tokens = 512,
            n = 1,
            temperature = 0.6,
            model = "gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message["content"]
    except Exception as e:
        print(f"Error: {e}")
def main():
    input_text = input("Enter your text here:")
    input_language =  input("Enter the input language:")
    output_language = input("Enter the output language:")
    messages = [
    {
        "role": "system",
        "content": f"You are a translator assistant from {input_language} to {output_language}. Translate accurately, using B2 level vocabulary to help users understand easily. Correct grammar and emotional, sweet, clear and logical writing style."
    },]
    # print(messages)
    messages.append(
        {
        "role": "user",
        "content": input_text
    },)
    try:
        while True:
            print(answer_question(messages))
            question = input("Question: ")
            messages.append({
                "role": "user",
                "content": question
            })
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()