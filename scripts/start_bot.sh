#!/bin/bash
source /home/ec2-user/chain-bot/venv/bin/activate
python /home/ec2-user/chain-bot/bot.py > /tmp/chain-bot 2>&1 &