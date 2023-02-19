import re
import discord
from discord import Message, Client
from functions.gnome_the_gnome import GNOME_UP_EMOJI, GNOME_DOWN_EMOJI

DARK_HORSE_DISCORD_GUILD_ID = 726864220838297610
TEST_SERVER_GUILD_ID = 850886002275778612

async def detect_dm(message: Message, client: Client):
    print(message, message.author, client.user)
    if message.author == client.user:
        return
    if not message.guild:
        try:
            if message.content.startswith("!gnome"):                
                match = re.match(r"!gnome (.*)", message.content.lower())
                print("received dm: ", match)
                if match:
                    maybe_message_id = match[1]
                    await spear_emote(client, int(maybe_message_id.strip()))
                    await message.channel.send("gnome success :D")
        except discord.errors.Forbidden:
            await message.channel.send("failed to gnome- is the message in a public channel?")
            print("Forbidden: ", e)
        except Exception as e:
            await message.channel.send("failed to gnome- did you send the correct message id?")
            print("Exception: ", e)

async def spear_emote(client: Client, message_id: int):
    print("spear emote: ", message_id)
    message = await fetch_message_from_guild(client, message_id, DARK_HORSE_DISCORD_GUILD_ID)
    await message.add_reaction(GNOME_UP_EMOJI)
    await message.add_reaction(GNOME_DOWN_EMOJI)

async def fetch_message_from_guild(client: Client, message_id: int, guild_id: int):
    guild = client.get_guild(guild_id)
    channels = await guild.fetch_channels()
    for channel in channels:
        if isinstance(channel, discord.TextChannel):
            try:
                threads = channel.threads
                for thread in threads:
                    try:
                        message = await thread.fetch_message(message_id)
                        return message
                    except:
                        pass
                message = await channel.fetch_message(message_id)
                return message
            except:
                pass
