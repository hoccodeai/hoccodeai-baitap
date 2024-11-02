from openai import OpenAI
import requests
from bs4 import BeautifulSoup

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key='YOUR_API_KEY',
)
# Bài Tập 1,2:
def ask_question_nonstream():
    messages = [{"role": "system", "content": "You are a smart and friendly companion."}]
    
    print("You can ask multiple questions (type 'exit' to stop asking questions):")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting question mode.")
            break
        messages.append({"role": "user", "content": question})
        response = client.chat.completions.create(
            messages=messages,
            temperature=0,
            model="gemma2-9b-it",
        )
        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        print("Bot:", answer)

# Bài Tập 3:
def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        return response.text
    except requests.RequestException as e:
        print("Error fetching the website:", e)
        return None

def parse_html_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    content = " ".join([p.get_text() for p in paragraphs])
    return content

def summarize_content(content):
    prompt = (
        "Please summarize the following article while focusing on the key points and important details. "
        "Your summary should be concise yet informative, capturing the essence of the content. "
        "As you summarize, try to maintain a positive tone and inject a bit of humor where appropriate, "
        "without detracting from the core message. Write the summary in Vietnamese.\n\n"
        "===\n"
        f"{content}\n"
        "===\n"
    )

    messages = [{"role": "system", "content": "You are an in-depth website content analyst."}, {"role": "user", "content": prompt}]
    try:
        response = client.chat.completions.create(
            messages=messages,
            temperature=0,
            model="gemma2-9b-it",
        )
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print("Error with OpenAI API:", e)
        return None

def summarize_website_content():
    url = input("Dán link website vào đây: ")
    html_content = fetch_website_content(url)
    if html_content is None:
        print("Không thể lấy nội dung trang web.")
        return

    parsed_content = parse_html_content(html_content)
    if not parsed_content:
        print("Không thể phân tích nội dung trang web.")
        return

    summary = summarize_content(parsed_content)
    if summary:
        print("Tóm tắt nội dung:")
        print(summary)
    else:
        print("Không thể tạo tóm tắt.")


# Bài Tập 4:
def generate_prompt(text, source_language, target_language):
    return (
        f"Translate the following government document from {source_language} to {target_language}. "
        "The translation should be accurate, clear, and maintain the original meaning and tone. "
        "Preserve the original formatting as much as possible. Use formal language appropriate for an official government document.\n\n"
        "===\n"
        f"{text}\n"
        "==="
    )

def translate_text(text, source_language, target_language):
    prompt = generate_prompt(text, source_language, target_language)
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        model="gemma2-9b-it",
    )
    
    return response.choices[0].message.content

def split_text(text, max_length=2000):
    parts = []
    while len(text) > max_length:
        split_index = text.rfind(' ', 0, max_length)
        if split_index == -1:
            split_index = max_length
        parts.append(text[:split_index])
        text = text[split_index:].strip()
    parts.append(text) 
    return parts

def translate_text_file():
    source_language = "English"  
    target_language = "Vietnamese"

    # Đọc nội dung từ file
    with open("input_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
    
    # Tách nội dung thành các phần nhỏ
    text_parts = split_text(content, max_length=2000)
    
    translated_parts = []
    for part in text_parts:
        translated_part = translate_text(part, source_language, target_language)
        translated_parts.append(translated_part)
    
    # Ghi kết quả vào file mới
    with open("translated_file.txt", "w", encoding="utf-8") as file:
        for translated in translated_parts:
            file.write(translated + "\n")

# Bài Tập 5:
def generate_code(question):
    prompt = f"Write a Python code snippet to perform: {question} result only show code"
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5, 
        model="gemma2-9b-it",
    )
    
    return response.choices[0].message.content

def generate_code_snippet():
    print("Input your question for code generation (type 'exit' to quit):")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting code generation mode.")
            break
        
        code = generate_code(question)
        print("Code result:\n", code)
        
        # Ghi kết quả vào file final.py
        with open("final.py", "a", encoding="utf-8") as f:
            f.write(f"# Question: {question}\n")
            f.write(code + "\n\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Ask questions to the bot")
        print("2. Summarize website content")
        print("3. Translate text from file")
        print("4. Generate Python code snippet")
        print("5. Exit")

        choice = input("Select an option (1-5): ")
        if choice == "1":
            ask_question_nonstream()
        elif choice == "2":
            summarize_website_content()
        elif choice == "3":
            translate_text_file()
        elif choice == "4":
            generate_code_snippet()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
