# -*- coding: utf-8 -*-  
# leetcode time     cost : 28 ms
# leetcode memory   cost : 16.5 MB
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion terminal
        if not root:
            return self.res
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res