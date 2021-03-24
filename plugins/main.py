import logging
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text="YO",
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
