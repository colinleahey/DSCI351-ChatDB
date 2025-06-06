from openai import OpenAI
from config import OPENAI_API_KEY

def get_openai_client():
    """Instantiate and return an OpenAI client."""
    return OpenAI(api_key=OPENAI_API_KEY)