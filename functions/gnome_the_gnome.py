from discord import Message

GNOME_ID = 326183956485767171
GNOME_UP_EMOJI = "<:DH_GnomeUp:1012067067945566209>"
GNOME_DOWN_EMOJI = "<:DH_GnomeDown:1038145968299835452>"

async def gnome_the_gnome(message: Message):
	if message.author.id == GNOME_ID:
		await message.add_reaction(GNOME_UP_EMOJI)
		await message.add_reaction(GNOME_DOWN_EMOJI)