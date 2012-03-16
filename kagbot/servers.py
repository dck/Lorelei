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
		s = "kag://{ip}:{port:d}/{password}".format(**self.__s)
		return s
	
	def is_avaiable(self):
		return True
		
	def is_free(self):
		return True

	def get_info(self):
		return "[Mock] Some info"

	def get_name(self):
		return self.__s["name"]

if __name__ == "__main__":
	pass