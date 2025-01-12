
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def require_user_input(message):
    user_input = ""
    while(user_input == ""):
        user_input = input(message)
    return user_input

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv('API_KEY'),
)