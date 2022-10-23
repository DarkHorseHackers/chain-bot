#!/bin/bash
source /home/ec2-user/chain-bot/venv/bin/activate
python -m pip show requests
python -m pip show discord.py
python /home/ec2-user/chain-bot/bot.py