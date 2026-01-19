# use the set to define subarray 




def longestSubarray(s:str):
	''' hashset to find longest subarray
	    input: str
	    return : int 
	'''
	longest = 0 
	left = 0 
	store = set()
	for right in range(len(s)):
		while s[right] in store:
			store.remove(s[left])
			left += 1 
		store.add(s[right])
		update = right - left + 1 
		longest = max(longest,update)
	return longest   




if __name__ == "__main__":
	str1 = "aaabababacv"
	print("This is longest subarray:  ",str1 ," |---> ",longestSubarray(s=str1))
