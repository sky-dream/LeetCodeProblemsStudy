# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = currentNode = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            # use and to check whether the node pointer is none, if it is none, use 0 as its value on this bit.
            value = ((l1 and l1.val) or 0) + ((l2 and l2.val) or 0) + carry
            carry = int(value/10)
            currentNode.next = ListNode(value%10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            currentNode = currentNode.next
        return res.next    
