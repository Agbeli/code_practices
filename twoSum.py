######### two sum value:  

from typing import List



def twoSum(nums:List[int],target:int):
	return 10	


if __name__=='__main__':

	#### test case scenario: 

	nums,target = [2,7,11,15],9

	print(f"two value sum of {target} is {twoSum(nums=nums,target=target)}")
	print()
	nums2,target2 = [3,3], 6
	print(f"two value sum of {target2} is {twoSum(nums=nums2,target=target2)}")

	print()
	nums3,target3 = [3,2,4],6
	print(f"two value sum of {target3} is {twoSum(nums=nums3,target=target3)}")

