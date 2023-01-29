from collections import defaultdict
from typing import List




class TopKfrequent:

	def topKfrequent(self,nums:List[int],k:int)->List[int]:

		"""
		nums : input a list of integers 

		k : topmost frequent integer in the list. 

		return : list of topmost integers. 

		"""

		stored = defaultdict(int) #### define a hashmap to store frequency of the digits.  

		for num in nums:
			stored[num] += 1 

		sortFrequency = sorted(stored.items(), key=lambda x: x[1],reverse=True) #### sort the values of the data stored. 

		return [key for key, _ in sortFrequency[:k]]



if __name__ == '__main__':

	#### instantiate the class: ####### 
	topK = TopKfrequent()

	#### testcase: ####### 

	nums, k = [1,1,1,2,2,3], 2

	print(f"top {k} of {nums} is {topK.topKfrequent(nums,k)}")

	print()
	
	#### testcase 2: ######

	nums2,k2 = [1], 1

	print(f"top {k2} of {nums2} is {topK.topKfrequent(nums2,k2)}")


