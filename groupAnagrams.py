##### import the required libraries needed 
from typing import List
from collections import defaultdict





class GroupAngagram:

	def groupAnagram(self,strs:List[str])->List[List[str]]:

		"""
		strs: list of strings of anagram. 

		return: list of group of anagram of words.

		Time complexity : O(n)

		space complexity  : O(n) 
	
		"""


		storeAnagram = defaultdict(list) #### define hashmap with default list : key ---> value(list)

		for word in strs:

			sortWord = "".join(sorted(word)) #### rearrange the word 

			storeAnagram[sortWord].append(word) ### store the word in the hashmap. 

		return list(storeAnagram.values())
	
	def groupAnagram2(self,strs: List[str])-> List[List[str]]:
		storage = defaultdict(list) 
		for text in strs:
			keys = [0] * 26 
			for l in text:
				keys[ord(l) - ord("a")] += 1 
			storage[tuple(keys)].append(text) 
		return list(storage.values())


	


if __name__ == '__main__':


	#### instantiate the class GroupAnagram
	group = GroupAngagram()

	##### test case scenario:

	strs = ["eat","tea","tan","ate","nat","bat"]

	print(f"Group anagram for {strs} : {group.groupAnagram2(strs)}")

	print()

    #### test case 2

	strs2 = [""]

	print(f"Group anagram for {strs2} : {group.groupAnagram2(strs2)}")

	print()
    
    #### test case 3 :

	strs3 = ["a"]

	print(f"Group anagram for {strs3} : {group.groupAnagram2(strs3)}")


### Diffulty level: Medium by leetcode rating 

