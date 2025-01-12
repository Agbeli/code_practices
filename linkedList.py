

class Node:
    
    def __init__(self,data=None):
        
        self.data = data 
        self.next_node = None





class LinkedList:
    
    def __init__(self,head=None):
        
        self.head = head
        
        
    def is_empty(self):
        
        return self.head == None
    
    def size(self):
        
        current = self.head
        count = 0 #

        while current:
            count += 1
            current = current.next_node 
            
        return count  