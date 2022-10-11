import re
from discord import Message

reference_referrer_pairs = [(755811907948118179, 741321254027526195), (726866762523738202, 743540914336694392)]

async def detect_cross_channel(message: Message):    
	match = re.match(r"https://discord(app)?\.com/channels/(\d+)/(\d+)/(\d+)", message.content)
	if match:
		guild_id, channel_id, message_id = match[2], match[3], match[4]
		if (int(channel_id), message.channel.id) in reference_referrer_pairs:
			print("detected cross channel reference")
			ref_channel = await client.fetch_channel(channel_id)
			ref_msg = await ref_channel.fetch_message(message_id)
			if ref_msg.author.id != message.author.id:
				msg = "<@!%s> you have been summoned by <@!%s> " % (ref_msg.author.id, message.author.id)
				await message.channel.send(msg)