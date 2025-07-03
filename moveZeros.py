from typing import List	


def moveZeros(nums:List):

	"""
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
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
	nums = [0,1,3,0,5]
	print(moveZeros(nums))
	print("*" * 20)
	nums2 = [4,0,8,0,0,20]
	print(moveZeros(nums2))




