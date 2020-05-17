# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 2, iteration
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(m+n)
# Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummyNode = ListNode(-1)
        prevNode = dummyNode

        while l1 and l2:
            if l1.val <= l2.val:
                prevNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                prevNode.next = ListNode(l2.val)
                l2 = l2.next
            prevNode = prevNode.next
        if l1:
            prevNode.next = l1
        else:
            prevNode.next = l2
        return dummyNode.next