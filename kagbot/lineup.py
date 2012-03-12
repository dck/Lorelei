#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError,
									MixIsAlreadyUp

class LineUp(object):
	def __init__ (self, mode):
		self.__plist = []
		self.__mode = mode
		self.__isRun = False

	def add (self, player):
		if len(self.__plist) >= self.__mode["maxplayers"]:
			raise LineUpIsFullError()
		elif player in self.__plist:
			raise PlayerAlreadyExistError()
		else:
			self.__plist.append(player)
	
	def delete (self, player):
		if player in self.__plist:
			self.__plist.remove(player)
			return True
		else:
			return False
	def get_on_command(self):
		return self.__mode["create"]

	def get_add_command(self):
		return self.__mode["add"]
	
	def is_run(self):
		return self.__isRun
	
	def turn_on(self):
		if not self.__isRun:
			self.__isRun = True
		else:
			raise MixIsAlreadyUp()

	def turn_off(self):
		if self.__isRun:
			self.__isRun = False
			self.__plist = []
			
	def get_status(self):
		str = "[ "
		str += " - ".join(self.__plist)
		str += " - x" * (self.__mode["maxplayers"] - self.__plist)
		str += " ]"
		return str


	def shuffle (self):
		pass

	def get_list (self):
		return self.__plist



if __name__ == "__main__":
    la = LineUp(6)
    try:
    	la.add("Hi")
    	la.add("Hi")
    except Error as e:
    	print e.msg
    print la.get_list()
