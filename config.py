import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.getenv("APP_ID"))
    API_HASH = os.getenv("API_HASH")

    # Read USERS from .env (can still use static definition if needed)
    USERS = os.getenv("USERS", "7865959549")  # Default value in case .env is missing
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in USERS.split())
