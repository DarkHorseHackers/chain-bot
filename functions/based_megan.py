from discord import Message

LATE_NIGHT_PUB_ID = 750780587920457819
MEGAN_ID = 744702028046925834
BASED_EMOJI = "<:DH_Based:1062783035029864570>"

async def based_megan(message: Message):
	if message.author.id == MEGAN_ID:
	    await message.add_reaction(BASED_EMOJI)
#		if message.channel.id == LATE_NIGHT_PUB_ID:
