from irc import *
import os
import random
import irc
 
channel = "#testit"
server = "irc.freenode.net"
nickname = "reddity"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
 
while 1:
    text = irc.get_text()
    print(text)
 
    if "PRIVMSG".encode('utf-8') in text and channel in text and "hello".encode('utf-8') in text:
        irc.send(channel, "Hello!")
