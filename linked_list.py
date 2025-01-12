class Node:

	def __init__(self,data):
		self.data = data 
		self.next = None 


class LinkedList:

	def __init__(self):
		self.head = None 
	
	def insertNode(self,node):

		if self.head is None:
			self.head = node
		else:
			lastNode = self.head
			while lastNode:
				lastNode = lastNode.next
			lastNode = node

	
