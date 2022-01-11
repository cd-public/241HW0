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

# You may add additional methods or fields, but most have these methods or fields.

class SortableCourse:
	   
	# constructor
	def __init__(self):
		pass
		
	# setting data if appropriate
	def setData(self, name, prefix, num):
		pass
		
	def getData(self):
		pass
	
	def __gt__(self, arg):
		pass
