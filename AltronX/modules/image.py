import random
import os

from telethon import events, Button
from telegraph import Telegraph

from AltronX.data import XIMAGES
from config import Altron
from AltronX.modules.video import resize_image, cancel


ImageURL = ""
telegraph = Telegraph()
r = telegraph.create_account(short_name="Altron")
auth_url = r["auth_url"]


@Altron.on(events.NewMessage(pattern="/image"))
async def image(event):
    XIMAGE = random.choice(XIMAGES)
    TEXT = f"**» **"
    await event.client.send_file(event.chat_id, XIMAGE, caption=TEXT)


@Altron.on(events.NewMessage(pattern="/addimage"))
async def addvideo(event):
    EventText = event.text.split(" ")

    global ImageURL
    if (len(EventText) >= 2) and (EventText[1].startswith("https://")):
        ImageURL = EventText[1]

    elif event.reply_to_msg_id:
        XMsg = await event.get_reply_message()
        user_object = await Altron.get_entity(XMsg.sender_id)
        title_of_page = user_object.first_name
        optional_title = event.pattern_match.group(2)

        if optional_title:
            title_of_page = optional_title
        page_content = XMsg.message
        if XMsg.media:
            if page_content != "":
                title_of_page = page_content
            downloaded_file_name = await Altron.download_media(XMsg, "./")
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            for m in m_list:
                page_content += m.decode("UTF-8") + "\n"
            os.remove(downloaded_file_name)
        page_content = page_content.replace("\n", "<br>")
        response = telegraph.create_page(title_of_page, html_content=page_content)
        ImageURL = "https://telegra.ph/{}".format(response["path"])

    else:
        await event.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗔𝗱𝗱-𝗜𝗺𝗮𝗴𝗲\n  » /addimage <telegra.ph url>\n  » /addimage <reply to a Media>")
        return


    TEXT = f"**#ɪᴍᴀɢᴇ : @ItzExStar**\n\n**ʙʏ ᴜꜱᴇʀ:** [{event.sender.first_name}](tg://user?id={event.sender.id})\n**ɪᴍᴀɢᴇ ᴜʀʟ:** {ImageURL}"
    await event.client.send_file(-1001881521235,
                "https://te.legra.ph/file/bd33eba4a7d74809df620.mp4",
                caption=TEXT,
                buttons=[
                    [
                    Button.inline("✅ ᴀᴅᴅ ɪᴍᴀɢᴇ", data="addimage"),
                    Button.inline("❌ ᴄᴀɴᴄᴇʟ", data="cancel")
                    ],
                ]
                )
    await event.reply(f"» ʏᴏᴜʀ ɪᴍᴀɢᴇ ᴜʀʟ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/TheExVideos)")

@Altron.on(events.CallbackQuery(pattern=r"addimage"))
async def addimg(event):
    XIMAGES.append(ImageURL)
    await event.reply(f"» ɪᴍᴀɢᴇ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!\n\n**ɪᴍᴀɢᴇ-ᴜʀʟ:** {ImageURL}")
