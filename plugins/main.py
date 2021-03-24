from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


@bot.on_message(filters.command("start"))
async def start(client, message):
    chatid = message.chat.id
    name = await bot.ask(chatid, 'YOUR NAME')
    got = name.text
    await bot.send_message(chat_id=message.chat.id, text=f"{got}")
