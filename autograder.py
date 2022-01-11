# Autograder

# This will attempt to perform intended tasks for Sortable, SortableNat, and SortableSet
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: SORTABLEDATA ---\n") # This should all be correct from the provided code
from sortableData import SortableData
s1 = SortableData()
s2 = SortableData()

print("AUTOGRADER: SortableData Set/Get Testing: 15 pts\n")
points = singleTest("Checking Default Data Value", 0, s1.getData(), points)
s2.setData('word')
points = singleTest("Checking Data Value After Setting Value to Some String (\'word\')", "word", s2.getData(), points)
s2.setData(1)
points = singleTest("Checking Data Value After Setting Value to Integer (1)", 1, s2.getData(), points)

print("AUTOGRADER: Sortable Comparison Testing: 15 pts\n")
points = singleTest("Checking SortableData(1) > SortableData(0)", True, s2 > s1, points)
points = singleTest("Checking SortableData(0) > SortableData(1)", False, s1 > s2, points)
s2.setData(0)
points = singleTest("Checking SortableData(0) > SortableData(0)", False, s1 > s2, points)

print("\n --- AUTOGRADER: SORTABLECOURSE ---\n")
from sortableCourse import SortableCourse
cs2 = SortableCourse()
cs1 = SortableCourse()
math = SortableCourse()
sys = SortableCourse()

print("AUTOGRADER: SortableCourse Constructor Testing: 05 pts\n")
points = singleTest("Checking SortableCourse Default Data Value", ["","",0], cs2.getData(), points)

print("AUTOGRADER: SortableCourse Set/Get Testing: 15 pts\n")
cs2.setData("Structures", "CS", 241)
points = singleTest("Checking Name is \"Structures\" After Setting to [\"Structures\", \"CS\", 241]", "Structures", cs2.getData()[0], points)
points = singleTest("Checking Prefix is \"CS\"", "CS", cs2.getData()[1], points)
points = singleTest("Checking Number is 241", 241, cs2.getData()[2], points)

print("AUTOGRADER: SortableCourse Comparison Testing: 50 pts\n")
cs1.setData("Programming", "CS", 151)
math.setData("Foundations", "Math", 251)
sys.setData("Systems", "CS", 399)
points = singleTest("Checking if CS 241 is before (less than) Math 251 (CS alphabetically first)", True, cs2 < math, points)
points = singleTest("Checking if Math 251 is before CS 241 (CS alphabetically first)", False, math < cs2, points)
points = singleTest("Checking if CS 399 is before (less than) Math 251 (CS alphabetically first)", True, sys < math, points)
points = singleTest("Checking if Math 251 is before CS 399 (CS alphabetically first)", False, math < sys, points)
points = singleTest("Checking if CS 151 is before (less than) CS 241 (151 is less than 241)", True, cs1 < cs2, points)
points = singleTest("Checking if CS 241 is before (less than) CS 151 (151 is less than 241)", False, cs2 < cs1, points)
points = singleTest("Checking if CS 399 is before (less than) CS 241 (241 is less than 399)", False, sys < cs2, points)
points = singleTest("Checking if CS 241 is before (less than) CS 399 (241 is less than 399)", True, cs2 < sys, points)
points = singleTest("Checking if CS 241 is greater than Math 251 (CS alphabetically first)", False, cs2 > math, points)
points = singleTest("Checking if CS 241 is greater than CS 151 (241 is greater than 151)", True, cs2 > cs1, points)