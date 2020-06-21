# -*- coding: utf-8 -*-  
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
# Time  Complexity: O(n)
# Space Complexity: O(1)
# leetcode time     cost : 64 ms
# leetcode memory   cost : 14.8 MB
# solution 2, using next pointer
class Solution:
    def processChild(self, childNode, nextLevelNode, leftmost):
        if childNode:
            
            # If the "nextLevelNode" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if nextLevelNode:
                nextLevelNode.next = childNode
            else:    
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            nextLevelNode = childNode 
        return nextLevelNode, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "nextLevelNode" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            nextLevelNode, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the nextLevelNode
                # and leftmost pointers as necessary.
                nextLevelNode, leftmost = self.processChild(curr.left, nextLevelNode, leftmost)
                nextLevelNode, leftmost = self.processChild(curr.right, nextLevelNode, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root 