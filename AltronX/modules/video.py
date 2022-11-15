import random
import os

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from AltronX.data import XVIDEOS
from config import Altron
from telethon import events, Button


VideoURL = ""
telegraph = Telegraph()
r = telegraph.create_account(short_name="Altron")
auth_url = r["auth_url"]


@Altron.on(events.NewMessage(pattern="/video"))
async def video(event):
    XVIDEO = random.choice(XVIDEOS)
    TEXT = f"**» **"
    await event.client.send_file(event.chat_id, XVIDEO, caption=TEXT)


@Altron.on(events.NewMessage(pattern="/addvideo"))
async def addvideo(event):
    EventText = event.text.split(" ")

    global VideoURL
    if (len(EventText) >= 2) and (EventText[1].startswith("https://")):
        VideoURL = EventText[1]

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
        else:
            os.remove(downloaded_file_name)
            VideoURL = f"https://te.legra.ph{media_urls[0]}"

    else:
        await event.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗔𝗱𝗱𝗩𝗶𝗱𝗲𝗼\n  » /addvideo <telegra.ph url>\n  » /addvideo <reply to a Media>")
        return


    TEXT = f"**#ᴠɪᴅᴇᴏ : @ItzExStar**\n\n**ʙʏ ᴜꜱᴇʀ:** [{event.sender.first_name}](tg://user?id={event.sender.id})\n**ᴠɪᴅᴇᴏ ᴜʀʟ:** {VideoURL}"
    await event.client.send_file(-1001881521235,
                "https://te.legra.ph/file/bd33eba4a7d74809df620.mp4",
                caption=TEXT,
                buttons=[
                    [
                    Button.inline("✅ ᴀᴅᴅ ᴠɪᴅᴇᴏ", data="addvideo"),
                    Button.inline("❌ ᴄᴀɴᴄᴇʟ", data="cancel")
                    ],
                ]
                )
    await event.reply(f"» ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴜʀʟ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/TheExVideos)")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@Altron.on(events.CallbackQuery(pattern=r"addvideo"))
async def addvid(event):
    XVIDEOS.append(VideoURL)
    await event.reply(f"» ᴠɪᴅᴇᴏ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!\n\n**ᴠɪᴅᴇᴏ-ᴜʀʟ:** {VideoURL}")

@Altron.on(events.CallbackQuery(pattern=r"cancel"))
async def cancel(event):
    await event.edit(f"» ᴍᴇᴅɪᴀ ᴄᴀɴᴄᴇʟʟᴇᴅ!\n\n**ᴜʀʟ:** {VideoURL}")
