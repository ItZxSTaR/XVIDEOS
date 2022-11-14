import glob
from pathlib import Path
from config import load_plugins, Altron
import logging
import asyncio

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AltronX/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝐀𝐥𝐭𝐫𝐨𝐧 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 😎🤘🏻\nMy Master ---> @𝐈𝐭𝐳𝐄𝐱𝐒𝐭𝐚𝐫")


async def main():
    await Altron.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
