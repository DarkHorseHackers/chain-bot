#!/bin/bash
source /home/ec2-user/chain-bot/venv/bin/activate
python /home/ec2-user/chain-bot/bot.py > /dev/null 2> /dev/null < /dev/null &