class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 1 recursion.
# leetcode time     cost : 40 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(N)
# Space Complexity: worst case is O(N), for best case of balance tree, it is O(log(N))
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0 
        
        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1 