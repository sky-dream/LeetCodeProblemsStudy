# -*- coding: utf-8 -*-  
# leetcode time     cost : 56 ms
# leetcode memory   cost : 16.2 MB
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# python 中序遍历

class Solution(object):
    def __init__(self):
        self.travelpath = []
 
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        if root is not None:
            
            self.inorderTraversal(root.left)
            self.travelpath.append(root.val)
            self.inorderTraversal(root.right)
        return self.travelpath  