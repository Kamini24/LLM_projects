import os
import requests
from bs4 import BeautifulSoup
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import json

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')


if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

openai = OpenAI()

system_message = "You are a helpful assistant"
  
def stream_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    stream = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


def messages_for(prompt):
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

def stream_ollama(prompt):
    payload = {
        "model": MODEL,
        "messages": messages_for(prompt),
        "stream": True
    }

    response = ""
    with requests.post(OLLAMA_API, json=payload, headers=HEADERS, stream=True) as result:
        for chunk in result.iter_lines(decode_unicode=True):
            if chunk.strip():
                data = json.loads(chunk)
                token = data.get("message", {}).get("content", "")
                response += token
                yield response


def stream_model(prompt, model):
    if model=="GPT":
        result = stream_gpt(prompt)
    else:
       result = stream_ollama(prompt)
    yield from result

view = gr.Interface(
    fn=stream_model,
    inputs=[gr.Textbox(label="Your message:"), gr.Dropdown(["GPT", "Ollama"], label="Select model", value="GPT")],
    outputs=[gr.Markdown(label="Response:")],
    flagging_mode="never"
)
view.launch(inbrowser=True)
