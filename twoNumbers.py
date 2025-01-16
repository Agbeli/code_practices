# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        headNode = ListNode(val=0)

        currNode = headNode

        carry = 0
        while (l1 or l2 or carry != 0):

            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            total = v1 + v2 + carry 

            remainder = total % 10 
            currNode.next = ListNode(remainder)
            carry = total // 10 

            # update the pointer 
            currNode = currNode.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

        return headNode.next