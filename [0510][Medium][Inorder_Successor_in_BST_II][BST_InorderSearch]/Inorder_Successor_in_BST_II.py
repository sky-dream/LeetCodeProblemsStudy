# leetcode time     cost : 116 ms
# leetcode memory   cost : 21.3 MB
# Time  Complexity: O(H)
# Space Complexity: O(1)
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# solution 1, iteration
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent