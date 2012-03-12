#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError, MixIsAlreadyUp

class Command(object):
	def execute(self):
		raise NotImplementedError()
	
class OnCommand(Command):
	def execute(self, context, channel, nick, args):
		for lineup in context.lineups:
			if lineup.get_on_command() == args[0]:
				try:
					lineup.add(nick)
					context.msg(channel, lineup.get_status())
				except Error as e:
					context.msg(channel, e.msg)
		
			
class AddCommand(Command):
	def execute(self, context, args):
		pass


commands = {}


if __name__ == "__main__":
	print "Commands test"
	a = AddCommand()
	print a.execute("a")