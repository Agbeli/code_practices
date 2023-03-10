from collections import defaultdict
from typing import List




class TopKfrequent:

	def topKfrequent(self,nums:List[int],k:int)->List[int]:

		"""
        nums : input a list of integers 

		k : topmost frequent integer in the list. 

		return : list of topmost integers. 

		Time Complexity : O(n)

		Space Complexity : O(n)

		"""

		stored = defaultdict(int) #### define a hashmap to store frequency of the digits.  

		for num in nums:
			stored[num] += 1 

		sortFrequency = sorted(stored.items(), key=lambda x: x[1],reverse=True) #### sort the values of the data stored. 

		return [key for key, _ in sortFrequency[:k]]



if __name__ == '__main__':

	#### instantiate the class: ####### 
	topK = TopKfrequent()

	#### testcase 1: ####### 

	nums, k = [1,1,1,2,2,3], 2

	print(f"top {k} of {nums} is {topK.topKfrequent(nums,k)}")

	print()
	
	#### testcase 2: ######

	nums2,k2 = [1] , 1

	print(f"top {k2} of {nums2} is {topK.topKfrequent(nums2,k2)}")

	nums3 , k3 = [9,9,9,9,9,1,1,1,3,4,3,5], 3
	print(f"top {k3} of {nums3} is {topK.topKfrequent(nums3,k3)}")


	nums4 , k4 = [3,4,4,4,5,6,2,4,4,4,3,2,3] , 2

	print(f"top {k4} of {nums4} is {topK.topKfrequent(nums3,k3)}")