# Chain Bot

## What's In The Name?
So named after its first functionality, to detect chains of conversation across channels 🔗

## Deployment
Chain Bot uses CodeDeploy to continuously deploy. A high level overview of the deployment steps:
* A commit is pushed to the Github Repository
* A new CodeDeploy deployment is triggered
* CodeDeploy uses `appspec.yml` to run lifecycle hooks ([doc](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html)), which does the following:
  * Installing dependencies
  * Running the bot
  * Killing the bot when the app stops

tar -xvf Python-3.8.16.tgz
cd Python-3.8.16/
sudo ./configure --enable-optimizations
sudo make install

export DISCORD_TOKEN=MTA1NjQyNjM3NTA2MzU0Nzk1NA.GE2Yxv.FpWlQWLa9eUyyGNVM_44Ylnt2SMEkw62fSj5_c

python3.8 -m venv chain-bot-env --system-site-packages
source chain-bot-env/bin/activate
pip3.8 install -r requirements.txt --user

tail -f /proc/<pid>/fd/1
tail -f /proc/5220/fd/1

deactivate

chmod 777 /tmp/chain-bot
python3.8 bot.py > /dev/null 2> /dev/null < /dev/null &

pkill -9 -f bot.py

## Functionalities
TODO

#### *Made with ♥ for the Dark Horse Discord Community*
