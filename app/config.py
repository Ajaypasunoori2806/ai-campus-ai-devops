from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional: debug check
if not OPENAI_API_KEY:
    print("⚠️ WARNING: OPENAI_API_KEY is not set")