import os
import asyncio
import discord
from dotenv import load_dotenv
from functions.detect_chupa import detect_chupa

from functions.detect_lab_leak import detect_lab_leak
from functions.detect_cross_channel import detect_cross_channel
from functions.detect_wordcloud import detect_wordcloud
from functions.detect_couple import detect_couple
from functions.detect_brian import detect_brian
from functions.detect_name import detect_name
from functions.detect_violations import detect_violations
from functions.detect_new_ep import detect_new_ep
from functions.do_background_tasks import do_background_tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = discord.Client(intents=intents)

# NOTE: to install discord.py 2.0, use 
# pip install git+https://github.com/Rapptz/discord.py

@client.event
async def on_ready():
	print("bot ready")

@client.event
async def on_message(message):
	print(message.content, message.author)
	if message.author == client.user:
		return

	await detect_violations(message, client)

	await detect_new_ep(message, client)

	await detect_cross_channel(message)
				
	await detect_lab_leak(message)
	
	await detect_wordcloud(message)

	await detect_name(message)
		
	await detect_brian(message)
		
	await detect_chupa(message)

	await detect_couple(message, client)

async def main():
	await client.login(token=TOKEN)

	# do other async things	
	do_background_tasks(client)

    # start the client
	async with client:
		print("starting client")
		await client.start(TOKEN)

asyncio.run(main())