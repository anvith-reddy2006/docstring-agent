# config.py

import os
from dotenv import load_dotenv

# Load .env from current directory explicitly
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY not found in environment variables.")
    print("Please ensure .env file exists with GROQ_API_KEY=your_key")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script directory: {os.path.dirname(__file__)}")
    exit(1)

try:
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)
    print("✅ GROQ client initialized successfully")
except ImportError:
    print("Error: groq package not installed. Please run: pip install -r requirements.txt")
    exit(1)

MODEL_NAME = "llama-3.3-70b-versatile"

