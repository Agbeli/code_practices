from typing import List	


def moveZeros(nums:List):

	"""
        nums: List[int]
        return: modify the list in-place.
        """
 	
	lastZeroNum = 0 
	size = len(nums)
	

	for indx in range(0,size):
		if nums[indx] != 0:
			
			temp = nums[lastZeroNum]
			nums[lastZeroNum] = nums[indx]
			lastZeroNum += 1
			nums[indx] = temp 
	return nums	




if __name__ == "__main__":
	## sample input 
	nums = [0,1,3,0,5]
	print(moveZeros(nums))
	print("*" * 20)
	nums2 = [4,0,8,0,0,20]
	print(moveZeros(nums2))
	## weird case example 
	nums3 = [3,4,2,9,0,0,0]
	print(moveZeros(nums3))




