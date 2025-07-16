
#Company OnBoarding Services OnboardAI

#company onboarding solutions.
# imports

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Initialization

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
#
MODEL = "gpt-4o-mini"
openai = OpenAI()
OLLAMA_API = "http://localhost:11434/api/chat"
# HEADERS = {"Content-Type": "application/json"}
# MODEL = "llama3.2"

system_message = (
    "You are an HR onboarding assistant. "
    "Use the available tools to create employee profiles or get welcome news. "
    "Always use tools instead of answering manually if possible."
)

# Let's start by making a useful function
import uuid
from datetime import datetime
employee_db = {}
def createEmployeeProfile(name: str, email: str, department: str, startDate: str):
    datetime.strptime(startDate, "%Y-%m-%d")
    employee_id = str(uuid.uuid4())
    # Create profile
    profile = {
        "employeeId": employee_id,
        "name": name,
        "email": email,
        "department": department,
        "startDate": startDate,
         "status": "Onboarded",


        }
    employee_db[employee_id] = profile
    return {
            "success": True,
            "message": "Employee profile created successfully.",
            "data": profile
        }

new_employee = createEmployeeProfile(
    name="John Doe",
    email="john.doe@company.com",
    department="Sales",
    startDate="2025-07-20"
)

print(new_employee)


# Define your model and system message
# Tools list
tools = [
    {
        "type": "function",
        "function": {
            "name": "createEmployeeProfile",
            "description": "Create a new employee profile in the internal onboarding system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Full name of the employee."},
                    "email": {"type": "string", "description": "Email address of the employee."},
                    "department": {"type": "string", "description": "Department name."},
                    "startDate": {"type": "string", "format": "date", "description": "Joining date in YYYY-MM-DD format."}
                },
                "required": ["name", "email", "department", "startDate"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "getWelcomeNews",
            "description": "Fetch top 3 HR-relevant news headlines to include in welcome messages.",
            "parameters": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "description": "2-letter country code (e.g., 'us', 'in').",
                        "default": "us"
                    },
                    "category": {
                        "type": "string",
                        "description": "News category (e.g., 'business', 'technology').",
                        "default": "general"
                    }
                },
                "required": []
            }
        }
    }
]


def chat(message, history):
    # Prepare messages
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    # First GPT call
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    choice = response.choices[0]

    # Tool call detected
    if choice.finish_reason == "tool_calls":
        tool_message = choice.message

        # ✅ Append assistant tool call message
        messages.append({
            "role": "assistant",
            "tool_calls": tool_message.tool_calls,
            "content": None
        })

        # ✅ Append tool function response message
        tool_response = handle_tool_call(tool_message)
        messages.append(tool_response)

        # Re-ask GPT for final reply
        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages
        )

    final_reply = response.choices[0].message.content or "Sorry, no response."
    return final_reply





def handle_tool_call(tool_message):
    tool_call = tool_message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print(f"[Tool Call] {function_name} with {arguments}")

    # Route the function call
    if function_name == "createEmployeeProfile":
        result = createEmployeeProfile(**arguments)
    elif function_name == "getWelcomeNews":
        result = getWelcomeNews(**arguments)
    else:
        result = {"error": f"Unknown tool: {function_name}"}

    # ✅ Tool response message (OpenAI format)
    tool_response = {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)  # must be string!
    }

    return tool_response

import requests
NEWS_API_KEY='848c039970f34ab2907556fbf1df58c5'

def getWelcomeNews(country="IN", category="Business"):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "category": category,
        "pageSize": 3
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        headlines = [{"title": a["title"], "url": a["url"]} for a in articles[:3]]

        return {
            "success": True,
            "headlines": headlines
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }

import gradio as gr

# Assuming you have: `chat(message, history)` and `createEmployeeProfile` etc. defined above

with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(label="AI Assistant", height=500, type="messages")
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
    with gr.Row():
        clear = gr.Button("Clear")

    def do_entry(message, history):
        history.append({"role": "user", "content": message})
        reply = chat(message, history)  # This will call OpenAI + tool logic
        history.append({"role": "assistant", "content": reply})
        return "", history

    entry.submit(do_entry, inputs=[entry, chatbot], outputs=[entry, chatbot])
    clear.click(lambda: [], outputs=chatbot, queue=False)

ui.launch(inbrowser=True)
