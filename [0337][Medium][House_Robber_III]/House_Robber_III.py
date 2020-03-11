# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# DP
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def rob(self, root):
        def superrob(node):
            # returns tuple of size two (now, later)
            # now: max money earned if input node is robbed
            # later: max money earned if input node is not robbed
            
            # base case
            if not node: return (0, 0)
            # get values
            left, right = superrob(node.left), superrob(node.right)
            # rob now,then can only get the later(not robed) value of the next node.
            now = node.val + left[1] + right[1]
            # rob later
            later = max(left) + max(right)
            
            return (now, later)
        return max(superrob(root))