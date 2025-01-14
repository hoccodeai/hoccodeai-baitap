import json
from openai import OpenAI
import os
from dotenv import load_dotenv
import wikipedia
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
from chromaVectorDb import ChromaVectorDb

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_CHAT_MODEL = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
EMBEDDING_MODEL = 'togethercomputer/m2-bert-80M-8k-retrieval'
client = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=OPENAI_API_KEY
)


db= ChromaVectorDb()

collection = db.create_collection()

def extract_content(term:str)->str:
    page_pys = wikipedia.search(term, results = 1)
    if not page_pys:
        return f'Không tìm thấy nội dung tìm kiếm {term} trên wikipedia'
    else :
       
        pageUrl = wikipedia.page(page_pys[0]).url
        response =requests.get(pageUrl)
        if response.status_code == 200:
            
             soup = BeautifulSoup(response.text, "html.parser")
             # Initialize variable
             paragraphs = get_artical_section(soup)

             for i in range(0, len(paragraphs)):
                 collection.add(documents=[paragraphs[i]], ids=[str(i)])
          
             return paragraphs
             

def search_query(query:str):
    q = collection.query(query_texts=[query], n_results=5)
    results = q["documents"]
    return results


def get_artical_section(soup: BeautifulSoup)->list[str]:
    paragraphs = []
    for tag in soup.find_all():
        if tag.name=="p":
         paragraphs.append(tag.text)

    return paragraphs

def embedding_str(text:str):
    response = client.embeddings.create(
        model = "togethercomputer/m2-bert-80M-8k-retrieval",
        input = text
        )
    return response.data[0].embedding


messages = []

messages = [{'role': 'system','content':"You are a helpful assistant. When the user asks about a topic, "
            "fetch the relevant information from Wikipedia and provide a concise answer"}]


tools = [
  {
      "type": "function",
      "function": {
          "name": "extract_content",
          "description": "Fetch data of famous people on wikipedia . Use this to get factual information.",
          "parameters": {
              "type": "object",
              "properties": {
                  "term": {
                      "type": "string",
                      "description": "The name of person"
                  }
              },
              "required": ["term"],
              "additionalProperties": False
          }
      }
  },
  {
      "type": "function",
      "function": {
          "name": "search_query",
          "description": "The user's infomartion like : birthday, hometown, family, songs, bets,baby, parent, mother,sister...",
          "parameters": {
              "type": "object",
              "properties": {
                  "query": {
                      "type": "string",
                      "description": "The original of user's input"
                  }
              },
              "required": ["query"],
              "additionalProperties": False
          }
      }
  }
]


FUNCTION_MAP = {
    "extract_content": extract_content,
    "search_query":search_query
}


def generate_prompt(context: str,query:str)->str:
    prompt = f"""
    Use the following CONTEXT to answer the QUESTION at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use an unbiased and journalistic tone.

    CONTEXT: {context}

    QUESTION: {query}
    """
    return prompt


def get_completion(messages):
    # chat completions API
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=messages,
        tools=tools,
        temperature=0,
        max_tokens=5000
    )
    return response


while True:
    user_question = input('Hãy nhập thông tin bạn muốn tìm trên wikipedia:')

    if(user_question.lower() == 'exist'):
        break
    
    messages.append({'role': 'user', 'content': user_question})
    response = get_completion(messages)
    first_choice = response.choices[0]
    finish_reason = first_choice.finish_reason

    while finish_reason != "stop":
        tool_calls = first_choice.message.tool_calls
        if not tool_calls:
            print("No tool calls returned by the LLM.")
            break

        tool_call = first_choice.message.tool_calls[0]
        tool_call_function = tool_call.function
        tool_call_arguments = json.loads(tool_call_function.arguments)
        tool_call_name = tool_call_function.name

        print('==================================>')
        print(tool_call_name)
        # tool_function = FUNCTION_MAP[tool_call_function.name]
        # results = tool_function(**tool_call_arguments)
        result_message=''
      
        if tool_call_name == 'extract_content':
             term = tool_call_arguments.get('term')
             result_message = extract_content(term)

        if tool_call_function.name == 'search_query':
            query =  tool_call_arguments.get('query')
            results = search_query(query)
            result_message = generate_prompt(results,query)


        messages.append(first_choice.message)
        messages.append({
            'role':'tool',
            'tool_call_id': tool_call.id,
            'name':tool_call_name,
            'content':  json.dumps({"result": result_message}) 
        })

        response = get_completion(messages)
        first_choice = response.choices[0]
        finish_reason = first_choice.finish_reason

    messages.append(
        {"role": "assistant", "content": first_choice.message.content}
    )