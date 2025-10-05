from typing import List 




def subArray_sum(nums: List,k):
	"""
	 nums: List of elements to sum 
	 k: number of subarray to sum 

	 return:
		maximum value 
	"""
	counter = 0    # initialize the counter  
	sumValues = 0  # sum the values 
	for idx in range(k):
		sumValues+= nums[idx]
	maxValue = sumValues 
	for j in range(k,len(nums)):
		sumValues -= nums[counter] 
		sumValues += nums[j]  # update the sum value 
		counter += 1  # increase the counter 
			
		maxValue = max(sumValues, maxValue) # get the updated maximum value 

	return maxValue


if __name__ == "__main__":
	array1 , k = [1, 2, 3, 4, 5], 3
	print("subArray example 1:")
	print(subArray_sum(nums = array1,k=k))
	
