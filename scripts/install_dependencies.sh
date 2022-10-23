#!/bin/bash
sudo yum install python3-pip
python3.8 -m venv /home/ec2-user/chain-bot/venv --system-site-packages
source /home/ec2-user/chain-bot/venv
pip install -r /home/ec2-user/chain-bot/requirements.txt --user
pip install -U discord.py --user