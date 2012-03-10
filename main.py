#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from kagbot.kagbotfactory import KagBotFactory
from botconfig import config as c

server = c["servername"]
port = c["serverport"]

f = KagBotFactory(c)

# connect factory to this host and port
reactor.connectTCP(server, port, f)

# run bot
reactor.run()
