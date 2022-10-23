#!/bin/bash
source /home/ec2-user/chain-bot/venv/bin/activate
chmod 777 /tmp/chain-bot
python /home/ec2-user/chain-bot/bot.py > /tmp/chain-bot 2>&1 &