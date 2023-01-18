######## solution for two word is anagram: 



class IsAnagram:

	def isAnagram(self,s: str, t: str)->bool:
		"""
		s : string 
		t : string 

		return: boolean 
		"""

		if len(s) == len(t):
			for i in s:
				if s.count(i) != t.count(i):
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