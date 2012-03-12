#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Server(object):
	def connect(self):
		raise NotImplementedError()
	
	def disconnect(self):
		raise NotImplementedError()
	
	def is_free(self):
		raise NotImplementedError()

	def get_info(self):
		raise NotImplementedError()



class KagServer(Server):
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