import openai
import os
from dotenv import load_dotenv
from groq import Groq
# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("GROQ_API_KEY")

def get_completion(prompt):
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Có lỗi xảy ra: {str(e)}"

def main():
    print("Chào mừng bạn đến với ChatBot!")
    print("Gõ 'quit' để thoát")
    
    while True:
        user_input = input("\nBạn: ")
        
        if user_input.lower() == 'quit':
            print("Tạm biệt!")
            break
            
        response = get_completion(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    main()
