# -*- coding: utf-8 -*-  
# leetcode time     cost : 28 ms
# leetcode memory   cost : 16.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# with the help of value range border
class Solution:
    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, root, left=float('-inf'), right=float('inf')):
        if not root:
            return True        
        # every node's value has its range, need to add constraint for them.
        return left < root.val < right and self.helper(root.left, left, root.val)\
               and self.helper(root.right, root.val, right)

# python3 get max int
# import sys
# max = sys.maxsize

# python3 get max float
# solution1, import sys, max = sys.float_info.max
# solution2, infinity = float("inf"), 