import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("BOSON_API_KEY"),
    base_url=os.getenv("BOSON_BASE_URL", "https://hackathon.boson.ai/v1"),
)