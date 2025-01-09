import requests
from bs4 import BeautifulSoup
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_website_content(url):
    try:
        # Gửi request đến website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm nội dung chính (có thể điều chỉnh selector tùy theo website)
        if 'tuoitre.vn' in url:
            main_content = soup.find('div', {'id': 'content'})
            if not main_content:
                main_content = soup.find('div', {'class': 'detail__section'})
        elif 'vnexpress.net' in url:
            main_content = soup.find('article', {'class': 'fck_detail'})
            if not main_content:
                main_content = soup.find('div', {'class': 'article-content'})
        else:
            # Thử nhiều selector phổ biến
            main_content = (
                soup.find('article') or
                soup.find('main') or 
                soup.find('div', {'class': ['content', 'article', 'post-content', 'entry-content']}) or
                soup.find('div', {'id': ['content', 'article', 'post-content', 'entry-content']})
            )
    
        if main_content:
            # Lấy text và loại bỏ khoảng trắng thừa
            content = ' '.join(main_content.get_text().split())
            return content
        return "Không thể tìm thấy nội dung chính của trang web."
    
    except Exception as e:
        return f"Lỗi khi lấy nội dung website: {str(e)}"

def summarize_content(content):
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        prompt = f"""Hãy tóm tắt nội dung sau đây một cách ngắn gọn, súc tích. Tập trung vào các điểm chính và thông tin quan trọng nhất.
        Định dạng phản hồi:
        - Tiêu đề chính (nếu có)
        - Tóm tắt ngắn gọn (3-4 câu)
        - Các điểm chính (dạng bullet points)
        
        Nội dung cần tóm tắt:
        {content}
        """
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Lỗi khi tóm tắt nội dung: {str(e)}"

def main():
    print("Chào mừng bạn đến với Website Summarizer!")
    print("Dán link website để tóm tắt (hoặc gõ 'quit' để thoát)")
    
    while True:
        url = input("\nNhập URL: ")
        
        if url.lower() == 'quit':
            print("Tạm biệt!")
            break
            
        print("\nĐang xử lý...")
        content = get_website_content(url)
        
        if content:
            summary = summarize_content(content)
            print("\nTóm tắt nội dung:")
            print("-" * 50)
            print(summary)
            print("-" * 50)

if __name__ == "__main__":
    main()