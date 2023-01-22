from collections import defaultdict
from typing import List




class TopKfrequent:

	def topKfrequent(self,nums:List[int],k:int)->List[int]:

		stored = defaultdict(int)

		for num in nums:
			stored[num] += 1 

		sortFrequency = sorted(stored.items(), key=lambda x: x[1],reverse=True)

		return [key for key, _ in sortFrequency[:k]]



if __name__ == '__main__':

	#### instantiate the class:  
	topK = TopKfrequent()

	#### testcase: 

	nums, k = [1,1,1,2,2,3], 2

	print(f"top {k} of {nums} is {topK.topKfrequent(nums,k)}")

	print()
	
	#### testcase 2:
	nums2,k2 = [1], 1

	print(f"top {k2} of {nums2} is {topK.topKfrequent(nums2,k2)}")


