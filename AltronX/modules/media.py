import random
import os

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from AltronX.data import XVIDEOS, XIMAGES
from config import Altron
from telethon import events, Button


MediaURL = ""
telegraph = Telegraph()
r = telegraph.create_account(short_name="Altron")
auth_url = r["auth_url"]


@Altron.on(events.NewMessage(pattern="/video"))
async def video(event):
    XVIDEO = random.choice(XVIDEOS)
    TEXT = f"**» **"
    await event.client.send_file(event.chat_id, XVIDEO, caption=TEXT)

@Altron.on(events.NewMessage(pattern="/image"))
async def video(event):
    XIMAGE = random.choice(XIMAGES)
    TEXT = f"**» **"
    await event.client.send_file(event.chat_id, XIMAGE, caption=TEXT)


@Altron.on(events.NewMessage(pattern="/addmedia"))
async def addvideo(event):
    EventText = event.text.split(" ")

    global MediaURL
    if (len(EventText) >= 2) and (EventText[1].startswith("https://")):
        MediaURL = EventText[1]

    elif event.reply_to_msg_id:
        r_message = await event.get_reply_message()
        downloaded_file_name = await Altron.download_media(r_message, "./")
        x = await event.reply("» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await x.edit("ERROR: " + str(exc))
            os.remove(downloaded_file_name)
            return
        else:
            os.remove(downloaded_file_name)
            MediaURL = f"https://te.legra.ph{media_urls[0]}"

    else:
        await event.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗔𝗱𝗱𝗠𝗲𝗱𝗶𝗮\n  » /addmedia <telegra.ph url>\n  » /addmedia <reply to a Media>")
        return


    TEXT = f"**#ᴍᴇᴅɪᴀ : @ItzExStar**\n\n**ʙʏ ᴜꜱᴇʀ:** [{event.sender.first_name}](tg://user?id={event.sender.id})\n**ᴍᴇᴅɪᴀ ᴜʀʟ:** {MediaURL}"
    await event.client.send_file(-1001881521235,
                "https://te.legra.ph/file/bd33eba4a7d74809df620.mp4",
                caption=TEXT,
                buttons=[
                    [
                    Button.inline("✅ ᴀᴅᴅ ɪᴍᴀɢᴇ", data="addimage"),
                    Button.inline("✅ ᴀᴅᴅ ᴠɪᴅᴇᴏ", data="addvideo")
                    ],
                    [
                        Button.inline("❌ ᴄᴀɴᴄᴇʟ", data="cancel")
                    ],
                ]
                )
    await event.reply(f"» ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴜʀʟ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/TheExVideos)")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@Altron.on(events.CallbackQuery(pattern=r"addvideo"))
async def addvid(event):
    if MediaURL not in XVIDEOS:
        XVIDEOS.append(MediaURL)
    await event.reply(f"» ᴠɪᴅᴇᴏ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!\n\n**ᴠɪᴅᴇᴏ-ᴜʀʟ:** `{MediaURL}`")
    global MediaURL
    MediaURL = ""

@Altron.on(events.CallbackQuery(pattern=r"addimage"))
async def addvid(event):
    if MediaURL not in XIMAGES:
        XIMAGES.append(MediaURL)
    await event.reply(f"» ɪᴍᴀɢᴇ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!\n\n**ɪᴍᴀɢᴇ-ᴜʀʟ:** `{MediaURL}`")
    global MediaURL
    MediaURL = ""

@Altron.on(events.CallbackQuery(pattern=r"cancel"))
async def cancel(event):
    await event.edit(f"» ᴍᴇᴅɪᴀ ᴄᴀɴᴄᴇʟʟᴇᴅ!\n\n**ᴜʀʟ:** {MediaURL}")
