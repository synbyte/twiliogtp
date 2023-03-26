import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.ChatCompletion()

start_chat_log = [
    {"role": "system", "content": "You are a sales representative for a payment software company. The softwares selling point is it processes payment data and stores it in any format you choose, allowing you to never be locked into any one merchants format all while keeping it tokenized and secure.  Your task is to pitch your product to potential clients. Respond to the following prompt: 'Can you tell me more about the benefits of using your payment software for my business?'"},
]
def askgpt(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    chat_log = chat_log + [{'role': 'user', 'content': question}]
    response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
    answer = response.choices[0]['message']['content']
    chat_log = chat_log + [{'role': 'assistant', 'content': answer}]
    return answer, chat_log
