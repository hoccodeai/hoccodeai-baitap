import os
from dotenv import load_dotenv
import openai
import tiktoken
import re

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
            model = "gpt-4o-mini-2024-07-18",
        )
        return chat_completion.choices[0].message["content"]
    except Exception as e:
        print(f"Error: {e}")
def split_chunk(input_text, max_token):
    text = re.sub(r'\s+', '\n', input_text).strip()
    enc = tiktoken.get_encoding("gpt2")
    tokens = enc.encode(text)
    chunks = [tokens[i: i+ max_token] for i in range(0, len(tokens), max_token)]
    return [enc.decode(chunk) for chunk in chunks]
# print(split_chunk("Đây là một ví dụ về cách chia văn bản thành các phần nhỏ hơn. Văn bản này có thể dài hơn giới hạn token của GPT-3.5.", 10))
def main():
    input_text = input("Enter your text here:")
    input_language =  input("Enter the input language:")
    output_language = input("Enter the output language:")
    full_answer = ""
    split_text = split_chunk(input_text, 512)
    messages = [
    {
        "role": "system",
        "content": f"You are a translator assistant from {input_language} to {output_language}. Translate accurately, using B2 level vocabulary to help users understand easily. Correct grammar and emotional, sweet, clear and logical writing style."
    },]
    # print(messages)
    for text in split_text:
        messages.append(
            {
            "role": "user",
            "content": text
        })
        try:
                answer = answer_question(messages)
                messages.append({
                    "role": "assistant",
                    "content": answer
                })
                # print(answer)
                full_answer += answer + "\n"
                # # question = input("Question: ")
                # messages.append({
                #     "role": "user",
                #     "content": question
                # })
        except Exception as e:
            print(f"Error: {e}")
    with open("translate_data.txt","w", encoding = "utf-8") as f:
        f.write(full_answer)
        print("Data saved!")
if __name__ == "__main__":
    main()