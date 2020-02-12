class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 2 DFB with iteration.
# leetcode time     cost : 36 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root),], float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        
        return min_depth 