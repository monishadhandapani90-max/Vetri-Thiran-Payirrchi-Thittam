import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Explicitly locate and load .env file from project root
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Retrieve the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing or empty! "
        "Please check your .env file and ensure it is formatted as: GEMINI_API_KEY=your_key_here"
    )

# Configure the Gemini client
client = genai.Client(api_key=api_key)
def answer_question_with_gemini(question: str) -> str:
    """
    Generates an answer using the Gemini API for a given user prompt.
    """
    if not question or not question.strip():
        return "Please enter a valid question."

    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        response = model.generate_content(question)
        
        if response and hasattr(response, "text"):
            return response.text
        return "No response received from the Gemini model."
        
    except Exception as e:
        return f"Error in QnA Module: {str(e)}"