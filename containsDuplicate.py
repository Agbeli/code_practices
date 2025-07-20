### The goal is to check if there are duplicates in the array. #######
from typing import List

class ContainsDuplicate:
	def __init__(self,nums:List[int]):

		"""
		Pass a list of integers
		------------------------
		nums : list of numbers, List[nums]   

		return : boolean
		"""

		self.nums = nums 

	def checkDuplicate(self)->bool:
		
		"""
		return : boolean output 
		"""
		singleNum = set()  ### instantiate hash set to store unique numbers  

		for num in self.nums:

			if num in singleNum:
				return True ### return true when the element is already there. 
			else:
				singleNum.add(num) ### add new element into hash set  
		return False 


if __name__ == '__main__':
	
	##### testcase 1: 
	nums1 = [1,2,3,1]
	constainsElement = ContainsDuplicate(nums=nums1)
	print(f"The {nums1} has duplicate elements: {constainsElement.checkDuplicate()}")

	print("#"*20)
	
	##### testcase 2:
	nums2 = [1,2,3,4]
	constainsElement2 = ContainsDuplicate(nums=nums2)
	print(f"The {nums2} has duplicate elements: {constainsElement2.checkDuplicate()}")

	print("#"*20)

	##### testcase 3: 
	nums3 = [1,1,1,3,3,4,3,2,4,2]
	constainsElement3 = ContainsDuplicate(nums=nums3)
	print(f"The {nums3} has duplicate elements: {constainsElement3.checkDuplicate()}"

)
