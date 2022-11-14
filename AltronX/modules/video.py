import random
import os

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from AltronX.data import XVIDEOS
from config import Altron
from telethon import events


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
    VideoURL = ""

    if len(EventText) >= 2:
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
            VideoURL = media_urls[0]

    else:
        await event.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗔𝗱𝗱𝗩𝗶𝗱𝗲𝗼\n  » /addvideo <telegra.ph url>\n  » /addvideo <reply to a Media>")
        return


    TEXT = f"**#ᴠɪᴅᴇᴏ : @ItzExStar**\n\n**ʙʏ ᴜꜱᴇʀ:** [{event.sender.first_name}](tg://user?id={event.sender.id})\n**ᴠɪᴅᴇᴏ ᴜʀʟ:** {VideoURL}"
    await event.client.send_file(-1001881521235,
                "https://te.legra.ph/file/8cdbbabea5471d5e88f8a.mp4",
                caption=TEXT
                )
    await event.reply(f"» ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴜʀʟ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/TheExVideos)")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
