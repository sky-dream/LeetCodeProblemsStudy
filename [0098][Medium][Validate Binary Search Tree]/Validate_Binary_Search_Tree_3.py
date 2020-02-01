# -*- coding: utf-8 -*-  
# leetcode time     cost : 76 ms
# leetcode memory   cost : 15.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# without the help from the value range border
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)

    def helper(self, root, left=None, right=None):
        if not root:
            return True
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False
        return self.helper(root.left, left, root) and\
               self.helper(root.right, root, right)