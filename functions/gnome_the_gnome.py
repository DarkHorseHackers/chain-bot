from discord import Message

GNOME_ID = 326183956485767171
GNOME_EMOJI = "<:DH_Gnome:1012067067945566209>"

async def gnome_the_gnome(message: Message):
	if message.author.id == GNOME_ID:
		await message.add_reaction(GNOME_EMOJI)