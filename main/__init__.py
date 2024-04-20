#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9813287
API_HASH = "b5de20c46fb8f2e1b4aa393dea1ffe03"
BOT_TOKEN = "5212081719:AAGEqCcHWYX5xQDVQ7GP9vX5Z097tzDNX-A"
SESSION = "BQCVvScAjMQoDpH7pdjWaSSzcErDiviEvBZujK2FpB6ENudBPzQ3od0C66yKqrx-RaHLy9CgPREH9vD0Bo-UHVkLOlU3c5ksD8UbNQqK4YKWdJnA3xP2dumUMPMam3-8zU04v30E7p3POSPNZ_h0qxkbb5uNva66VFwwI4snd45xDmkCIrPp0HZYwJ35jYspPcv0JqZY5AqJFFSZevaxDmlGVfcvG-Yqmh2TWmwjQH0IQHSnHsihPY3iIkC_EBGKRDuWbEDO6jYuDZBY9kXnoVfBunHbavVDGwhpqGZEgxDbXkG-bfRCA9KZmvtQAcjmUFJDDAH19TAiq8vUGcZq2ifn4vWROAAAAAA9xQydAA"
FORCESUB = "Wolfy004"
AUTH = 1036323997

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
