#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kagbotexceptions import Error, PlayerAlreadyExistError, LineUpIsFullError

class LineUp(object):
	def __init__ (self, size):
		self.__plist = []
		self.__size = size

	def add (self, player):
		if len(self.__plist) >= self.__size:
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
