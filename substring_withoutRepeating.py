from collections import defaultdict





def longest_substringWithoutRepeating(s:str):

	''' 
	Finding the longest substrings  without repeating character.
	'''
	left = 0

	longest = 0 
	counter : dict[str,int] = defaultdict(int)
	for right in range(len(s)):
		counter[s[right]] += 1 
		while counter[s[right]] > 1:
			counter[s[left]] -= 1 
			left += 1 
		longest = max(longest, right - left + 1) 
	return longest



if __name__ == "__main__":
	s = "cabcdeesefad"
	print(longest_substringWithoutRepeating(s))
	
