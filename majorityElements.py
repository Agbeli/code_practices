from typing import List 


def majorityElements(nums: List):
	
	"""
         :type nums: List[int]
         :rtype: int

         computation complexity 
         O(n) for time 
         O(n) for space
	  
        """

	dictStorage = {}
	
	for num in nums:
		if num in dictStorage:
			dictStorage[num] += 1 

		else:
			dictStorage[num] = 1

	return max(dictStorage, key = lambda k : dictStorage[k])


def majorityElements2(nums: List):

	"""
         :type nums: List[int]
         :rtype: int

         computation complexity 
         O(n) for time 
         O(1) for space 
        """

	ans, counter = 0, 0 

	for num in nums:
		if counter == 0:
			ans = num 
		counter += 1 if ans == num else -1 ## substract 1 when the current num is different from the next one otherwise add. 
	return ans 





if __name__ == "__main__":
	nums = [ 1,2,2,2,2,3,1,2,2]

	print(majorityElements(nums))

	print("*"*20) 
	print(majorityElements2(nums))




