#!/bin/bash
source /home/ec2-user/chain-bot/venv/bin/activate
chmod 777 /tmp/chain-bot.log
PYTHONUNBUFFERED=1 python /home/ec2-user/chain-bot/bot.py > /tmp/chain-bot.log 2>&1 &