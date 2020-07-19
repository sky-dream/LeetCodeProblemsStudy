# -*- coding: utf-8 -*- 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
# leetcode time     cost : 96 ms
# leetcode memory   cost : 16.2 MB
# solution 1, use set to check the duplicated node
# solution 2, slow,fast,2 pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            # print("slow:",slow.val,",fast:",fast.val)
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False