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

print("\nšš„š­š«šØš§ šš©šš¦ ššØš­š¬ ššš©š„šØš²šš šš®šššš¬š¬šš®š„š„š² šš¤š»\nMy Master ---> @šš­š³šš±šš­šš«")


async def main():
    await Altron.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
