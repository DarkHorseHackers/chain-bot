import argparse
import asyncio
import re
from discord import Message

async def detect_chupa(message: Message):
    if message.content.startswith("!chupa"):
        try:
            print("detected chupa in channel %s with message %s" % (message.channel.name, message.content))
            match = re.match(r"!chupa (.*)", message.content.lower())
            if match:
                text = match[1]
                parser = argparse.ArgumentParser(description='Process chupa arguments.')
                parser.add_argument('--time', type=int)
                parser.add_argument('text', nargs=argparse.REMAINDER, default="")
                args = vars(parser.parse_args(text.split(" ")))
                print("chupa args: ", args)
                if args["time"]:
                    await asyncio.sleep(args["time"])
            await message.delete()
        except Exception as e:
            print("Exception: ", e)