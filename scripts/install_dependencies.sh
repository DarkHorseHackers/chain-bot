#!/bin/bash
sudo yum install python3-pip
python3.8 -m venv /home/ec2-user/chain-bot/venv --system-site-packages
chown ec2-user:ec2-user /home/ec2-user/chain-bot/venv
chown ec2-user:ec2-user /home/ec2-user/chain-bot/venv/*
source /home/ec2-user/chain-bot/venv/bin/activate
pip install -r /home/ec2-user/chain-bot/requirements.txt --user