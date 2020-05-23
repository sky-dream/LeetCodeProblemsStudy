# leetcode time     cost : 156 ms
# leetcode memory   cost : 17.8 MB 
# Time  Complexity: O(Nlogk),
# Space Complexity: O(N)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution2. min heap
import queue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = queue.PriorityQueue()
        for index, l in enumerate(lists):
            if l:
                #add index to solve heap compare conflict for 2 same value
                q.put((l.val,index, l))
        while not q.empty():
            val,index, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,index, node))
        return head.next