import os

class Config(object):
    # Get a bot token from BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is required")

    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = os.environ.get("APP_ID")
    if not APP_ID:
        raise ValueError("APP_ID is required")
    APP_ID = int(APP_ID)

    API_HASH = os.environ.get("API_HASH")
    if not API_HASH:
        raise ValueError("API_HASH is required")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set()
    auth_users = os.environ.get("AUTH_USERS")
    if auth_users:
        AUTH_USERS = set(int(x) for x in auth_users.split() if x.isdigit())
    else:
        raise ValueError("AUTH_USERS must be set and should be a space-separated list of integers")

