import re
from discord import Message

async def detect_twitter(message: Message):    
	notmatch = re.match(r".*fxtwitter.com.*", message.content.lower())
	if !notmatch:
    match = re.match(r".*twitter.com.*", message.content.lower())
		if match:
      message.edit(content = message.content.replace("twitter", "fxtwitter"))
      
      
