# -*- coding: utf-8 -*-

from twisted.internet import reactor, protocol
from kagbot import KagBot


class KagBotFactory(protocol.ClientFactory):

    def __init__(self, config):
        self.config = config

    def buildProtocol(self, addr):
        p = KagBot(self.config)
        return p

    def clientConnectionLost(self, connector, reason):
        """Reconnect to server."""
        print "Connection lost: %s. Trying to reconnect\n" % reason
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed: %s\n" % reason
        reactor.stop()
