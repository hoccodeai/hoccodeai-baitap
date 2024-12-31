
from openai import OpenAI
import os

client = OpenAI(
     base_url="https://api.together.xyz/v1",
    api_key='010dde7e500cc647a52d1a92efd2c9ece8331a059942d6151cf916a4cb206420',
)

def input_program():
    print('Hãy chương trình tìm kiếm ký tự trong chuỗi\n')
    user_input =  input('Nhập chuỗi: ')
    find_characters = input('Nhập ký tự cần tìm kiếm: ')
    return  user_input, find_characters

def execute_program():
    
    str_input, find_characters = input_program()
    # create message - send messages to openai and get response
    
    print(str_input)
    print(find_characters)
    
    
    messages = [{'role': 'system', 'content':'Lập trình tìm kiếm phần tử trong chuỗi bằng ngôn ngữ python'}
                ,{'role':'assistant','content':'Bạn là lập trình viên máy tính'}
                ,{'role':'user','content':'Viết chương trình python.\n Hãy tìm kiếm trong chuỗi sau : \n {str_input} \n.Ký tự {find_characters} xuất hiện bao nhiêu lần và vị trí xuất hiện của ký tự {find_characters}. Chỉ xuất ra chương trình code python.' }]

    response = client.chat.completions.create(
        model= "meta-llama/Llama-3-70b-chat-hf",
        messages= messages,
        temperature= 0.7
       )
    bot_reply = response.choices[0].message.content
    file_path = 'exercise_05.py'
    file_existed = checkFileExist(file_path)

    if file_existed == True:
        save_file(bot_reply,file_path)
    else:
        print('Khong tim thay file')


def checkFileExist(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False



def save_file(content, file_path):
    with open(file_path, "wb") as file:
        file.write(content.encode("utf-8"))  # Chuyển đổi str thành bytes


if __name__ == '__main__':
    #example : nhap chuoi : 'cherry', ky tu tim kiem : 'r', 
    # out put : số lần xuất hiện: 2, vị trí [2,3]
    execute_program()




        
