#========================================================================
# Don't Remove Credit Tg - @TDBotDev
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TDBotDev
# Ask Doubt on telegram https://t.me/TDBotDev
#========================================================================
import os
import random
from dotenv import load_dotenv

# config.py
load_dotenv()

API_ID = int(os.environ.get("API_ID", "35282740"))
API_HASH = os.environ.get("API_HASH", "3776eec38f32dfac0d8dc849a6a5a047")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8946189722:AAGlFUGrxwZqtYUDoCgwCaVQXL0RHlgKunQ")

# Search Settings
DB_CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", "-1003827120818"))
START_TEXT = os.environ.get("START_TEXT", "𝗛𝗲𝘆 𝗙𝗿𝗶𝗲𝗻𝗱𝗼𝗼\n𝗜 𝗔𝗺 𝗠𝗼𝘃𝗶𝗲𝘀 𝗕𝗼𝘁, 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗚𝗲𝘁 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀 𝗛𝗲𝗿𝗲 ✨!\n𝗝𝘂𝘀𝘁 𝗧𝘆𝗽𝗲 𝗠𝗼𝘃𝗶𝗲 𝗢𝗿 𝗦𝗲𝗿𝗶𝗲𝘀 𝗡𝗮𝗺𝗲 📛\n𝗖𝗼𝗿𝗿𝗲𝗰𝘁𝗹𝘆 𝗔𝗻𝗱 𝗚𝗲𝘁 𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗙𝗶𝗹𝗲𝘀 📁\n𝗗𝗼𝗻❜𝘁 𝗙𝗼𝗿𝗴𝗲𝘁 𝗧𝗼 𝗦𝗵𝗮𝗿𝗲 𝗠𝗲 𝗪𝗶𝘁𝗵 𝗬𝗼𝘂𝗿 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 🤗")
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", 10))

# Help and About Texts
HELP_TEXT = os.environ.get("HELP_TEXT", "📖 **Help Menu**\n\n1. Send any movie or series name to search.\n2. Use the quality and language filters to narrow down results.\n3. Click on the file name to receive it instantly.")
ABOUT_TEXT = os.environ.get("ABOUT_TEXT", "❄️ **About This Bot**\n\nThis is a high-speed file storage and search bot for CineVerse users. It indexes thousands of files and provides them with minimal delay.\n\nDeveloper: [ @TDBotDev ]")

# Database Settings
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://iphone1234:hydra123@cluster1.cc8x4jf.mongodb.net/?appName=Cluster1")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "autofilebot")
COLLECTION_NAME = "files"

# Optional settings
OWNER_ID = int(os.environ.get("OWNER_ID", "5725682503"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "5725682503").split(",") if x]  # multiple admins allowed ("8475661555","8475661555")

# Force Subscribe Settings
# Updated to multiple channels as per user request
FORCE_SUB_CHANNELS = [int(x) for x in os.environ.get("FORCE_SUB_CHANNELS", "-1002493712153,-1003923865001").split(",") if x] # multiple force sub allowed ("-1003511440278","-1003511440278")
ADMIN_IDS = ADMINS + [OWNER_ID]
FORCE_SUB_TEXT = os.environ.get("FORCE_SUB_TEXT", "📥 **𝗣𝗹𝗲𝗮𝘀𝗲 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁!**\n\n𝗗𝘂𝗲 𝘁𝗼 𝗵𝗶𝗴𝗵 𝘀𝗲𝗿𝘃𝗲𝗿 𝗹𝗼𝗮𝗱, 𝗢𝗻𝗹𝘆 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝗲𝗮𝗿𝗰𝗵 𝗳𝗶𝗹𝗲𝘀.")

# Updates Link
UPDATES = os.environ.get("UPDATES", "https://t.me/+2Ty1_CDfHNthN2M1")

# Auto-Delete Settings
AUTO_DELETE_TIME = os.environ.get("AUTO_DELETE_TIME", "1h") # Format: 30s, 1m, 1h, 1d or '0' to disable
DELETE_MESSAGE_TEXT = "⚠️ IMPORTANT:𝗔𝗹𝗹 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 {time}.𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗮𝘃𝗲 𝗼𝗿 𝗳𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗲𝗺 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗦𝗮𝘃𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀."

# UI Images
PICS = [
    "https://kommodo.ai/i/5T7I2MFpTh829uZGitm5"
]

def get_random_pic():
    return random.choice(PICS)

# Initial images
START_PIC = PICS[0]
FORCE_PIC = PICS[0]

# Bot Commands
BOT_COMMANDS = [
    ("start", "🚀 Start the bot"),
    ("help", "🆘 How to use the bot"),
    ("delete_file", "🗑️ Delete your DB files (admin)"),
    ("broadcast", "⚡ Broadcast message (admin)"),
    ("status", "👀 Bot statistics (admin)"),
    ("reset", "❌ Total reset (only owner)")
]

#========================================================================
# Don't Remove Credit Tg - @TDBotDev
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TDBotDev
# Ask Doubt on telegram https://t.me/TDBotDev
#========================================================================
