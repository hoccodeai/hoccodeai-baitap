import os
from dotenv import load_dotenv
import openai

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

def answer_question(messages):
    chat_completion = openai.ChatCompletion.create(
        messages = messages,
        max_tokens = 512,
        n = 1,
        temperature = 0.6,
        model = "gpt-4o-mini-2024-07-18",
    )
    return chat_completion.choices[0].message["content"]
def main():
    try:
            question = input("Enter your question:")
            messages = [
            {
                "role": "system",
                "content": "You are a python programmer. Requirements: Write easy-to-understand source code with full comments for each part. Print out only code and comments"
            }]
            messages.append(
            {
                "role": "user",
                "content": question
            })
            answer = answer_question(messages)
            messages.append({
                "role": "assistant",
                "content": answer
            })
    except Exception as e:
        print(f"Error: {e}")
    with open("final.py", "w", encoding="utf-8") as f:
        f.write(answer)
        print("The answer has been saved to final.py")
if __name__ == "__main__":
    main()    
