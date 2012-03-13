#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError, UserInOtherLineUp

class Command(object):
	def execute(self):
		raise NotImplementedError()
	
class OnCommand(Command):
	def execute(self, context, channel, nick, args):
		inMix = filter(lambda x: x.has_player(nick),context.lineups)
		if inMix:
			raise UserInOtherLineUp()
		for lineup in context.lineups:
			if lineup.get_on_command() == args[0]:
				try:
					try:
						number = int(args[1])
					except (ValueError, IndexError):
						number = lineup.get_max() 
					if lineup.create(number):
						lineup.add(nick)
					context.msg(channel, lineup.get_status())
				except Error as e:
					context.msg(channel, nick + ", " + e.msg)
		
			
class AddCommand(Command):
	def execute(self, context, channel, nick, args):
		try:
			nick = args[1]
		except:
			pass
		for lineup in context.lineups:
			if lineup.get_add_command() == args[0]:
				try:
					lineup.add(nick)
					context.msg(channel, lineup.get_status())
				except Error as e:
					context.msg(channel, nick + ", " + e.msg)


class StatusCommand(Command):
		def execute(self, context, channel, nick, args):
			for lineup in context.lineups:
				if lineup.is_run():
					context.msg(channel, lineup.get_status())


class DelCommand(Command):
		def execute(self, context, channel, nick, args):
			try:
				nick = args[1]
			except:
				pass
			for lineup in context.lineups:
				if lineup.is_run():
					if lineup.delete(nick):
						if not lineup.is_run():
							context.msg(channel, "[ Mix is gone ]") #please, rewrite this
						else:
							context.msg(channel, lineup.get_status())
						break


class OffCommand(Command):
	def execute(self, context, channel, nick, args):
		if not context.userIsOpped(nick):
			return
		for lineup in context.lineups:
			if lineup.get_off_command() == args[0]:
				if lineup.is_run():
					lineup.turn_off()
					context.msg(channel, "[ Mix is offed ]")

commands = {}
commands["!status"] = StatusCommand()
commands["!del"] = DelCommand()

if __name__ == "__main__":
	print "Commands test"
	a = AddCommand()
	print a.execute("a")