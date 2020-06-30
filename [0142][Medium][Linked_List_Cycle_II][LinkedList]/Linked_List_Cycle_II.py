# -*- coding: utf-8 -*- 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
# leetcode time     cost : 76 ms
# leetcode memory   cost : 17.2 MB
# solution 1, hash set
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None