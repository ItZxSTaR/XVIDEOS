import os
import sys
import heroku3
from datetime import datetime
from config import Altron, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from telethon import events


@Altron.on(events.NewMessage(incoming=True, pattern=r"/ping"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"» __ᴀʟᴛʀᴏɴ__", parse_mode=None, link_preview=None)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ! 🖤\n**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{mp}`")


@Altron.on(events.NewMessage(incoming=True, pattern=r"/reboot"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"**ᴇʀʀᴏʀ 131**: ꜱᴇʀᴠᴇʀ ɪꜱ ʀᴇꜱᴛᴀʀᴛɪɴɢ 🥵")
        try:
            await Altron.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USER", None)

@Altron.on(events.NewMessage(incoming=True, pattern=r"/sudo"))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...__")
        mks = "SUDO_USER"
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except Exception:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
        if len(sudousers) > 0:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        heroku_var[mks] = newsudo   
