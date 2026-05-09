from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_credentials():
    return {
        "api_key": API_KEY,
        "api_secret": API_SECRET
    }