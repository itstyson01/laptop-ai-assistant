import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash"
)


def ask_gemini(prompt: str) -> str:
    response = chat.send_message(prompt)


    return response.text