# -*- coding: utf-8 -*-  
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution 2, inorder traversal
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def _inorder(root):
            if not root: return
            # 遍历左子树
            _inorder(root.left)
            
            nonlocal pre, nodes
            if pre and pre.val > root.val:  # 记录当前的逆序对
                nodes.append(pre)
                nodes.append(root)
            pre = root
            # 遍历右子树
            _inorder(root.right)

        pre = None
        nodes = []
        _inorder(root)
        if len(nodes) == 2:
            i, j = 0, 1
        elif len(nodes) == 4:
            i, j = 0, 3
        else:
            return

        nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
        return