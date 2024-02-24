

from pyrogram import __version__
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from bot import Bot
from config import OWNER_ID


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href="<b>○ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟</a>\n○ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/Badhacker98?tab=repositories'>Click here</a>\n○ sᴜᴘᴘᴏʀᴛ : @ll_THE_BAD_BOT_ll\n○ <b>○ ᴏᴡɴᴇʀ: <a href='tg://user?id={OWNER_ID}'>This Person</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("❌ ᴄʟᴏsᴇ ❌", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
