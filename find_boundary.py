


def find_boundary(input):
	'''
	The use of binary search to find the first true
	'''
	left , right = 0 , len(input) - 1
	boundary_index = -1  
	while left < right: 
		mid = (left + right)//2 
		if input[mid]:
			boundary_index = mid 
			right = mid - 1 
		else:
			left = mid + 1 
	return boundary_index 


if __name__ == "__main__":
	boolean_values = [False, False,False, True, True, True]
	print(find_boundary(boolean_values))
			 
