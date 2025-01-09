import openai
import os
from dotenv import load_dotenv
from groq import Groq
# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("GROQ_API_KEY")

def get_completion(messages):
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Có lỗi xảy ra: {str(e)}"

def main():
    print("Chào mừng bạn đến với ChatBot!")
    print("Gõ 'quit' để thoát")
    
    # Khởi tạo mảng messages để lưu lịch sử trò chuyện
    messages = []
    
    while True:
        user_input = input("\nBạn: ")
        
        if user_input.lower() == 'quit':
            print("Tạm biệt!")
            break
            
        # Thêm tin nhắn của người dùng vào messages
        messages.append({"role": "user", "content": user_input})
        
        # Lấy phản hồi từ bot với toàn bộ lịch sử trò chuyện
        response = get_completion(messages)
        
        # Thêm phản hồi của bot vào messages
        messages.append({"role": "assistant", "content": response})
        
        print("\nBot:", response)

if __name__ == "__main__":
    main()
