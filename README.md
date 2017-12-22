# Acidus-IRC-Bot
IRC Bot written in Python 2.7

First install Python 2.7 with:

sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
sudo apt-get update
sudo apt-get install python2.7

Next change the hostname of the IRC you will be connecting the bot to, and the channel on the IRC. In line 11 change:

self.host = 'irc.address'

And in line 14 change:

self.chan = '#iffi' #change iffi to whatever the irc channel is

And change the port below to whatever port the IRC is running on:

self.port = 6667 #default

Run the bot with:

python main.py
