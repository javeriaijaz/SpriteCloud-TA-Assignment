import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # UI Automation Config
    BROWSER = os.getenv("BROWSER", "chrome")  # Default to Chrome
    BASE_URL = os.getenv("BASE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    # API Automation Config
    API_BASE_URL = os.getenv("API_BASE_URL")
    TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
    TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
