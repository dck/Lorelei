# -*- coding: utf-8 -*-

#If you want to add new exception inherit from Error class
#and redefine msg attribute

class Error(Exception):
	pass

class PlayerAlreadyExistError(Error):

	def __init__ (self):
			self.msg = "You are already in lineup"
	
	def __str__ (self):
		return self.msg

class LineUpIsFullError(Error):

	def __init__ (self):
			self.msg = "Lineup is full"
	
	def __str__ (self):
		return self.msg

class MixIsntUp(Error):

	def __init__ (self):
			self.msg = "Mix isn't up. Use !on to create"
	
	def __str__ (self):
		return self.msg

class UserInOtherLineUp(Error):

	def __init__ (self):
			self.msg = "You are in other line up"
	
	def __str__ (self):
		return self.msg

class MixTurnedOff(Error):

	def __init__ (self):
			self.msg = "Mix is turned off"
	
	def __str__ (self):
		return self.msg


if __name__ == "__main__":
	try:
		raise PlayerAlreadyExistError()
	except Error as e:
		print e.msg
