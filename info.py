import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29882686'))
API_HASH = environ.get('API_HASH', 'b642a25aee67b2aed02116df4a916bca')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://envs.sh/fHy.jpg https://envs.sh/fge.jpg https://envs.sh/fra.jpg https://envs.sh/fHV.jpg https://envs.sh/fsB.jpg https://envs.sh/fgi.jpg https://envs.sh/fsn.jpg https://envs.sh/fgD.jpg https://envs.sh/fgb.jpg https://envs.sh/fsS.jpg https://envs.sh/fgP.jpg https://envs.sh/fgh.jpg https://envs.sh/fsT.jpg https://envs.sh/fgw.jpg https://envs.sh/fsA.jpg https://envs.sh/fgF.jpg https://envs.sh/fgq.jpg https://envs.sh/fs_.jpg https://envs.sh/fgt.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/aPc.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/7478ff3eac37f4329c3d8.jpg https://graph.org/file/56b5deb73f3b132e2bb73.jpg')).split()  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6316008361 6157414954 6796307271').split()] # Replace with the actual admin ID(s) to add
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002434598772').split()]  # Channel id for auto indexing (make sure bot is admin)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002122152204'))  # Log channel id (make sure bot is admin)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002370487322'))  # Bin channel id (make sure bot is admin)
DEENDAYAL_MOVIE_UPDATE_CHANNEL = int(environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL', '-1002116325676'))  # Notification of those who verify will be sent to your channel
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002122152204'))  # Premium logs channel id
auth_channel = environ.get('AUTH_CHANNEL', '-1002429510787')  # Channel/Group ID for force sub (make sure bot is admin)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002370487322').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002431912132')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002116325676')  # Request channel id (make sure bot is admin)
AUTH_CHANNEL = [int(fch) if id_pattern.search(fch) else fch for fch in environ.get('AUTH_CHANNEL', '-1002429510787').split()]
MULTI_FSUB = [int(channel_id) for channel_id in environ.get('MULTI_FSUB', '-1002429510787 -1002116325676').split() if re.match(r'^-?\d+$', channel_id)]  # Channel for force sub (make sure bot is admin)


# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/aPL.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'sukhwindersingh48396-3@okhdfcbank')

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sandhusaab61291:Sandhu@cluster0.c67tt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://sandhusaab050505:Sandhu2@cluster0.lfrnj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "sandhusaab61291")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Deendayal_files')

# ============================
# Movie Notification & Update Settings
# ============================
DEENDAYAL_MOVIE_UPDATE_NOTIFICATION = bool(environ.get('DEENDAYAL_MOVIE_UPDATE_NOTIFICATION', True))  # Notification On (True) / Off (False)
DEENDAYAL_IMAGE_FETCH = bool(environ.get('DEENDAYAL_IMAGE_FETCH', True))  # On (True) / Off (False)
CAPTION_LANGUAGES = ["Bhojpuri", "Hindi", "Bengali", "Tamil", "English", "Bangla", "Telugu", "Malayalam", "Kannada", "Marathi", "Punjabi", "Bengoli", "Gujrati", "Korean", "Gujarati", "Spanish", "French", "German", "Chinese", "Arabic", "Portuguese", "Russian", "Japanese", "Odia", "Assamese", "Urdu"]

# ============================
# Verification Settings
# ============================
VERIFY = bool(environ.get('VERIFY', False))  # Verification On (True) / Off (False)
DEENDAYAL_VERIFY_EXPIRE = int(environ.get('DEENDAYAL_VERIFY_EXPIRE', 24))  # Add time in hours
DEENDAYAL_VERIFIED_LOG = int(environ.get('DEENDAYAL_VERIFIED_LOG', '-1002122152204'))  # Log channel id (make sure bot is admin)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/+dVRLYHXJztJlMmY9')  # How to open tutorial link for verification

# ============================
# Link Shortener Configuration
# ============================
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shortxlinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '820b18ededb2ed6cf4de90d828e900add9a1a60d')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/+dVRLYHXJztJlMmY9')  # Tutorial video link for opening shortlink website
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+_-9trQQYYFczNTJl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/OttSandhu')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Ott_Sandhu_Owner_bot')
DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK = environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK', 'https://t.me/+nBnb3csEICIyNWM1')
OWNERID = int(os.environ.get('OWNERID', '6796307271'))  # Replace with the actual admin ID

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '0').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '0').split()]

# ============================
# Miscellaneous Configuration
# ============================
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))  # True if you want no results messages in Log Channel
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+mrrgTUvDf5YyY2Q1')  # Support group link (make sure bot is admin)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False) # pm & Group button or link mode (True) / Off (False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
IMDBSEARCH_TEMPLATE = environ.get("IMDBSEARCH_TEMPLATE", f"{script.IMDBSEARCH_TEMPLATE}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002434598772')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))  # PM Search On (True) / Off (False)

# ============================
# Bot Configuration
# ============================
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

# ============================
# Server & Web Configuration
# ============================

STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False
NO_PORT = bool(environ.get('NO_PORT', True))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'DeendayalBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Deendayal'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]



# ============================
# Command admin
# ============================
commands = [
    """• /system - <code>sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏн...</code>
• /movie_update - <code>ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>""",

    """• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <codeʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>""",

    """• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""
]



# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("SINGLE_BUTTON is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")

