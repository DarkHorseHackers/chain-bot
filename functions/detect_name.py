import re
from discord import Message

async def detect_name(message: Message):    
	match = re.match(r"!name (.*)", message.content.lower())
	if match:
		name = match[1]
		print("detected channel name change")
		msg = "changing channel name <#%s> -> %s" % (message.channel.id, name)
		await message.channel.send(msg)
		await message.channel.edit(name=name)
		msg = "channel name changed to %s" % (message.channel.name)
		await message.channel.send(msg)