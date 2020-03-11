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

class Solution:
    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /   \          \
 1   2   1      [1,0]  [2,0]     [1,0]
    """
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
    
    def dfs(self, root: TreeNode):
        if not root:
            return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))