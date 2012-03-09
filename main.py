# -*- coding: utf-8 -*-

from twisted.internet import reactor
from kagbot.kagbotfactory import KagBotFactory

f = KagBotFactory("#kag2d.ru")

# connect factory to this host and port
reactor.connectTCP("irc.quakenet.org", 6667, f)

# run bot
reactor.run()
