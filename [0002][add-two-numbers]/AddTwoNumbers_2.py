# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # use and to check whether the node pointer is none, if it is none, use 0 as its value on this bit.                       
        value = ((l1 and l1.val) or 0) + ((l2 and l2.val) or 0)
        carry = int(value/10)
        result = ListNode(value%10)
        result.next = self.addTwoNumbers(l1.next,l2.next)       
        # if carry exist ,created linked list with the value of carry and add it to current link node.
        if carry:
            result.next = self.addTwoNumbers(result.next,ListNode(carry))
        return result
