from array import *

def runRecursive(array):
	
	return runRecursiveHelper(array, 0)


def runRecursiveHelper(array, index):
	# base case
	if not array:
		return []
	elif (len(array) == 1):
		return sorted(array[0])
	
	elif (len(array) == 2):
		return sorted(array[0])
	
	# normal case
	elif (index < len(array)-2):
		newArray = sorted(array[index])
		index += 1
		'''
		#finalArray = newArray + runRecursiveHelper(array, index)
		#print "Final Array: " 
		print finalArray
		return finalArray
		'''
		return newArray + runRecursiveHelper(array, index)
		
	else: 
		return run
		
             
	
def runIterative():
	array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
	print array
	newArray = []
	
	for row in array:
		if not row:
			pass
		temp = sorted(row)
		newArray += temp
		print newArray
		
def main():

	runIterative()
	
	'''
	array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
	print array
	print "Array[0]"
	print array[0]
	print "Array[1]"
	print array[1]
	print "Array[2]"
	print array[2]
	print "Array[3]"
	print array[3]
	print ""			

	tempArray = []
	print "Array[0] sorted"
	tempArray = sorted(array[0])
	print tempArray
	print "Array[1] sorted"
	tempArray = sorted(array[1])
	print tempArray
	print "Array[2] sorted"
	tempArray = sorted(array[2])
	print tempArray
	print "Array[3] sorted"
	tempArray = sorted(array[3])
	print tempArray
	print ""
	
	tempArray = sorted(array[0]) + sorted(array[1]) + sorted(array[2]) + sorted(array[3])
	print tempArray
	
	
	#runRecursive(array)
	'''
	
if __name__ == "__main__":
	main()
