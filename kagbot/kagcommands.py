#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError

class Command(object):
	def execute(self):
		raise NotImplementedError()
	
class AddCommand(Command):
	def execute(self, context, *args):
		pass


if __name__ == "__main__":
	print "Commands test"
	a = AddCommand()
	print a.execute("a")