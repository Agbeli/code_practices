from typing import List 






class ProductExceptSelf:
	def _productExceptSelf(self,nums:List[int])->List[int]:

		"""
		nums: list of integer 

		return: product of integer except the given index. 
		
		"""

		product = [1] * len(nums) #### initialize the indices with 1 

		preproduct = 1  ### prefix the product with 1 

		postproduct = 1  ### postfix the product with 1 

		
		for i in range(len(nums)):

			product[i] = preproduct

			preproduct *= nums[i]

		for i in range(len(nums)-1,-1,-1):

			product[i] *= postproduct ### update the product 

			postproduct *= nums[i]

		return product




if __name__ == '__main__':


	#### instantiate the prodExceptSelf 
	prodExceptSelf = ProductExceptSelf()

	##### test case 

	nums = [1,2,3,4]

	print(f"product Except Self of {nums} is {prodExceptSelf._productExceptSelf(nums)}")

	print()

	nums2 = [-1,1,0,-3,3]

	print(f"product Except Self of {nums2} is {prodExceptSelf._productExceptSelf(nums2)}")

	print()

	nums3 = [-1,2,0,1,1,2]

	print(f"product Except Self of {nums3} is {prodExceptSelf._productExceptSelf(nums3)}")

