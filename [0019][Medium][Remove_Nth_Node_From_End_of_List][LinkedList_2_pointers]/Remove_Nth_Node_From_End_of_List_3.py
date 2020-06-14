#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution 3, recursion
class Solution:
    def __init__(self):
        self.reversed_idx = 0
    def removeNthFromEnd(self, head, n):
        if head is None:
            self.reversed_idx=0
            return None
        head.next = self.removeNthFromEnd(head.next,n)
        self.reversed_idx+=1
        return head.next if self.reversed_idx==n else head