from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡 ✪
 
 Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
 
 Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
 
Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
 
Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
 
Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
 
 Rᴇᴘᴏ ʟᴇɢᴀ Lᴀɴᴅ ʟᴇʟᴇ 🤡
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Harshu_Raven"),
             InlineKeyboardButton(" Network", url="https://t.me/RavenxNetwork"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Raven_Legion"),          
             InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://t.me/Raven_Legion"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://vault.pictures/p/ed5f2c41bf024abdb83201a26d776da1",
        caption=start_txt,
        reply_markup=reply_markup
    )
