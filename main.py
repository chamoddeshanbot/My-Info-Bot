from pyrogram import Client, filters
from config import Config
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import Message
from requests import get
import os


caption = """
✍️ User Info ✍️

◇───────────────◇

🚀 ** You Id ** ➳ `{}`

🌺 **You Name** : #press Button(my name)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """
caption2 = """
✍️ User Info ✍️

◇───────────────◇

🚀 ** You name ** ➳ {}

🌺 **You id ** : #press Button(my id)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

caption3 = """
✍️ User Info ✍️

◇───────────────◇

🚀 ** You Username ** ➳ ` {} `

🌺 **You id ** : #press Button(my id)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

captiont = """
🌿 Hello There {}

** 🤞🏿 User Info Bot 🇱🇰**

** How to Use Me ** 

/id You Id,Group Id,Channel Id
/name You name
/picture You Picture
/usrname You Username
/first You Firsname
/last You Lastname
 
🌿 Dev : || @chamod_deshan ||

"""

DEV = """ 
🤞🏿 Developer 🇱🇰

|| @About_Deshan || """

BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_logo_generate_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My Name 📝", callback_data="name"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌿 My Usrname 🌿", callback_data="user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🆘  Help  🆘", callback_data="help"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🤞🏾   Dev   🍀", callback_data="dev"
                    )
                ]
           ]
        )


app = Client(
    'logo Bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
 
@app.on_message(filters.command(["start", "help"]))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/65a7f792ade3adf3cb6cf.jpg",caption=captiont.format(message.from_user.first_name), reply_markup=BUTTON, reply_to_message_id = message.message_id)
   
@app.on_message(filters.forward)
async def fd(client, message):
  text =f" You Id : {message.from_user.id}"
  channel =f" Channel Id : {message.forward_from_chat}"
  photo = get(f"https://single-developers.up.railway.app/logo?name={text}\n{channel}").history[1].url
  await message.reply_chat_action("upload_photo")
  await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.id), reply_to_message_id = message.message_id,
               reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌿 My Username 🌿", callback_data="user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
                    )
                ]
            ]
          )
    )


@app.on_message(filters.command("id"))
async def id(client, message):
  text = message.from_user.id
  photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
  await message.reply_chat_action("upload_photo")
  await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.id), reply_to_message_id = message.message_id,
               reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌿 My Username 🌿", callback_data="user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("name"))
async def name(client, message):
    text = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption2.format(message.from_user.mention), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌿 My Username 🌿", callback_data="user"
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

@app.on_message(filters.command("username"))
async def username(client, message):
    text = message.from_user.username
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption3.format(message.from_user.username), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
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

@app.on_message(filters.command("picture"))
async def picture(client, message):
    file = await client.download_media(message.from_user.photo.big_file_id)
    if not file:
        text = query.from_user.id
        photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
        await app.send_photo(photo=photo,
                     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📝 My Name 📝", callback_data="name"
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
        return
    await app.send_photo(message.chat.id, photo=file, reply_to_message_id = message.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
                    )
                ]
            ]
          )
    )

@app.on_callback_query(filters.regex("pic"))
async def pic(_,query):
    message = query.message
    file = await query.message.download_media(query.from_user.photo.big_file_id)
    await query.message.reply_photo(file,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
                    )
                ]
            ]
          )
    )

@app.on_callback_query(filters.regex("dev"))
async def dev(_,query):
    message = query.message
    await query.answer(f"🤞🏿 My Dev 🇱🇰")
    await query.message.delete()
    await query.message.reply(DEV)

@app.on_callback_query(filters.regex("id"))
async def id(_,query):
    message = query.message
    await query.answer(f"🤞🏿 You Id 🏖")
    await query.message.delete()
    text = query.from_user.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.reply_photo(photo,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="picture"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
                    )
                ]
            ]
          )
    )

@app.on_callback_query(filters.regex("user"))
async def user(_,query):
    message = query.message
    await query.answer(f"🤞🏿 You Username 🏖")
    await query.message.delete()
    text = query.from_user.username
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.reply(photo,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📝 My name 📝", callback_data="name"
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

  
@app.on_callback_query(filters.regex("name"))
async def name(_,query):
    message = query.message
    await query.answer(f"🤞🏿 You Name 🏖")
    await query.message.delete()
    text = query.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.reply(caption2.format(query.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="picture"
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

@app.on_callback_query()
async def button(app, update):
      cb_data = update.data
      if "picture" in cb_data:
        await update.answer(f"🤞🏿 You Picture 🏖")
        await update.message.delete()
        await picture(app, update.message)
      elif "ivd" in cb_data:
        await update.answer(f"🤞🏿 You Id 🏖")
        await update.message.delete()
        await id(app, update.message)
      elif "nagme" in cb_data:
        await update.answer(f"🤞🏿 You name 🏖")
        await update.message.delete()
        await name(app, update.message)

app.run()
