from typing import List 




def subArray_sum(nums: List,k):
	"""
	 nums: List of elements to sum 
	 k: number of subarray to sum 
	

	 return:
		maximum value 
	""" 
	sumValue = 0 

	for i in range(k):
		sumValue += nums[i]
	maxValue = sumValue
	
	for j in range(k,len(nums)):
		sumValue += nums[j]
		sumValue -= nums[i - k]
		maxValue = max(maxValue, sumValue)
	return maxValue 


if __name__ == "__main__":
	array1 , k = [1, 2, 3, 4, 5], 3
	print("subArray example 1:")
	print(subArray_sum(nums = array1,k=k))
	
