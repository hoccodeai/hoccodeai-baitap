import requests
import yfinance as yf
import urllib3
from pydantic import TypeAdapter
import inspect
from openai import OpenAI
import os
import json
from pprint import pprint

 # Init openAI client
client = OpenAI(
    base_url="https://api.together.xyz/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://api.together.ai/settings/api-keys để lấy API Key nha
    api_key='010dde7e500cc647a52d1a92efd2c9ece8331a059942d6151cf916a4cb206420',
)

# Suppress SSL warning (use with caution)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_completion(messages):
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=messages,
        tools=tools,
        temperature=0
    )
    return response


def get_symbol(company:str) -> str:
    """
    Retrieve the stock symbol for a spectified company using the Yahoo Finance API.
    :param company: The name of the company for which to retrieve the stock symbol , e.g, 'Nvidia'.
    :output: The stock symbol for the spectified company

    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": company, "country": "United States"}
    user_agents = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/42.0.2311.135 Safari/537/36 Edge/12.246"}
    print('call get_symbol =============================================>')
    res = requests.get(
        url=url,
        params=params,
        headers= user_agents,
        verify=False
    )

    data =res.json()
    symbol= data['quotes'][0]['symbol']

    return symbol


def get_stock_price(symbol:str):
    """
    Retrieve the most recent stock price data for a specified company using the Yahoo Finance API via the yfinance Python library.
    :param symbol : The stock symbol for which to retrieve data, e.g, 'NVDA' for Nvidia.
    :output: A dictionary containing the most recent stock price data
    """
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    latest = hist.iloc[-1]
    print('call get_stock_price ===================================>')
    return {
        "timestamp" : str(latest.name),
        "open":latest["Open"],
        "high": latest["High"],
        "low":latest["Low"],
        "close":latest["Close"],
        "volume": latest["Volume"]
    }


tools = [
    {
        "type":"function",
        "function":{
            "name":"get_symbol",
            "description" : inspect.getdoc(get_symbol),
            "parameters": TypeAdapter(get_symbol).json_schema(),
        },
    },
    {
        "type":"function",
        "function":{
            "name": "get_stock_price",
            "description": inspect.getdoc(get_stock_price),
            "parameters" : TypeAdapter(get_stock_price).json_schema()
        }
    }
]


FUNCTION_MAP = {
    "get_symbol": get_symbol,
    "get_stock_price": get_stock_price
}


messages = [
    {"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user. You're analytical and sarcasm."},
]


while True:
    question = input("Có câu hỏi gì về không bạn ơi: ")

    if question.lower() in ['quit', 'close']:
        break

    messages.append(
        {"role": "user", "content": question}
    )

    response = get_completion(messages)
    first_choice = response.choices[0]
    finish_reason = first_choice.finish_reason

    pprint('finish_reason ==============================')
    pprint(finish_reason)

    while finish_reason != "stop":

        tool_call = first_choice.message.tool_calls[0]

        tool_call_function = tool_call.function
        tool_call_arguments = json.loads(tool_call_function.arguments)

        tool_function = FUNCTION_MAP[tool_call_function.name]
        result = tool_function(**tool_call_arguments)

        messages.append(first_choice.message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call_function.name,
            "content": result
        })
        pprint('second call ======================================')
        pprint('messages ======================================')
        pprint(messages)
        # Chờ kết quả từ LLM
        response = get_completion(messages)
        first_choice = response.choices[0]
        finish_reason = first_choice.finish_reason
        pprint('second choice====================================================================')
        pprint (first_choice)

    print(f"BOT: {first_choice.message.content}")
    messages.append(
        {"role": "assistant", "content": first_choice.message.content}
    )


# def demo_symbol(question :str):
#     messages =[
#         {'role': 'system', 'content':'You are a helpful customer support assistant. Use the supplied tools to assist the user'},
#         {'role':'user','content': question}
#        ]

#      # call openAI and get response
#     response = get_completion(messages)

#     first_choice = response.choices[0]
#     # get function-call from LLM
#     tool_call = first_choice.message.tool_calls[0]
#     tool_call_function = tool_call.function
#     tool_call_arguments =  json.loads(tool_call.function.arguments)

#     # run function in local
#     if tool_call_function.name == 'get_symbol':
#         result= get_symbol(tool_call_arguments['company'])

#     elif tool_call.function.name == 'get_stock_price':
#         result = get_stock_price(tool_call_arguments['symbol'])
       

#     else:
#         print('khong tim thay function')

#     print(result)
#     print('=====================================')
#     # gui ket qua len cho LLM 
#     messages.append(first_choice.message)
#     messages.append({
#         'role' : 'tool',
#         "content" :result,
#         "tool_call_id": tool_call.id,
#         "name": tool_call_function.name
#     })

#     final_question1_response = get_completion(messages)
    
#     print(final_question1_response.choices[0].message)

    
# if __name__ == "__main__":

#     user_question = input('Bạn: ')

#     demo_symbol(user_question)


    

