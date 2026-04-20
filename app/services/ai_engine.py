from openai import OpenAI
import os
from config import OPENAI_API_KEY
from data.college_data import college_data

# Get API key from env or config
api_key = os.getenv("OPENAI_API_KEY") or OPENAI_API_KEY

# Initialize client only if key exists
client = OpenAI(api_key=api_key) if api_key else None


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

    # Handle missing API key (important for Docker/CI)
    if client is None:
        return "AI service not configured (missing API key)"

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return "AI service is currently unavailable"