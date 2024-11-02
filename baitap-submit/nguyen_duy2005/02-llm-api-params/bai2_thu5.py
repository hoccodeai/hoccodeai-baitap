import os

from docx import Document
from openai import OpenAI


def create_prompt(user_input):
    message = {
        "role": "user",
        "content": user_input,
    }
    memory_AI.append(message)
    return memory_AI


def docx_to_txt(file_docx, file_txt):
    doc = Document(file_docx)
    with open(file_txt, "w", encoding="utf-8") as file:
        for para in doc.paragraphs:
            sentences = para.text.strip(".")
            for sentence in sentences:
                if sentence.strip():
                    file.write(sentence.strip() + ".\n")


def read_txt_fromdox(file):
    with open("new_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return str(content)


response_Ai = []
memory_AI = [
    {
        "role": "system",
        "content": "you are a developer of python",
    },
    {
        "role": "user",
        "content": "my name is Duy,write me code to solve the exercise",
    },
]
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)

running = True
while running:
    user_input = input("message mybot :")
    if ("solve") in user_input:
        enter_file = input("re-enter file dox :")
        user_input = user_input + read_txt_fromdox(enter_file)
    stream = client.chat.completions.create(
        messages=create_prompt(user_input),
        model="llama3-groq-70b-8192-tool-use-preview",
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        response_Ai.append(content)
    if "quit" in user_input:
        print("bye")
        running = False

with open("bot_response.py", "w", encoding="utf-8") as file:
    for line in response_Ai:
        file.write(line)
# bai11_leetcode.docx
# Read the whole passage I gave you and analyze it. Then write me the code to solve the exercise using python language.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
