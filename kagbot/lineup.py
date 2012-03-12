#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError, MixIsntUp

class LineUp(object):
	def __init__ (self, settings):
		self.__plist = []
		self.__settings = settings
		self.__isRun = False
		self.__numbers = settings["maxplayers"] * 2

	def create(self, number):
		if number > self.__settings["maxplayers"] or number < 2:
			number = self.__settings["maxplayers"]
		if not self.__isRun:
			self.__isRun = True
			self.__numbers = number * 2
			return True
		else:
			return False

	def add (self, player):
		if not self.__isRun:
			raise MixIsntUp()
		if len(self.__plist) >= self.__numbers:
			raise LineUpIsFullError()
		elif player in self.__plist:
			raise PlayerAlreadyExistError()
		else:
			self.__plist.append(player)
	
	def delete (self, player):
		if player in self.__plist:
			self.__plist.remove(player)
			if not self.__plist:
				self.__isRun = False
			return True
		else:
			return False

	def get_on_command(self):
		return self.__settings["create"]

	def get_add_command(self):
		return self.__settings["add"]
	
	def get_off_command(self):
		return self.__settings["off"]

	def is_run(self):
		return self.__isRun

	def turn_off(self):
		if self.__isRun:
			self.__isRun = False
			self.__plist = []

	def get_status(self):
		s = "[ "
		s += " - ".join(self.__plist)
		s += " - x" * (self.__numbers - len(self.__plist))
		s += " ]"
		return s

	def get_max(self):
		return self.__settings["maxplayers"]

	def shuffle (self):
		pass

	def get_list (self):
		return self.__plist

	def is_empty(self):
		if self.__plist:
			return True
		else:
			return False



if __name__ == "__main__":
    la = LineUp(6)
    try:
    	la.add("Hi")
    	la.add("Hi")
    except Error as e:
    	print e.msg
    print la.get_list()
