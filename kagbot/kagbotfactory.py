# -*- coding: utf-8 -*-

from twisted.internet import reactor, protocol
from kagbot import KagBot


class KagBotFactory(protocol.ClientFactory):

    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr):
        p = KagBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """Reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()
