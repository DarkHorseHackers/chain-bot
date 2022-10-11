import discord
import random
import re
from discord import Message, Client

QUESTION_SUBMISSION_LIMIT = 65
bot_sandbox_channel_id = 730163671191519342
question_submission_channel_id = 755811907948118179
question_chat_channel_id = 741321254027526195
general_channel_id = 850886002729418764 # in Bot Testing Server

pinned_rules_message_link = "https://discord.com/channels/726864220838297610/755811907948118179/983562041786789898"

async def detect_violations(message: Message, client: Client):
	if any(role.name == 'Organizer' or role.name == 'Moderator' for role in message.author.roles): # whitelist moderator and organizer roles
		pass
	else:
		print(message.type)
		# rules: [rule lambda, message to send violator, hint]
		contains_hyperlink = [lambda m: re.match(r".*https://.*", m, re.S), "contains hyperlink", ""]
		content_too_long = [lambda m: len(m.split(" ")) > QUESTION_SUBMISSION_LIMIT, "content too long", ""]
		does_not_contain_bold_text = [lambda m: not re.match(r".*\*\*.*\*\*.*", m, re.S), "does not contain bold text", ""]
		does_not_contain_hyperlink = [lambda m: not re.match(r".*https://.*", m, re.S), "does not contain hyperlink", ""]

		# [list of rule, channel id using these rules]
		all_rules = [
			[[contains_hyperlink, content_too_long], question_submission_channel_id],
		]

		did_violate = False
		violations = []
		hints = []
		for rules, rule_channel_id in all_rules:
			if message.channel.id == rule_channel_id:
				for rule_lambda, violation_message, hint in rules:
					if rule_lambda(message.content):
						violations.append(violation_message)
						hints.append(hint)
						did_violate = True
		if did_violate:
			await message.delete()
			bot_noise = random.choice(["*mechanical wail~~*", "Booooop", "Boink", "BeepBeep", "Blarmo!"])
			await message.author.send(
				"%s <@!%s>! Your message in <#%s> was deleted for the following violations:\n\n" % (bot_noise, message.author.id, message.channel.id) + 
				"\n".join(v + "\n" + h for v, h in zip(("**"+v+"**" for v in violations), ("*"+h+"*" if h else "" for h in hints))) +
				"\n\nPlease check the pinned rules: " + pinned_rules_message_link +
				"\n\nPlease resubmit your entry!" +
				"\n\nHere is your original entry:\n\n" +
				"```" + 
				message.content +
				"```" 
			)