# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "MrUnknown")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "@MrUnknown114")

# Account
API_HASH = os.environ.get("API_HASH", "")
API_ID = os.environ.get("API_ID", "")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PICS = os.environ.get("PICS", "https://telegra.ph/file/17a668f74d66f7f783047.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "vpsteaster1")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://vpsteaster1:LHz6YGCGQt3gBPwZ@cluster0.nqm5e2l.mongodb.net/?retryWrites=true&w=majority")
# Chats & Users
ADMINS = os.environ.get("ADMINS", "1418002763")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "the_seeker_s_cave")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001707091598")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001656311343").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001690180221")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001656311343")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "600"))

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
