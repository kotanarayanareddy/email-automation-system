from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Gmail credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Safety check
if not EMAIL_USER or not EMAIL_PASSWORD:
    raise Exception("ERROR: EMAIL_USER or EMAIL_PASSWORD not found in .env file")