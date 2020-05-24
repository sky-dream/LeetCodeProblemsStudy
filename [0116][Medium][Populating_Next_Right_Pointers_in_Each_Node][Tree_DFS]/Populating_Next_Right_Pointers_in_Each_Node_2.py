# -*- coding: utf-8 -*-  
# solution 2, DFS
# Time  Complexity: O(n)
# Space Complexity: O(1)
# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.1 MB
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        # Once we reach the final level, we are done
        # loop from top to bottom with left pointer
        while leftmost.left:
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            # loop from left to right with next pointer
            while head:
                # CONNECTION 1
                head.left.next = head.right
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                # Progress along the list (nodes on the current level)
                head = head.next
            # Move onto the next level
            leftmost = leftmost.left
        return root