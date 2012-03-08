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





if __name__ == "__main__":
	try:
		raise PlayerAlreadyExistError()
	except Error as e:
		print e.msg