import discord
import re
from discord import Message, Client

monitoRSS_id = 268478587651358721
darkhorse_podcast_category_id = 833086830521483324

async def detect_new_ep(message: Message, client: Client):
	if message.author.id == monitoRSS_id: # check if MonitoRSS posted a new livestream episode
		match = re.match(r".*Bret and Heather (.*) DarkHorse Podcast Livestream.*(https\:\/\/odysee\.com\/.*)", message.content, re.S)
		print("MATCH: " + match[0])
		if match:
			livestream, livestream_link = match[1], match[2]
			print("LINK: " + livestream_link)
			livestream_number = int("".join(e for e in livestream if e.isnumeric()))
			episode_name = "episode-%s" % livestream_number
			channel = discord.utils.get(client.get_all_channels(), name=episode_name)
			category = await client.fetch_channel(darkhorse_podcast_category_id)
			if not channel:
				# if channel isn't created yet, create new discussion channel, post livestream link, then pin livestream link
				new_channel = await message.guild.create_text_channel(episode_name, category=category)
				print("CREATE CHANNEL: ", new_channel)
				message = await new_channel.send(livestream_link)
				print(message)
				await message.pin(reason="livestream link")