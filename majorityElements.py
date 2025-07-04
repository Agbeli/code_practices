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



if __name__ == "__main__":
	nums = [ 1,2,2,2,2,3,1,2,2]

	print(majorityElements(nums))

	
