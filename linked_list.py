class Node:

	def __init__(self,data):
		self.data = data 
		self.next = None 


class LinkedList:

	def __init__(self):
		self.head = None 
	
	def printList(self):
		curr_node = self.head
		while curr_node:
			print("here is the data: ",curr_node.data)
			curr_node = curr_node.next	
	def insertNode(self,node):

		if self.head is None:
			self.head = node
		else:
			lastNode = self.head
			while lastNode.next:
				lastNode = lastNode.next
			lastNode.next = node

	def prepend(self,node):
		if self.head is None:
			self.head = node
			return
		node.next = self.head
		self.head = node 
		
if __name__=='__main__':
	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(100)
	llistnode = LinkedList()
	llistnode.insertNode(node1)
	llistnode.insertNode(node2)
	llistnode.prepend(node3)
	llistnode.printList()
