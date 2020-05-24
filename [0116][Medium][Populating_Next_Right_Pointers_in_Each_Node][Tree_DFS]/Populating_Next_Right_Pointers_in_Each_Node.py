# -*- coding: utf-8 -*-  
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# solution 1, BFS
# Time  Complexity: O(n)
# Space Complexity: O(n)
# leetcode time     cost : 72 ms
# leetcode memory   cost : 15.3 MB
import collections 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])
        # Outer while loop which iterates over each level
        while Q:
            # Note the size of the queue
            size = len(Q)
            # Iterate over all the nodes on the current level
            for i in range(size):
                # Pop a node from the front of the queue
                node = Q.popleft()
                # This check is important. the last one in current level no need add next pointer
                if i < size - 1:
                    # always use the first node in the queue after current pop
                    node.next = Q[0]
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root