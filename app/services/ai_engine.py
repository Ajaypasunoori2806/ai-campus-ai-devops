from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.data.college_data import college_data

client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(message, context):
    prompt = f"""
You are a smart AI assistant for a college campus.

Use the following college data to answer:

{college_data}

Conversation history:
{context}

User question:
{message}

Answer clearly and helpfully like a real assistant.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "AI service is currently unavailable"