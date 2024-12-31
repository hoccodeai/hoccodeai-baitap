from openai import OpenAI

# Int openAI client
client = OpenAI(
    base_url="https://api.together.xyz/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://api.together.ai/settings/api-keys để lấy API Key nha
    api_key='010dde7e500cc647a52d1a92efd2c9ece8331a059942d6151cf916a4cb206420',
)

def chat_with_bot():
    print ("\n Wellcome to the Chatbot console! (Type '0' to exist)\n")
    list_messages =[] #array luu hoai thoai nguoi dung
    while True:
        # Nguoi dung nhap cau hoi
        user_input = input("You:")
       
        # kiem tra neu nguoi dung muon thoat thi nhap 0
        if user_input.lower() == '0':
            break

        list_messages.append({"role":"user", "content":user_input})
        # gui cau hoi toi openAI va nhan cau tra loi

        response = client.chat.completions.create(
            messages =list_messages,
            model="meta-llama/Llama-3-70b-chat-hf"
        )
        
        bot_reply = response.choices[0].message.content
        list_messages.append({"role":"assistant","content":bot_reply })
        print(f"Bot: {list_messages}")



if __name__ == "__main__":
    chat_with_bot()