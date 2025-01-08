import os
from os.path import dirname, join

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, verbose=True)

client = OpenAI(
    base_url=os.environ.get("URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_ai_response(question):
    try:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "user",
                    "content": question,
                },
            ],
            n=1,
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            stream=True,
        )

        print("回答: ", end="", flush=True)
        collected_content = []
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                collected_content.append(content)
        print()
        return "".join(collected_content)
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


def main():
    print("質問を入力してください。終了するにはCtrl+Cを押してください。")
    try:
        while True:
            question = input("\n質問: ")
            if not question.strip():
                continue
            get_ai_response(question)
    except KeyboardInterrupt:
        print("\nプログラムを終了します。お疲れ様でした!")


if __name__ == "__main__":
    main()
