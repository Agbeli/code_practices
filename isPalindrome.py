

## define the function to check for palindrome 

def isPalindrome(s:str):
	left_index , right_index = 0, len(s) - 1
	
	while left_index < right_index:
		
		while left_index < right_index and not s[left_index].isalnum():
			left_index += 1 
		while left_index < right_index and not s[right_index].isalnum():
			right_index -= 1
		if s[left_index] != s[right_index]:
			return False 

		left_index += 1
		right_index -= 1 

	return True 



if __name__ == "__main__":
	str1 = "EmmE"
	print(isPalindrome(str1)) 

	print("#" * 30)

	
