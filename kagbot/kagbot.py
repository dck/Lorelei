# -*- coding: utf-8 -*-

from twisted.words.protocols import irc
from lineup import LineUp
from kagcommands import *
from kagbotexceptions import Error
import sys

class KagBot(irc.IRCClient):

    def __init__(self, config):
        self.config = config
        self.nickname = self.config["nickname"]
        self.username = self.config["username"]
        self.realname = self.config["realname"]
        self.serverpass = self.config["serverpass"]
        self.users = {}
        self.lineups = []
        for mode in self.config["modes"]:
            self.lineups.append(LineUp(mode))
            commands[mode["create"]] = OnCommand()
            commands[mode["add"]] = AddCommand()
            commands[mode["off"]] = OffCommand()

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        sys.stdout.write("I am successfully connected to %s:%d\n" % 
                            (self.config["servername"], self.config["serverport"]))
        sys.stdout.flush()

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        sys.stdout.write("Disconnected from server\n")
        sys.stdout.flush()


    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        for chan in self.config["channels"]:
            self.join(chan)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        sys.stdout.write("I have joined to %s\n" % channel)
        sys.stdout.flush()

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]
        words = msg.split()

        if channel == self.nickname:
            self.__handlePrivMsg(user, words)
        else:
            self.__handleChanMsg(channel, user, words)

    def action(self, user, channel, msg):
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]

    # irc callbacks

    def irc_NICK(self, prefix, params):
        """Called when an IRC user changes their nickname."""
        old_nick = prefix.split('!')[0]
        new_nick = params[0]

    def alterCollidedNick(self, nickname):
        """The nick is in use"""
        return "|" + self.nickname + '|'

    def userIsVoiced(self, nick):
        #TODO: implement this
        return True
    
    def userIsOpped(self, nick):
        #TODO: implements this shit
        return True
    
    def userIsAuthed(self, nick):
        #TODO: implement this
        return True
    
    def __handlePrivMsg(self, nick, args):
        pass

    def __handleChanMsg(self, channel, nick, args):
        try:
            cmd = commands[args[0]]
            cmd.execute(self, channel, nick, args)
        except KeyError:
            pass
        except Error as e:
            self.msg(channel, nick + ", " + e.msg)