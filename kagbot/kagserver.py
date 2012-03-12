#!/usr/bin/env python
# -*- coding: utf-8 -*-


class KagServer(object):
	def __init__(self, settings):
		self.__s = settings
	
	def connect(self):
		pass

	def disconnect(self):
		pass

	def get_clicker(self):
		s = "kag://" + self.__s["ip"] + ":" + self.__s["port"] + "/" + self.__s["password"]
		return s
	
	def is_free(self):
		return True

	def get_info(self):
		return "Some info"

if __name__ == "__main__":
	pass