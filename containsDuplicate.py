### The goal is to check if there are duplicates in the array. 
### return a boolean output. 

from typing import List

class containsDuplicate:
	def __init__(self,nums:List[int]):

		self.nums = nums 

	def checkDuplicate(self)->bool:

		singleNum = set()  ### instantiate hash set to store unique numbers  

		for num in self.nums:

			if num in singleNum:
				return True ### return true when the element is already there. 
			else:
				singleNum.add(num) ### add new element into hash set  
		return False 


if __name__ == '__main__':
	nums1 = [1,2,3,1]
	constainsElement = containsDuplicate(nums=nums1)
	print(f"The {nums1} has duplicate elements: {constainsElement.checkDuplicate()}")
	print()
	nums2 = [1,2,3,4]
	constainsElement2 = containsDuplicate(nums=nums2)
	print(f"The {nums2} has duplicate elements: {constainsElement2.checkDuplicate()}")

	print()
	nums3 = [1,1,1,3,3,4,3,2,4,2]
	constainsElement3 = containsDuplicate(nums=nums3)
	print(f"The {nums3} has duplicate elements: {constainsElement3.checkDuplicate()}")