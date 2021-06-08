# bot.py
import os
import random
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	match = re.match(r"https://discordapp\.com/channels/(\d+)/(\d+)/(\d+)", message.content)
	if match:
		guild_id, channel_id, message_id = match[1], match[2], match[3]
		ref_channel = await client.fetch_channel(channel_id)
		ref_msg = await ref_channel.fetch_message(message_id)
		msg = "<@!%s> you have been summoned by <@!%s> " % (ref_msg.author.id, message.author.id)
		await message.channel.send(msg)

client.run(TOKEN)