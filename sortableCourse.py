# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a data field or fields, that contains the sortable data
# NEW: A course contains a 
#   * Course name (a string)
#   * Course prefix (a string)
#   * Course number
# Public
# - a getData method that takes no inputs returns the data
# NEW: This will return a list of three outputs, [<name>, <prefix>, <number>]
# - a setData method that updates the data given inputs and returns nothing
# NEW: This will now take three inputs, two strings (name and prefix) and a number
# Special
# - a __gt__ (greaterThan) method given another sortable s, returns true if data is greater than s.data
# NEW: Courses are sorted by:
#   * Course prefix (a string), unless course prefixs are the same, then
#   * Course number
# - a constructor __init__ that initializes with a default value (Two empty strings "" and 0)

class SortableCourse:
	   
	# constructor
	def __init__(self):
		self.__name = ""
		self.__prefix = ""
		self.__num = 0
		
	# setting data if appropriate
	def setData(self, name, prefix, num):
		self.__name = name
		self.__prefix = prefix
		self.__num = num
		return
		
	def getData(self):
		return [self.__name, self.__prefix, self.__num]
	
	def __gt__(self, arg):
		fields = arg.getData()
		if self.__prefix == fields[1]: # deal with same prefix
			return self.__num > fields[2]
		return self.__prefix > fields[1] # alphabetical is backwards