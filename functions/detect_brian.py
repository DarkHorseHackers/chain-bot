import re
from discord import Message

async def detect_brian(message: Message):    
	match = re.match(r"!brian (.*)", message.content.lower())
	if match:
		text = match[1]
		print("detected brian, %s" % text)
		brian_text = "@".join(text.split(" "))
		print("text: ", brian_text)
		await message.channel.send(brian_text)