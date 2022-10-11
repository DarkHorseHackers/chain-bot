import argparse
import re
import shlex
import discord
from discord import Message
from .generate_wordcloud import generate_wordcloud

async def detect_wordcloud(message: Message):
	if message.content.startswith("!wordcloud"):
		try:
			channel = message.channel
			print("generating wordcloud for channel %s" % message.channel.name)
			match = re.match(r"!wordcloud (.*)", message.content.lower())
			if match:
				text = match[1]
				parser = argparse.ArgumentParser(description='Process wordcloud arguments.')
				parser.add_argument('--limit', type=int)
				args = vars(parser.parse_args(shlex.split(text)))
				print("wordcloud args: ", args)
				await generate_wordcloud_for_channel(channel, args["limit"])
			else:
				await generate_wordcloud_for_channel(channel)
		except Exception as e:
			print("Exception: ", e)

async def generate_wordcloud_for_channel(channel, limit: int = 200):	
	messages = []

	async for message in channel.history(limit=limit):
		if not message.author.bot:
			messages.append(message.content)

	text = "".join(messages)
	wordcloud = generate_wordcloud(text)
	wordcloud.to_file("wordcloud.jpg")
	with open('wordcloud.jpg', 'rb') as fp:
		await channel.send(file=discord.File(fp, 'wordcloud.jpg'))