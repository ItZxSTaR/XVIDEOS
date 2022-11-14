import random

from AltronX.data import XVIDEOS
from config import Altron
from telethon import events

@Altron.on(events.NewMessage(pattern="/video"))
async def video(event):
    XVIDEO = random.choice(XVIDEOS)
    TEXT = ""
    await event.client.send_file(event.chat_id, XVIDEO, caption=TEXT)
