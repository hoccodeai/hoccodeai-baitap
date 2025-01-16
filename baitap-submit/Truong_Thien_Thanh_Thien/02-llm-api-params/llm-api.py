
# Đẩy các chức năng từ thư viện ra ngoài để sử dụng
from typing import Text
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Sử dụng thư viện load-dotenv để đọc file.env 
load_dotenv(r'C:\users\babia\downloads\API_KEY.env')

# Khởi tạo OpenAI client
client = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=os.getenv("api_key")
)
# Khởi tạo một danh sách để lưu các câu trả lời
messages = [] 

# Hàm gửi câu trả lời cho chatbot
def send_messages(role, content):
  global messages #global để cho mọi tin nhắn ở thế toàn cục
  messages.append({"role":role,"content":content}) # Tạo một từ điển, khi mà nhận được role và content ở phần def botbai2():Có role là user và content là user input
  for msg in messages: #Duyệt từng tin nhắn
    message_content = msg['content'] # Lấy nội dung đoạn tin nhắn
    # Kiểm tra có lọc URL và content
    if (msg['content'].startswith("https://") or msg['content'].startswith("http://")) and (msg['content'].endswith(".com") or msg['content'].endswith(".vn")):
            url = message_content # Nếu true lúc này message_content sẽ là URL
            res= requests.get(url) # Gửi lệnh get URL
            if res.status_code == 200: # NẾu thành công
                html_content= res.text # thì lấy được nội dung HTML thành file text
            parsed_html= BeautifulSoup(res.content, 'html.parser') #Gửi lệnh parsed HTML
            paragraphs = soup.find_all()
            #Tìm toàn bộ parsed và gửi lên API
            for all in paragraphs:
                send_messages("user", all.get_text())
        #Kiểm tra không phải URL thì gửi phần còn lại lên
    elif not (msg['content'].startswith("https://") or msg['content'].startswith("http://")) and (msg['content'].endswith(".com") or msg['content'].endswith(".vn")):
         for item in messages:
           item = text
           send_messages("user", text)
  chat_completion = client.chat.completions.create( # Tạo nhận câu trả lời từ model và chế độ chạy chữ ra từ từ
        messages=messages,
        model="meta-llama/Llama-3-70b-chat-hf",
        stream=True
    )
  print("botbai2: ", end="") # Khi bot trả kết quả hiện " botbai: " trước kết quả, end="" là cho trả kết quả không xuống dòng .
  for tung_doan in chat_completion: # Đây là vòng lặp của từng đoạn trong chat.competion, để trả kết quả từ từ), end: như trên.
        print(tung_doan.choices[0].delta.content or"", end="") #
  print()
  print(" Bạn còn câu hỏi nào nữa không nếu không thì hãy chat: 'bye', muốn lưu thì chat: 'save'")
  print()

def luu_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
                file.write("tung_doan.choices[0].delta.content or"", end=""")

def botbai2():
    print("Hello minh dang learn code ai")
    while True: # Tạo vòng lặp vô hạn kết thúc bằng break, khi chạy hết 1 vòng có đk true luôn đúng nên chạy tiếp.
        user_message= input("You: ") # Đặt tên biến là người dùng gửi gán cho chức năng nhập dữ liệu là input trước nội dung input có "you: "
        if user_message.lower() == "bye": # Nếu người dùng gửi "bye" thì break và in bái bai, lower() để khi nhập viết hoa hay gì đó đều quay lại là "bye"
            print("botbai2: bái baiiiii")
            break
        if user_message.lower() == "save":
            luu_file("filename", content)
            
        send_messages("user", user_message) # Nếu không chat "bye" thì phần send_messages(role, content) sẽ nhận role là "user" và content là  user_message

if __name__ == "__main__":
    botbai2()

        