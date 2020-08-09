# -*- coding: utf-8 -*-  
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
# solution 3, Morris inorder traversal
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		pre = None
		while root:
			# 如果左节点不为空，就将当前节点连带右子树全部挂到
			# 左节点的最右子树下面
			if root.left:
				pre = root.left
				while pre.right:
					pre = pre.right
				pre.right = root
				# 将root指向root的left
				tmp = root
				root = root.left
				tmp.left = None
			# 左子树为空，则打印这个节点，并向右边遍历	
			else:
				res.append(root.val)
				root = root.right
		return res