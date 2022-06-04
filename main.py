from pyrogram import Client, filters
import random
from typing import Union
from config import Config
from logo import generate_logo
from logo import get_wallpapers, get_unsplash
from pyrogram.types import *
import result
from pyrogram.types import InputMediaPhoto, User, Message, InlineQueryResultPhoto, InlineQueryResult, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, Chat
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied, FloodWait
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import filters
from telegram import Message, MessageId
from telegram.ext import CallbackContext, Filters, MessageHandler
from telegram.error import ChatMigrated
from telegram.update import Update
from pyrogram.types import Message
from pyrogram import Client
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


caption = """
✍️ User Info Bot 🇱🇰

◇───────────────◇

🚀 ** You Id ** ➳ ´{}´

🌺 **You Name** : #press Button(my name)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """
caption2 = """
✍️ User Info Bot 🇱🇰

◇───────────────◇

🚀 ** You name ** ➳ {}

🌺 **You id ** : #press Button(my id)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

caption3 = """
✍️ Wallpaper Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  
    """

caption4 = """
✍️ Logohq Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  
    """

HELP = """

**🖼 How To Use Me ?**

**♻️ Example:** 

/logo NetwokTech
/logohq NetwokTech
/wall fish
/write NetwokTech
/slogo NetwokTech
/slogohq NetwokTech
/swall fish
/unsplash fish
"""
START = """

**🖼 How To Use Me ?**

Hello there, 💞💞

bot gen oyalata logo create karagannam
oyala bot wa oyalage onama group ekakata
add karala ehemath naththam bot inna group
ekata join wela @Network_techchat /logo command
eka bavitha karala logo create karaganna 
puluwan...ita passe bot logo eka create
karala euwama oyalata (send inbox) kiyana
inline button eka press karala oyalata
logo eka inbox ganna puluwan...

⭕️ Bot Command ⬇️

/logo NetwokTech
/logohq NetwokTech
/wall fish
/write NetwokTech
/slogo NetwokTech
/slogohq NetwokTech
/swall fish
/unsplash fish

"""

app = Client(
    'logo Bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
 
FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Network Tech 🇱🇰", url=f"https://t.me/NetworksTech") 
        ]]      
    )

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_sticker(sticker = "CAACAgUAAxkBAAIDTmIH_UzldE-IIKD0-N_n_hrcVhzRAAKaAwACKwAB-VTV1LdMsVUFGCME")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/12155d9fd310edf3fab33.jpg",
        caption = """
🍀 hello There 

🙋‍♂️ I am Logo Generate Bot,I can 

🌺 Generating logo
🌷 Generating wallpaper
🚀 Generating 4k logo
🍀 Writing Picture
🔥 **Inline search Image**
🎯 24 horse active

🔥 Bot Commands 🔥

/logo NetwokTech
/logohq NetwokTech
/wall fish
/write NetwokTech
/slogo NetwokTech
/slogohq NetwokTech
/swall fish
/unsplash fish

🌿 Developer : || @chamod_deshan ||

🔥 [Network Tech 🇱🇰](https://t.me/NetworksTech) Corporation ©️
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_logo_generate_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech 🇱🇰", url=f"https://t.me/NetworksTech"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech Chat 🇱🇰", url="https://t.me/Network_techchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷 Developer 🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🆘   help   🆘", callback_data="help"
                    )
                ],
                [
                    InlineKeyboardButton(text=
                       "◇────🔍 Search Here Image 🔎────◇", switch_inline_query_current_chat=""
                    )
                ]
           ]
        )
    )


@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/bd9a2bb25666a94f30211.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="<<< Back", callback_data="start_menu")]]), reply_to_message_id = message.message_id)   

@app.on_message(filters.command("about"))
async def about_(client: Client, message: Message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_sticker(sticker = "CAACAgUAAxkBAAIDTmIH_UzldE-IIKD0-N_n_hrcVhzRAAKaAwACKwAB-VTV1LdMsVUFGCME")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bd9a2bb25666a94f30211.jpg",
        caption = """

🔥 [Network Tech 🇱🇰](https://t.me/NetworksTech) Corporation ©️
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_logo_generate_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech 🇱🇰", url=f"https://t.me/NetworksTech"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech Chat 🇱🇰", url="https://t.me/Network_techchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷 Developer 🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🆘   help   🆘", callback_data="id"
                    )
                    
                ],
                [
                    InlineKeyboardButton(text=
                       "◇────🔍 Search Here Image 🔎────◇", switch_inline_query_current_chat=""
                    )
                ]
           ]
        )
    )

@app.on_message(filters.command("id"))
async def on_off_antiarab(_, message: Message):
    await message.reply("searching')
    photo = get(f"https://single-developers.up.railway.app/logo?name={message.from_user.id}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.id), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My name ✍", callback_data="name"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("name"))
async def on_off_antiarab(_, message: Message):
    status = await message.reply("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]), reply_to_message_id = message.message_id)
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    photo = get(f"https://single-developers.up.railway.app/logo?name={message.from_user.first_name}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption2.format(message.from_user.mention), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ]
            ]
          )
    )
 

@app.on_callback_query(filters.regex("id"))
async def button(app, update):
      cb_data = update.data
      if "id" in cb_data:
        await update.message.delete()
        await id(app, update.message)
      elif "name" in cb_data:
        await update.message.delete()
        await name(app, update.message)
      elif "ha" in cb_data:
        await update.message.delete()

@app.on_callback_query(filters.regex("namWje"))
async def help(_,query):
  await query.answer(f"🏖 Bot Help 🏖")
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="<<< Back", callback_data="start")]]))


@app.on_callback_query(filters.regex("help"))
async def help(_,query):
  await query.answer(f"🏖 Bot Help 🏖")
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="<<< Back", callback_data="start")]]))


app.run()
