import random

from AltronX.data import XVIDEOS
from config import Altron
from telethon import events

@Altron.on(events.NewMessage(pattern="/video"))
async def video(event):
    XVIDEO = random.choice(XVIDEOS)
    TEXT = f"**» **"
    await event.client.send_file(event.chat_id, XVIDEO, caption=TEXT)


@Altron.on(events.NewMessage(pattern="/addvideo"))
async def video(event):
    await event.reply("Code bana ra hu vro abhi")
