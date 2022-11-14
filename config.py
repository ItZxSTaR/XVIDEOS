import os
import logging
import sys
import importlib

from telethon import TelegramClient
from decouple import config
from os import getenv
from pathlib import Path


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = "5587989733:AAFw5feo7D6QuTeIVjecpvZzEkUWhWYqIzA"
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
Altron = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

def load_plugins(plugin_name):
    path = Path(f"AltronX/modules/{plugin_name}.py")
    name = "AltronX.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["AltronX.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)
