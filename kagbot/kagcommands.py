#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Command(object):
	def execute(self):
		raise NotImplementedError()
	
class AddCommand(Command):
	def __init__ (self):
		pass
	def execute(self, context):
		pass


if __name__ == "__main__":
	print "Commands test"
	a = AddCommand()
	print a.execute("a")