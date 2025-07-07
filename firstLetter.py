from typing import List 




def firstLetter(s: List):

	"""
	 Input: String 
	 return : letter appear first
	"""
	
	storageString = []
	for letter in s:
		if letter in storageString:
			return letter 
		else:
			storageString.append(letter)

	return None 



if __name__ == "__main__":
	s = "thisssforyyy"
	print(firstLetter(s))



