#%%
# imports
# If these fail, please check you're running from an 'activated' environment with (llms) in the command prompt

import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

openai = OpenAI()
#%%
# here is the question; type over this to ask something new
system_prompt = "You are an assistant that analyzes the code given  \
and provides a short description of code with explanation. \
Respond in markdown."

def user_prompt(code):
    question = "Explain me what this code does and why :"
    question += code
    return question.format(code=code)

def messages_for(code):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt(code)}
    ]
def explain(code):
    payload = {
        "model": MODEL_LLAMA,
        "messages": messages_for(code),
        "stream": False
    }
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    return response.json()['message']['content']

def code_explain(code):
    summary = explain(code)
    display(Markdown(summary))

code_explain("requests.post(OLLAMA_API, json=payload, headers=HEADERS)")
