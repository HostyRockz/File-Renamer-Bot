import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config

from pyrogram import Client, filters    
from translation import Translation

@Client.on_message(filters.command("start"))
async def start(client, message):
  await client.send_message(chat_id=message.chat.id, text=f"YO")
