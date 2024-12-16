#MrBroken©
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID")) #⚠️fill or leave
API_HASH = getenv("API_HASH") #⚠️fill or leave
BOT_TOKEN = getenv("BOT_TOKEN") #⚠️fill or leave 

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME", "Harhsu_Raven") #⚠️replace 
BOT_USERNAME = getenv("BOT_USERNAME", "VC_INFINITE_X_BOT") #⚠️replace
BOT_NAME = getenv("BOT_NAME", "˹𝑪𝒖𝒕𝒊𝒆 ✘ 𝒎𝒖𝒔𝒊𝒄˼") #⚠️replace
ASSUSERNAME = getenv("ASSUSERNAME", "Cuties_assistant") #⚠️Replace
EVALOP = list(map(int, getenv("EVALOP", "8004931028").split())) 
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1002314897715)) #⚠️REPLACE
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
DEEP_API = getenv("DEEP_API")
OWNER_ID = int(getenv("OWNER_ID", 8004931028)) #⚠️REPLACE

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/MRXBROKEN011/anniex") #⚠️Don't Change
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master") #⚠️Don't Change
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sparrow_Bots") #⚠️Replace
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Raven_Legion") #⚠️Replace

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b") #replace with your
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773") #replace with your
"ʜᴇʟʟᴏ {0}, 🥀

ɪᴛ'ꜱ ᴍᴇ {1} !

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,
┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.
┗━━━━━━━━━━━━━━━━━⧫
┏━━━━━━━━━━━━━━━━━⧫
┠ ➥ Uᴘᴛɪᴍᴇ : {2}
┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}
┠ ➥ CPU Lᴏᴀᴅ : {4}
┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}
┠ ➥ ᴜꜱᴇʀꜱ : {6}
┠ ➥ ᴄʜᴀᴛꜱ : {7}
┗━━━━━━━━━━━━━━━━━⧫

🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [Hᴀʀsʜᴜ Rᴀᴠᴇɴ](https://t.me/Harshu_Raven)",
    "ʜᴇʟʟᴏ {0}, 🥀

ɪᴛ'ꜱ ᴍᴇ {1} !

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,
┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.
┗━━━━━━━━━━━━━━━━━⧫
┏━━━━━━━━━━━━━━━━━⧫
┠ ➥ Uᴘᴛɪᴍᴇ : {2}
┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}
┠ ➥ CPU Lᴏᴀᴅ : {4}
┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}
┠ ➥ ᴜꜱᴇʀꜱ : {6}
┠ ➥ ᴄʜᴀᴛꜱ : {7}
┗━━━━━━━━━━━━━━━━━⧫

🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [Hᴀʀsʜᴜ Rᴀᴠᴇɴ](https://t.me/Harshu_Raven)"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "http://ibb.co/5sxk5Fb"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "http://ibb.co/5sxk5Fb"
)
PLAYLIST_IMG_URL = "http://ibb.co/zngBHKS"
STATS_VID_URL = "http://ibb.co/zngBHKS"
TELEGRAM_AUDIO_URL = "http://ibb.co/zngBHKS"
TELEGRAM_VIDEO_URL = "http://ibb.co/zngBHKS"
STREAM_IMG_URL = "http://ibb.co/1s8jhdw"
SOUNCLOUD_IMG_URL = "http://ibb.co/zngBHKS"
YOUTUBE_IMG_URL = "http://ibb.co/1s8jhdw"
SPOTIFY_ARTIST_IMG_URL = "http://ibb.co/1s8jhdw"
SPOTIFY_ALBUM_IMG_URL = "http://ibb.co/1s8jhdw"
SPOTIFY_PLAYLIST_IMG_URL = "http://ibb.co/1s8jhdw"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
