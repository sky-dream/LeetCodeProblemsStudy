# -*- coding: utf-8 -*-  
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 2, iteration with stack
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		stack = []
		current = root
		while stack or current:
			# 不断往左子树方向走，每走一次就将当前节点保存到栈中
			# 这是模拟递归的调用
			if current:
				stack.append(current)
				current = current.left
			# 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
			# 然后转向右边节点，继续上面整个过程
			else:
				tmp = stack.pop()
				res.append(tmp.val)
				current = tmp.right
		return res