# -*- coding: utf-8 -*-  
# leetcode time     cost : 1824 ms
# leetcode memory   cost : 15.4 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        newHead = sortPosition = ListNode(-1)
        currentNode = head
        while currentNode:
            # save the next node in unsorted list
            nextNode = currentNode.next
            # loop new link list to find the position of new current node
            while sortPosition.next and sortPosition.next.val < currentNode.val:
                sortPosition = sortPosition.next
            # insert node to new list before the node just bigger than it
            currentNode.next = sortPosition.next
            sortPosition.next = currentNode
            sortPosition = newHead
            # restore the link list loop
            currentNode = nextNode
        return newHead.next