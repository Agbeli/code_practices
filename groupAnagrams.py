from typing import List
from collections import defaultdict





class GroupAngagram:

	def groupAnagram(self,strs:List[str])->List[List[str]]:

		"""
		strs: list of strings 

		return: list of group of anagram 
		"""


		storeAnagram = defaultdict(list) #### define hashmap with default list 


		for word in strs:

			sortWord = "".join(sorted(word)) #### rearrange the word 

			storeAnagram[sortWord].append(word) ### store the word in the hashmap. 

		return [l for l in storeAnagram.values()]



if __name__ == '__main__':

	group = GroupAngagram()

	##### test case scenario:

	strs = ["eat","tea","tan","ate","nat","bat"]

	print(f"Group anagram is : {group.groupAnagram(strs)}")