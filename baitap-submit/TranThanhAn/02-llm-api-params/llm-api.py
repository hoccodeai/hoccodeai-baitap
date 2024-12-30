"""import os
from openai import OpenAI
# Thiết lập Groq API client
client = OpenAI(
    base_url="http://192.168.38.1:1234/v1",
    api_key='meta-llama-3.1-8b-instruct',  # Thay bằng API key của bạn
)
# Hàm chính để trò chuyện với AI
def chat_with_ai():
    print("Chào mừng bạn đến với chatbot console! (Gõ 'exit' để thoát)")
    messages = []  # Lưu lịch sử trò chuyện

    while True:
        # Người dùng nhập câu hỏi
        user_input = input("Bạn: ")
        if user_input.lower() == "exit":
            print("Tạm biệt!")
            break

        # Thêm câu hỏi vào lịch sử
        messages.append({"role": "user", "content": user_input})

        try:
            # Gửi yêu cầu đến Groq AI
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"  # Tên mô hình bạn đang sử dụng
            )

            # Lấy phản hồi từ AI
            bot_response = chat_completion.choices[0].message.content
            print(f"Bot: {bot_response}")

            # Lưu phản hồi vào lịch sử
            messages.append({"role": "assistant", "content": bot_response})
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            break

if __name__ == "__main__":
    chat_with_ai()

#dùng AI để tóm tắt bài báo
"""

import os
import requests
import logging
from bs4 import BeautifulSoup
from openai import OpenAI
from urllib.parse import urlparse

client = OpenAI(
    base_url="http://192.168.38.1:1234/v1",
    api_key='meta-llama-3.1-8b-instruct',  # Thay bằng API key của bạn
)

def validate_url(url):
    #Validate the URL format.
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def fetch_website_content(url):
    #Fetch HTML content from the given URL.
    if not validate_url(url):
        logging.error("Invalid URL format.")
        return None

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info("Successfully fetched website content.")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching content from URL: {e}")
        return None

def extract_main_content(html):
    #Extract the main content from the HTML.
    try:
        soup = BeautifulSoup(html, 'html.parser')
        #https://vnexpress.net/cach-ong-luu-binh-nhuong-can-thiep-chinh-quyen-giup-doanh-nghiep-de-huong-loi-4832281.html
        main_content = soup.find('article', class_='container')
        if not main_content:
            main_content = soup.find('div', class_='sidebar-1') 

        if main_content:
            logging.info("Successfully extracted main content.")
            return main_content.get_text(strip=True)
        else:
            logging.warning("Main content not found in the webpage.")
            return None
    except Exception as e:
        logging.error(f"Error parsing HTML: {e}")
        return None


def summarize_content(content):
    #Send the content to the OpenAI API for summarization.
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Act as an English translator and technical writer."},
                {"role": "user", "content": f"Summarize the following content in vietnamese for short summarize: {content}",}
            ],
            model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"
        )
        summary = chat_completion.choices[0].message.content
        logging.info("Successfully summarized content.")
        return summary
    except Exception as e:
        logging.error(f"Error sending summarization request: {e}")
        return None

def main():
    logging.info("Welcome to the website summarization tool!")
    url = input("Enter the URL of the article: ").strip()

    # Fetch website content
    html = fetch_website_content(url)
    if not html:
        return

    # Extract main content
    content = extract_main_content(html)
    if not content:
        return

    # Summarize content
    summary = summarize_content(content)
    if summary:
        print("\n=== Summary ===")
        print(summary)
    else:
        logging.error("Failed to generate summary.")

if __name__ == "__main__":
    main()
