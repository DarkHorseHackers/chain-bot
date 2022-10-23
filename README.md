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

## Functionalities
TODO

#### *Made with ♥ for the Dark Horse Discord Community*