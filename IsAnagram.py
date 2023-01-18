######## solution for two word is anagram: 



class IsAnagram:

	def isAnagram(self,s: str, t: str)->bool:
		"""
		s : string 
		t : string 

		return: boolean 
		"""

		if len(s) == len(t):   ##### check if the number of letters in each word are the same 
			for i in s: #### iterate through the reference word. 
				if s.count(i) != t.count(i): #### check if the number of letter is different from the other 
					return False 

			return True 
		return False 


if __name__ == '__main__':
	anagram = IsAnagram()

	s, t = "anagram", "nagaram"

	print(f"Are these two words: {s} and {t} anagram: {anagram.isAnagram(s,t)}")

	print()

	s2,t2 = "rat", "car"

	print(f"Are these two words: {s2} and {t2} anagram: {anagram.isAnagram(s2,t2)}")