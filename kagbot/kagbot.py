# -*- coding: utf-8 -*-

from twisted.words.protocols import irc
from lineup import LineUp
import sys

class KagBot(irc.IRCClient):

    nickname = "KAGGatherBot"

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        sys.stdout.write("Connections is made\n")
        sys.stdout.flush()

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        sys.stdout.write("Disconnected\n")
        sys.stdout.flush()


    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        self.join(self.factory.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        sys.stdout.write("I have joined!\n")
        sys.stdout.flush()

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]
        # Check to see if they're sending me a private message
        if channel == self.nickname:
            msg = ":>"
            self.msg(user, msg)
            return

        # Otherwise check to see if it is a message directed at me
        if msg == "!on":
            self.lineup = LineUp(6)
            self.msg(channel, "привет")

    def action(self, user, channel, msg):
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]

    # irc callbacks

    def irc_NICK(self, prefix, params):
        """Called when an IRC user changes their nickname."""
        old_nick = prefix.split('!')[0]
        new_nick = params[0]


    # For fun, override the method that determines how a nickname is changed on
    # collisions. The default method appends an underscore.
    def alterCollidedNick(self, nickname):
        """The nick is in use"""
        return nickname + '`'
