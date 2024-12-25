import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI API client
api_key = os.getenv("together_api_key")
client = openai.OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=api_key,
)

def generate_chat_response(prompt, isStream=True):
    """
    Sends a prompt to the OpenAI API and returns the response.
    """
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            stream=isStream,
            max_completion_tokens=500,  # Adjust token limit for summaries
        )
        
        if isStream:
            list_content = []
            for chunk in completion:
                content = chunk.choices[0].delta.content
                if content:
                    list_content.append(content)
            print(f"\nBot: {''.join(list_content)}")
            
        else:
            print(completion.choices[0].message.content)

    except Exception as e:
        return f"Error generating completion: {e}"