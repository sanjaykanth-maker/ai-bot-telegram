from pyrogram.types import (
  Message, 
)
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
import re

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
TOKEN = os.environ.get("TOKEN", None) 
BOT_ID = os.environ.get("BOT_ID", None)
KUKI_KEY = os.environ.get("KUKI_KEY", None)


kuki = Client(
      "KukiBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TOKEN,
)

@kuki.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/botname/owner/message={msg}").json()

  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


messageprivate = '''
Hi, I'm dmcj Chat Bot
'''

messagegroup = '''
Hi, I'm dmcj Chat Bot
'''





@kuki.on_message(filters.command("start"))
async def start(_, message):
    self = await kuki.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("dmcj", url="https://dmcj.co.in/"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))




kuki.run()
