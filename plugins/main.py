import logging
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


@Client.on_message(filters.command("start"))
async def start(client, message):
    chatid = message.chat.id
    name = await Client.ask(chatid, 'YOUR NAME')
    got = name.text
    await Client.send_message(chat_id=message.chat.id, text=f"{got}")
