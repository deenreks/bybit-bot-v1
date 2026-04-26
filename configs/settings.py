import os
from dotenv import load_dotenv

load_dotenv()

# SERVER
SERVER_ID = os.getenv("SERVER_ID")
BOT_NAME = os.getenv("BOT_NAME")

# API
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

# TELEGRAM
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# SYSTEM
LOCK_URL = os.getenv("LOCK_URL")
HEALTH_URL = os.getenv("HEALTH_URL")

# BEHAVIOR
SLEEP_TIME = int(os.getenv("SLEEP_TIME", 5))
RETRY_COUNT = int(os.getenv("RETRY_COUNT", 3))
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", 10))

# ALERTS
START_MESSAGE = os.getenv("START_MESSAGE")
FAILOVER_MESSAGE = os.getenv("FAILOVER_MESSAGE")
CRASH_MESSAGE = os.getenv("CRASH_MESSAGE")