from typing import List
from collections import defaultdict





class GroupAngagram:

	def groupAnagram(self,strs:List[str])->List[List[str]]:


		storeAnagram = defaultdict(list)


		for word in strs:

			sortWord = "".join(sorted(word))

			storeAnagram[sortWord].append(word)

		return [l for l in storeAnagram.values()]



if __name__ == '__main__':

	group = GroupAngagram()

	##### test case scenario:

	strs = ["eat","tea","tan","ate","nat","bat"]

	print(f"Group anagram is : {group.groupAnagram(strs)}")