# -*- coding: utf-8 -*-  
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 1, recursion, 
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def swapPairs(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node