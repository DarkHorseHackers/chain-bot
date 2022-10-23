#!/bin/bash
sudo yum install python3-pip
python3.8 -m venv /home/ec2-user/chain-bot/venv
source /home/ec2-user/chain-bot/venv
yes | pip3 install -r /home/ec2-user/chain-bot/requirements.txt