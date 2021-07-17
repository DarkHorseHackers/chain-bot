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
from generate_wordcloud import generate_wordcloud

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print("bot ready")

@client.event
async def on_message(message):
	print(message.content, message.author)
	if message.author == client.user:
		return

	match = re.match(r"https://discord(app)?\.com/channels/(\d+)/(\d+)/(\d+)", message.content)
	if match:
		guild_id, channel_id, message_id = match[2], match[3], match[4]
		print("detected cross channel reference")
		ref_channel = await client.fetch_channel(channel_id)
		ref_msg = await ref_channel.fetch_message(message_id)
		if ref_msg.author.id != message.author.id:
			msg = "<@!%s> you have been summoned by <@!%s> " % (ref_msg.author.id, message.author.id)
			await message.channel.send(msg)

	match = re.match(r".*lab leak theory.*", message.content.lower())
	if match:
		print("detected theory reference")
		msg = "<@!%s> do you mean lab leak hypothesis?" % (message.author.id)
		await message.channel.send(msg)

	if message.content.startswith("!wordcloud"):
		print("generating wordcloud for channel %s" % message.channel.name)
		channel = await client.fetch_channel(message.channel.id)
		await generate_wordcloud_for_channel(channel)

	match = re.match(r"!name (.*)", message.content.lower())
	if match:
		name = match[1]
		print("detected channel name change")
		msg = "changing channel name <#%s> -> %s" % (message.channel.id, name)
		await message.channel.send(msg)
		await message.channel.edit(name=name)
		msg = "channel name changed to %s" % (message.channel.name)
		await message.channel.send(msg)

async def generate_wordcloud_for_channel(channel):	
	messages = []

	async for message in channel.history(limit=200):
		if message.author != client.user:
			messages.append(message.content)

	text = "".join(messages)
	wordcloud = generate_wordcloud(text)
	wordcloud.to_file("wordcloud.jpg")
	with open('wordcloud.jpg', 'rb') as fp:
		await channel.send(file=discord.File(fp, 'wordcloud.jpg'))

@client.event
async def on_raw_message_delete(message):
	print("detected raw message delete")
	print(message)
	if message.cached_message:
		id = message.cached_message.author.id
		user = await client.fetch_user(id)
		await user.send("beep boop: your message in the <#%s> channel was deleted" % message.channel_id)

async def update_channel():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("current time is %s" % current_time)
	channel = await client.fetch_channel("730163671191519342")
	name = "bot-sandbox (%s)" % current_time
	await channel.edit(name=name)
	await channel.send("updated channel name to %s" % name)

async def check_time():
	print("running check_time")
	await client.wait_until_ready()
	print("ready check_time")
	while not client.is_closed:
		print("scheduling check_time")
		s = sched.scheduler(time.perf_counter, time.sleep)
		args = (update_channel(), )
		s.enter(60, 1, client.loop.create_task, args)
		s.run()
	print("done check_time")

def wait():
	print("execute wait")
	asyncio.run_coroutine_threadsafe(check_time(), asyncio.new_event_loop())

client.loop.create_task(check_time())

client.run(TOKEN)