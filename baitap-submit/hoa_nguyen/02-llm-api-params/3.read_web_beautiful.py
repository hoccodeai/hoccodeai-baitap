import requests
from bs4 import BeautifulSoup
from openai import OpenAI


def read_web_url():
    # gui request http den trang web
    url = 'https://tuoitre.vn/cac-nha-khoa-hoc-nga-bao-mat-troi-manh-nhat-20-nam-sap-do-bo-trai-dat-2024051020334196.htm'
    response = requests.get(url)
    
    if(response.status_code == 200):
        
        try:
            # phan tich cu phap html cua trang web
            soupHtml = BeautifulSoup(response.content,'html.parser')

            # lay noi dung cua trang web theo the div id= main-detail
            content_div = soupHtml.find('div', id='main-detail')
           
            title = content_div.find('h1',class_='detail-title article-title').text

            detail_info = content_div.find('h2',class_='detail-sapo').text

            detail_main = content_div.find('div',class_="detail-cmain").text

            content_body = title + "." + detail_info + detail_main

            chat_with_bot(content_body)

        except Exception as e:
            print(f"Error: {e}")

    else:
        print('khong tim thay trang web')



def chat_with_bot(contentHtml):

    # Init openAI client
    client = OpenAI(
        base_url="https://api.together.xyz/v1",
        # Làm theo hướng dẫn trong bài, truy cập https://api.together.ai/settings/api-keys để lấy API Key nha
        api_key='010dde7e500cc647a52d1a92efd2c9ece8331a059942d6151cf916a4cb206420',
    )
        
    list_message = []
    list_message.append({'role':'system', 'content': 'Bạn là chuyên gia trong lĩnh vực khoa học vũ trụ'})
    
    list_message.append({'role': 'user', 'content': 'Hãy tóm tắt lại nội dung bên dưới giúp tôi.Bài phân tích không dài quá 700 ký tự'})
    list_message.append({'role':'user','content':contentHtml})

    # gui cau hoi toi api va nhan cau tra loi
    response = client.chat.completions.create(
        messages = list_message,
        model = "meta-llama/Llama-3-70b-chat-hf"
    )
    
    bot_reply = response.choices[0].message.content
    list_message.append({"role":"assistant","content":bot_reply })
    print(f"Bot: {bot_reply}")

if __name__ == '__main__':
    read_web_url()
