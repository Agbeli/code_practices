######### two sum value:  

from typing import List

class TwoSum:

	def twoSum(self,nums:List[int],target:int):

		valueIndex = {} ##### set a hashmap for value --> index 

		for indx, num in enumerate(nums):

			difference = target - num  #### find the difference between the sum values. 

			if difference in valueIndex:   #### check if the difference already exist in the hashmap

				return [valueIndex[difference],indx]
			
            valueIndex[num] = indx  #### store the new value into the hashmap num ---> indx   


if __name__=='__main__':

	###### instantiate the class:  
	twosum = TwoSum()

	#### test case scenario: 

	nums,target = [2,7,11,15],9

	print(f"two value sum of {target} is {twosum.twoSum(nums,target)}")
	print()
	nums2,target2 = [3,3], 6
	print(f"two value sum of {target2} is {twosum.twoSum(nums2,target2)}")

	print()
	nums3,target3 = [3,2,4],6
	print(f"two value sum of {target3} is {twosum.twoSum(nums3,target3)}")

