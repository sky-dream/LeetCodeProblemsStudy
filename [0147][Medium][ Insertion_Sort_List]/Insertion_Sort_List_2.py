# -*- coding: utf-8 -*-  
# leetcode time     cost : 216 ms
# leetcode memory   cost : 15.3 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        newHead = sortTail = sortPosition = ListNode(float("-inf"))
        currentNode = head
        while currentNode:
            # check whether currentNode can be append to the last
            if sortTail.val < currentNode.val:
                sortTail.next = currentNode
                sortTail = currentNode
                currentNode = currentNode.next
            else:
                # save the next node in unsorted list
                nextNode = currentNode.next 
                sortTail.next = nextNode               
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