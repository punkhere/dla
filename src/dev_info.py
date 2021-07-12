# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("Join Channel", url="https://t.me/watchlistonfire")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""Made with ❤️ in 🇮🇳 by @catch_punk, @pk_o3, @TechyNabil_xD(for logo design).

Language: [Python3](https://www.python.org/)

Bot Framework: [Pyrogram Asyncio](https://github.com/pyrogram/pyrogram)

donate: pawanpark8@okhdfcbank

Please donate and share for further support 👍👍""", reply_markup=reply_markup, parse_mode="markdown")
