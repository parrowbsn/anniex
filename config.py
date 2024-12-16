import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = int(getenv("API_ID", "0"))  # Fill with a default or leave it
API_HASH = getenv("API_HASH", "your_api_hash_here")
BOT_TOKEN = getenv("BOT_TOKEN", "your_bot_token_here")

# Bot configuration
OWNER_USERNAME = getenv("OWNER_USERNAME", "Harshu_Raven")
BOT_USERNAME = getenv("BOT_USERNAME", "VC_INFINITE_X_BOT")
BOT_NAME = getenv("BOT_NAME", "˹𝑪𝒖𝒕𝒊𝒆 ✘ 𝒎𝒖𝒔𝒊𝒄˼")
ASSUSERNAME = getenv("ASSUSERNAME", "Cuties_assistant")
OWNER_ID = int(getenv("OWNER_ID", "12345678")
STRING1 = getenv("STRING1", ""))
# MongoDB URI
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Logger and Duration Configuration
LOGGER_ID = int(getenv("LOGGER_ID", "-1001234567890"))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT_MIN", "60"))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60

# External APIs
GPT_API = getenv("GPT_API", None)
DEEP_API = getenv("DEEP_API", None)
GIT_TOKEN = getenv("DEEP_API", None)

# Heroku Deployment Settings
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/MRXBROKEN011/anniex")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# Spotify API
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Support URLs
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sparrow_Bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Raven_Legion")

# URL Validation
def validate_url(url, name):
    if url and not re.match(r"(?:http|https)://", url):
        raise SystemExit(f"[ERROR] - Your {name} URL is invalid. It must start with https://")
    return url

validate_url(SUPPORT_CHANNEL, "SUPPORT_CHANNEL")
validate_url(SUPPORT_CHAT, "SUPPORT_CHAT")

# Static Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://ibb.co/5sxk5Fb")
PING_VID_URL = getenv("PING_VID_URL", "https://ibb.co/5sxk5Fb")
PLAYLIST_IMG_URL = "https://ibb.co/zngBHKS"

# Limits and Flags
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Helper: Convert Time
def time_to_seconds(time_str):
    try:
        return sum(int(x) * 60**i for i, x in enumerate(reversed(time_str.split(":"))))
    except Exception as e:
        raise ValueError(f"Invalid time format: {time_str}. Expected HH:MM:SS.")

# Precompute Duration Limit
try:
    DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
except ValueError as e:
    raise SystemExit(f"[ERROR] - {e}")

# Dynamic Dictionaries
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Developer Information
DEV_MSG = """
Hello {0}, 🥀

It's me, {1}!

Supporting Platforms:
YouTube, Spotify, Resso, Apple Music, SoundCloud, etc.

Uptime: {2}
Server Storage: {3}
CPU Load: {4}
RAM Consumption: {5}
Users: {6}
Chats: {7}

Developer: 👑 [Harshu Raven](https://t.me/Harshu_Raven)
"""
