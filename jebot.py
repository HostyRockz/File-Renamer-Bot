import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time
import aiohttp

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_utils.chat_base import TRChatBase
from helper_utils.display_progress import progress_for_pyrogram

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import Client, filters
from PIL import Image
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent

bot = Client(
   "Python Bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@bot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'supergroup':
      if (not client.get_chat_member(message.chat.id, message.from_user.id).status in ("administrator", "creator") and not user_id == 1674318962):
        await bot.send_message(chat_id=message.chat.id, text="""User""", parse_mode="html")
      else:
        await bot.send_message(chat_id=message.chat.id, text="""Admin""", parse_mode="html")

print("Yoo")

bot.run()
