#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError, UserInOtherLineUp, MixTurnedOff

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
					raise e
		
			
class AddCommand(Command):
	def run_game(self, context, channel, lineup):

		c1 = str(context.config["color1"])
		c2 = str(context.config["color2"])
		lineup.shuffle()
		l = lineup.get_list()
		mid = len(l)/2
		output = "\003{0}[\003 \003{1:d}".format(c1, 4)
		output += " ".join(l[:mid])
		output += "\003 \003{0}] \002vs\002 [\003 \003{1:d}".format(c1, 2)
		output += " ".join(l[mid:])
		output += "\003\003{0} ]".format(c1)
		 
		context.msg(channel, output)
		found = False
		server_map = dict((s.get_name(), s) for s in context.servers)
		for lineup_server in lineup.get_servers():
			try:
				server = server_map[lineup_server]
			except KeyError:
				continue
			else:
				if server.is_free():
					clicker = server.get_clicker()
					found = True
					break
		 		 
		if found:
			output = "\003{0}[\003\003{1} {2} \003\003{0}]\003".format(c1,c2,clicker)
		else:
			output = "\003{0}[\003\003{1} No server found. Wait until server is free \003\003{0}\003".format(c1,c2)
		context.msg(channel, output)


	def execute(self, context, channel, nick, args):
		try:
			nick = args[1]
		except:
			pass
		for lineup in context.lineups:
			if lineup.get_add_command() == args[0]:
				try:
					lineup.add(nick)
					if lineup.is_full():
						self.run_game(context, channel, lineup)
						lineup.turn_off()
					else:
						context.msg(channel, lineup.get_status())
				except Error as e:
					raise e


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
							raise MixTurnedOff()
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
					raise MixTurnedOff()


class ServerInfoCommand(Command):
	def execute(self, context, channel, nick, args):
		for server in context.servers:
			if server.get_trigger() == args[0]:
				if server.is_free():
					context.msg(channel, server.get_info())
				else:
					context.msg(channel, "Server is down")


commands = {}
commands["!status"] = StatusCommand()
commands["!del"] = DelCommand()

if __name__ == "__main__":
	print "Commands test"
	a = AddCommand()
	print a.execute("a")