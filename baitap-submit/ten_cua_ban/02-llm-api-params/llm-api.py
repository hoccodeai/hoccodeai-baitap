Bài 1: Viết một ứng dụng console đơn giản, người dùng gõ câu hỏi vào console, bot trả lời và in ra. Có thể dùng stream hoặc non-stream.

from openai import OpenAI

client = OpenAI(
    base_url="https://api.openai.com/v1",
       api_key='xxxxxxxxxxxxxx',
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello. Who are you?",
        }
    ],
    model="gpt-4o",
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
  
  BÀI 2: Cải tiến ứng dụng chat: Sau mỗi câu hỏi và trả lời, ta lưu vào array messages và tiếp tục gửi lên API để bot nhớ nội dung trò chuyện.

from openai import OpenAI
client = OpenAI(
    base_url="https://api.openai.com/v1",
       api_key='xxxxxxxxxxxxxx',
)
messages=[ 
	{
		"role": "system",
		"content": "You are a friendly and flirty female tour guide.",
	},
],	# dùng mảng messages đê chứa. khởi tạo ban đầu = rỗng,
user_mess="hello, who are you",
messages=messages.appen{"role":"user","content":user_mess}

chat_completion = client.chat.completions.create(
    messages=messages,  # Sử dụng mảng messages
    model="gpt-4o-mini"
)

print(chat_completion.choices[0].messages.content
messages=messages.appen{"role":"user","content":chat_completion.choices[0].messages.content}

while True:
    user_mess = input("Bạn: ")
    messages.append({"role": "user", "content": user_mess})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_message})

    print("Bot:", bot_message)
Bài 3: Tóm tắt website. Dán link website vào console, bot sẽ tóm tắt lại nội dung của website đó.
Bài này với bài 4 + 5 em chưa làm được 
