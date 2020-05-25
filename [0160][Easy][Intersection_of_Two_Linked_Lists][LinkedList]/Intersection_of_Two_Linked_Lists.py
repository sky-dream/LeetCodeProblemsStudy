# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 2 pointers, len_a + len_b = len_b + len_a
# Time  Complexity: O(m+n)
# Space Complexity: O(1)
# leetcode time     cost : 224 ms
# leetcode memory   cost : 28.9 MB 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA