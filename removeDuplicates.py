from typing import List 



def removeDuplicates(nums:List):

	"""
	 nums: list of duplicates 
	 return: Unique element in the list
	"""
	
	if len(nums) == 0:
		return 0 
	
	l = 1 
	n = len(nums)
	for j in range(1,n):
		if nums[j] != nums[j-1]:
			nums[l] = nums[j]
			l += 1
	return l 



if __name__ == "__main__":
	nums = [0,0,1,1,1,2,2,3,3,4]
	print(removeDuplicates(nums))



 
