# bot.py
import os
import random
import re
import threading
import asyncio
import time
import sched
from datetime import datetime

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

async def check_permission():
	print("running check_permission")
	await client.wait_until_ready()
	print("ready check_permission")
	while not client.is_closed():
		try:
			guild = await client.fetch_guild("726864220838297610")
			print("guild: %s" % guild)		
			member = await guild.fetch_member("850885659883339786")
			print("member: %s" % member)	
			channels = await guild.fetch_channels()
			for channel in channels:
				if channel.name == "Voice Chat":
					print("channel: %s" % channel)
					permissions = channel.permissions_for(member)
					print("permissions: %s" % permissions, permissions.manage_channels)
				if channel.name == "organizer-chat":
					print("channel: %s" % channel)
					permissions = channel.permissions_for(member)
					print("permissions: %s" % permissions, permissions.manage_channels)
			await asyncio.sleep(60)
		except Exception as e:
			print(e)
			await asyncio.sleep(60)
	print("done check_permission")

client.loop.create_task(check_permission())

client.run(TOKEN)