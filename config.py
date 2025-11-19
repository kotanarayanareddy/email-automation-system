from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL") or os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("PASSWORD") or os.getenv("EMAIL_PASSWORD")

if not EMAIL_USER or not EMAIL_PASSWORD:
    raise Exception("ERROR: EMAIL_USER or EMAIL_PASSWORD not found in environment variables")
