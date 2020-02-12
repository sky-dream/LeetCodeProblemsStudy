class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 3 BFB with iteration.
# leetcode time     cost : 16 ms
# leetcode memory   cost : 14.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
from collections import deque
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])
        
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))