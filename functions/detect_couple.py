import argparse
import discord
import re
import requests
import shlex
from discord import Message, Client
from .generate_meme import generate_meme

async def detect_couple(message: Message, client: Client):
	match = re.match(r"!couple (.*)", message.content.lower())
	if match:
		try:
			text = match[1]
			print("detected couple, %s" % text)

			parser = argparse.ArgumentParser(description='Process meme arguments.')
			parser.add_argument('--man_profile_id', type=int)
			parser.add_argument('--woman_profile_id', type=int)
			parser.add_argument('--man_text')
			parser.add_argument('--woman_text')
			parser.add_argument('text', nargs='?', default="")
			args, _unknown = parser.parse_known_args(shlex.split(text))
			args = vars(args)
			print("couple args: ", args)
			
			DEFAULT_TEXT0 = "i bet he's thinking about other women"
			CIN_URL = "https://i.ibb.co/P1NGNqz/cin.png"
			man_profile_id = args["man_profile_id"]
			woman_profile_id = args["woman_profile_id"]
			text = args["text"]
			man_text = args["man_text"] if args["man_text"] else text
			woman_text = args["woman_text"] if args["woman_text"] else DEFAULT_TEXT0
		
			if man_profile_id:
				# special cin case
				if man_profile_id == 456226577798135808:
					img_url = CIN_URL
				else:
					profile = await client.fetch_user(man_profile_id)
					img_url = profile.avatar.url.split("?")[0] + "?size=80"
				print(img_url)
				img_data = requests.get(img_url).content

				with open('man-profile.jpg', 'wb') as handler:
					handler.write(img_data)

			if woman_profile_id:
				# special cin case
				if woman_profile_id == 456226577798135808:
					img_url = CIN_URL
				else:
					profile = await client.fetch_user(woman_profile_id)
					img_url = profile.avatar.url.split("?")[0] + "?size=80"
				print(img_url)
				img_data = requests.get(img_url).content

				with open('woman-profile.jpg', 'wb') as handler:
					handler.write(img_data)

			generate_meme(text0=woman_text, text1=man_text, replace_man_profile=True if man_profile_id else False, replace_woman_profile=True if woman_profile_id else False)

			with open('meme.jpg', 'rb') as fp:
				await message.channel.send(file=discord.File(fp, 'meme.jpg'))
		
		except Exception as e:		
			print("Error: ", e)