#######################
#       IRC Bot       #
#     Made by Dan     #
#   http://topkek.pw  #
#######################

import sys, time, socket

class ircProtocol:
    def __init__(self):#Configuration
        self.host = 'irc.essence.network'
        self.port = 6667
        self.nick = 'Acidus'
        self.chan = '#iffi'
        self.real = 'Acidus'
        self.owner = 'username'
        
    def connect(self):#Connect to IRC Socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.send('NICK %s\r\n' % self.nick)
        self.s.send('USER %s %s %s :%s \r\n' % (self.nick, self.nick, self.nick, self.real))
                   
    def recv(self):#Read recieved Packets
        self.data = self.s.recv(2048)
        self.data = self.data.decode('utf-8')
        print self.data
        return self.data

    def pong(self):#Send a pong for auth
        if 'PING' in self.data:
            data = self.data.split(':', 1)
            self.s.send('PONG :%s \r\n' % data[1])
    
    def joinChan(self):#Join Channel
        if ':+iwx' in self.data:
            self.s.send('JOIN :%s \r\n' % self.chan)

    def cmdHandler(self):#Command Handler
        try:
            self.sender = self.data.split(':', 1)[1].split('!', 1)[0]
            data = self.data.split(':', 2)
            self.cmd = data[2]
        except IndexError:
            pass
        #self.s.send('PRIVMSG %s :%s\r\n' % ((self.chan, 'Ayy lmao')))
        
        if self.cmd.startswith('!'):
            try:
                if 'kick' in self.cmd:
                    data = self.data.split(':', 2)
                    self.user = data[2].split(' ')[1]
                    self.s.send('KICK %s %s :%s\r\n' % ((self.chan, self.user, self.nick)))
                    self.s.send('PRIVMSG %s :%s\r\n' % ((self.chan, self.sender + ' has kicked ' + self.user)))
                
                if 'op' in self.cmd:
                    data = self.data.split(':', 2)
                    self.user = data[2].split(' ')[1]
                    self.s.send('MODE %s +o %s\r\n' % ((self.chan, self.user)))
            
                if 'die' in self.cmd:
                    if self.sender != self.owner:
                        self.s.send('PRIVMSG %s :%s\r\n' % ((self.chan, 'Access Denied')))
                    else:
                        quit()
            except Exception as e:
                pass

#Run bot function
if __name__ == '__main__':
    ircBot = ircProtocol()
    ircBot.connect()
    
    while True:
        ircBot.recv()
        ircBot.pong()
        ircBot.joinChan()
        ircBot.cmdHandler()
