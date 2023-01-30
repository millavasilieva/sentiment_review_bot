# sentiment_review_bot
An empathic bot that can guess whether you liked a something or not.

## Instructions for launching the bot:

Install Docker if you don't have it installed yet. Installation information can be found here: https://docs.docker.com/engine/install/
Get your token in the telegram bot @BotFather, click on /token and copy.
Now open the config file.py and insert the token there. Then save the file.
In the terminal, go to the folder (directory) with the files and set the commands in turn:
 - docker build. #the point is not superfluous
 - docker images
Copy the ID of the last IMAGE (it should have been created a few seconds ago), and write in the terminal:
docker ru -d -p 80:80 [insert IMAGE ID]
