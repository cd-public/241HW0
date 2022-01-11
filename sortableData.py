# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a data field or fields, that contains the sortable data
# Public
# - a getData method that takes no inputs returns the data
# - a setData method that updates the data given inputs and returns nothing
# Special
# - a __gt__ (greaterThan) method given another sortable s, returns true if data is greater than s.data
# - a constructor __init__ that initializes the object with a default value (0)

class SortableData:
	
	# constructor
	def __init__(self):
		self.__data = 0 # default value
		
	# setting data if appropriate
	def setData(self,arg):
		self.__data = arg
		
	def getData(self):
		return self.__data
	
	def __gt__(self, arg):
		return self.__data > arg.getData()