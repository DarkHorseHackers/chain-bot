
import threading
import asyncio
import pytz
from datetime import datetime

def do_background_tasks(client):    
	thread = threading.Thread(target=between_callback, args=(client,))
	thread.start()

async def archive_channel_to_archive(channel_id, archive_id, client):
	old_channel = await client.fetch_channel(channel_id)
	archive_channel = await client.fetch_channel(archive_id)
	print("ARCHIVING CHANNEL: " + old_channel.name)
	await old_channel.edit(category=archive_channel, sync_permissions=True) # requires Manage Channel + Manage Permissions permissions

async def archive_old_podcasts(client):
	# archive old channels in episode discussions category
	category_id = 833086830521483324 # darkhorse podcast category id
	archive_id = 977024766387028008 # podcast archives category
	episode_discussions_channel = await client.fetch_channel(category_id)

	for channel in episode_discussions_channel.channels:
		if channel.name.startswith("episode-") and (datetime.now(pytz.utc)-channel.created_at).days > 13 and not channel.name == "episode-discussions":
			await archive_channel_to_archive(channel.id, archive_id, client)

async def update_channel_names(client):
	current_time = datetime.now(pytz.utc)
	current_day = datetime.today().weekday()
	print("current time is %s, weekday is %s" % (current_time.strftime("%H:%M:%S"), current_day))
	reset_channel_ids_and_names = [
		["833087132414771310", "Lounge One"],
		["732987976317009922", "lounge-one-text"],
		["833087155546620005", "Lounge Two"],
		["804431468662358057", "lounge-two-text"],
		["838114202979532830", "Seminar Room"],
	]
	if current_time.hour == 5: # reset channel names each day at midnight
		for id, name in reset_channel_ids_and_names:
			channel = await client.fetch_channel(id)
			await channel.edit(name=name)
		print("updated lounge channel names at midnight")
	# if current_day == 6 and ((current_time.hour == 19 and current_time.minute >= 30) or (20 <= current_time.hour < 22) or (current_time.hour == 22 and current_time.minute <= 15)): # between 4:30 and 7:15 PST
	# 	await lounge_two_channel.edit(name="Campfire Karaoke")
	# 	print("updated Lounge Two channel name to Campfire Karaoke")

async def check_time(client):
	print("running check_time")
	# await client.wait_until_ready()
	print("ready check_time")
	while not client.is_closed():
		try:
			print("scheduling check_time")

			await update_channel_names(client)

			await archive_old_podcasts(client)

			await asyncio.sleep(60)
		except Exception as e:
			print(e)
			await asyncio.sleep(60)
	print("done check_time")

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(check_time(client))
    loop.close()