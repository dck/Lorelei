#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LineUp:
	def __init__ (self, size):
		self.__plist = []
		self.__size = size

	def add (self, player):
		if player in self.__plist:
			return False
		else:
			self.__plist.append(player)
	
	def delete (self, player):
		pass
	
	def shuffle (self, isBalance=False):
		pass
	def get_list (self):
		return self.__plist


if __name__ == "__main__":
    la = LineUp(6)
    la.add("Hi")
    la.add("Hi")
    print la.get_list()