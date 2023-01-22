from collections import defaultdict
from typing import List




class TopKfrequent:

	def topKfrequent(self,nums:List[int],k:int):

		stored = defaultdict(int)


		for num in nums:
			stored[num] += 1 

		sortFrequency = sorted(stored.items(), key=lambda x: x[1],reverse=True)

		return [key for key, _ in sortFrequency[:k]]



if __name__ == '__main__':


	topK = TopKfrequent()

	#### testcase: 

	nums, k = [1,1,1,2,2,3], 2

	print(f"top {k} of {nums} is {topK.topKfrequent(nums,k)}")


