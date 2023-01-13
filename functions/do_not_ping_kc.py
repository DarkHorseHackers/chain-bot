import re
from discord import Message

async def do_not_ping_kc(message: Message):
	match = re.match(r".*@happymasksalesman#9549*", message.content.lower())
		if match:
			author_mention = message.author.mention
			msg = "Don't ping KC " + author_mention + ", k thx bai!"
			await message.send(msg)
			await message.delete()
