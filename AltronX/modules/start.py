import telethon
from telethon import events, Button
from config import Altron


CmdMsg = f"""
**» ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗧𝗼 𝗚𝗲𝘁 𝗠𝗲𝗱𝗶𝗮:
   ➲ /image : ᴛᴏ ɢᴇᴛ ꜱᴇxʏ ɢɪʀʟꜱ ɪᴍᴀɢᴇ
   ➲ /video : ᴛᴏ ɢᴇᴛ ꜱᴇxʏ ɢɪʀʟꜱ ᴠɪᴅᴇᴏ

𝗧𝗼 𝗔𝗱𝗱 𝗠𝗲𝗱𝗶𝗮:
   ➲ /addimage : ᴛᴏ ᴀᴅᴅ ꜱᴇxʏ ɪᴍᴀɢᴇ ɪɴ ᴛʜɪꜱ ʙᴏᴛ
   ➲ /addvideo : ᴛᴏ ᴀᴅᴅ ꜱᴇxʏ ᴠɪᴅᴇᴏ ɪɴ ᴛʜɪꜱ ʙᴏᴛ


**© @ItzExStar**
"""

PythonButton = [
        [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="alt_cmd")
        ],
        [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/Altron_X"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/TheAltron")
        ],
        ]


@Altron.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐏ʏᴛʜᴏɴ](https://t.me/ItzExStar)**\n"
        TEXT += f"» **ᴄᴏɴᴛᴇɴᴛ ᴘʀᴏᴠɪᴅᴇʀ​ : [𝐒ʜᴀᴜʀʏᴀ](https://t.me/YwR_CrUsH_SHaUrYa_xD)**\n"
        TEXT += f"» **ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `X1.0`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://te.legra.ph/file/07d39b85c6cea32f15259.jpg",
                caption=TEXT, 
                buttons=PythonButton)


@Altron.on(events.CallbackQuery(pattern=r"help_back"))
async def alt_cmd(event):
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐏ʏᴛʜᴏɴ](https://t.me/ItzExStar)**\n"
        TEXT += f"» **ᴄᴏɴᴛᴇɴᴛ ᴘʀᴏᴠɪᴅᴇʀ​ : [𝐒ʜᴀᴜʀʏᴀ](https://t.me/YwR_CrUsH_SHaUrYa_xD)**\n"
        TEXT += f"» **ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `X1.0`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.edit(TEXT, buttons=PythonButton)

@Altron.on(events.CallbackQuery(pattern=r"alt_cmd"))
async def back(event):
        await event.edit(CmdMsg,
                buttons=[[Button.inline("< Back", data="help_back"),],],
                )
