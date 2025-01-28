# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import pyrogram
import os
import asyncio

# Environment Variables
app_id = int(os.environ.get("app_id", "22448257"))
api_hash = os.environ.get("api_hash", "7f8e2def57731a61f07b264e13c130a1")
bot_token = os.environ.get("bot_token", "7627086441:AAHJvydOWzyK7mKCpHusxoofoZsqy1295Ss")
custom_caption = os.environ.get(
    "custom_caption",
    "`{file_name}`\n\n**By - @VDoraemon_tamil_links**"
)

# Create Bot Client
AutoCaptionBotV1 = pyrogram.Client(
    name="AutoCaptionBotV1",
    api_id=app_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Start and About Messages
start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is to add me to your channel as admin and I will show you my power</b>
<b>@VJ_Botz</b>"""

about_message = """
<b>• Name : <a href=https://t.me/VJ_Botz>VJ AutoCaption</a></b>
<b>• Developer : <a href=https://t.me/VJ_Botz>[VJ UPDATES]</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/VJ_Botz>Click Here</a></b>
<b>• Source Code : <a href=https://github.com/VJBots/VJ-AutoCaption-Bot>Click Here</a></b>"""

# Start Command Handler
@AutoCaptionBotV1.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
async def start_command(bot, update):
    await update.reply(
        start_message.format(update.from_user.mention),
        reply_markup=await start_buttons(bot),
        parse_mode=pyrogram.enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

# About Callback Handler
@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("about"))
async def about_callback(bot, update):
    bot_data = await bot.get_me()  # Await get_me() for bot details
    await update.message.edit(
        about_message.format(version=pyrogram.__version__, username=bot_data.mention),
        reply_markup=about_buttons(),
        parse_mode=pyrogram.enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

# Start Callback Handler
@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("start"))
async def start_callback(bot, update):
    await update.message.edit(
        start_message.format(update.from_user.mention),
        reply_markup=await start_buttons(bot),
        parse_mode=pyrogram.enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

# Edit Caption for Channel Posts
@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
async def edit_caption(bot, update: pyrogram.types.Message):
    techvj, _ = get_file_details(update)
    if not techvj:
        return  # Exit if no file details are found
    try:
        await update.edit(custom_caption.format(file_name=techvj.file_name))
    except pyrogram.errors.FloodWait as e:
        print(f"FloodWait: Waiting for {e.value} seconds")
        await asyncio.sleep(e.value)
        await update.edit(custom_caption.format(file_name=techvj.file_name))
    except pyrogram.errors.MessageNotModified:
        pass  # Ignore if the message is not modified
    except Exception as e:
        print(f"Unexpected error: {e}")

# Helper Function to Extract File Details
def get_file_details(update: pyrogram.types.Message):
    if update.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(update, message_type, None)
            if obj:
                return obj, obj.file_id
    return None, None

# Generate Start Buttons
async def start_buttons(bot):
    bot_data = await bot.get_me()
    buttons = [[
        pyrogram.types.InlineKeyboardButton("Updates", url="t.me/VJ_Botz"),
        pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
    ], [
        pyrogram.types.InlineKeyboardButton(
            "➕️ Add To Your Channel ➕️",
            url=f"http://t.me/{bot_data.username}?startchannel=true"
        )
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

# Generate About Buttons
def about_buttons():
    buttons = [[
        pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

# Run the Bot
if __name__ == "__main__":
    print("Telegram AutoCaption V1 Bot Starting...")
    print("Bot Created By @VJ_Botz")
    AutoCaptionBotV1.run()

