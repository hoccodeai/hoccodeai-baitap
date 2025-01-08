import os
from os.path import dirname, join
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, verbose=True)

client = OpenAI(
    base_url=os.environ.get("URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def extract_content_by_beautifulsoup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # メタタグと不要なタグを削除
        for tag in soup(["script", "style", "meta", "link"]):
            tag.decompose()

        # テキストを抽出して整形
        text = " ".join(soup.stripped_strings)
        return text
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


def summarize_content(text):
    try:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            n=1,
            max_tokens=500,
            temperature=0.7,
            top_p=1,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional content summarizer, summarize the main ideas of the text in a concise manner of about 50-70 words based on the input content.",
                },
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"要約中にエラーが発生しました: {str(e)}"


def main():
    print("リンクを入力してください。終了するにはCtrl+Cを押してください。")
    try:
        while True:
            website_url = input("Link: ")
            if not website_url.strip():
                continue

            if not is_valid_url(website_url):
                print("無効なURLです。正しいURLを入力してください。")
                continue

            print("コンテンツを取得中...")
            content = extract_content_by_beautifulsoup(website_url)

            print("内容を要約中...")
            summary = summarize_content(content)

            print("\n要約結果:")
            print(summary)
            print("\n---\n")
    except KeyboardInterrupt:
        print("\nプログラムを終了します。お疲れ様でした!")


if __name__ == "__main__":
    main()
