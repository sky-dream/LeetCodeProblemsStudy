# -*- coding: utf-8 -*-  
# leetcode time     cost : 84 ms
# leetcode memory   cost : 17.7 MB
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Solution 3, BFS, level order
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        queue = deque()
        if root: queue.appendleft(root)
        while queue:
            tmp = queue.pop()
            if tmp:
                res.append(tmp.val)
                queue.appendleft(tmp.left)
                queue.appendleft(tmp.right)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split(","))
        root = TreeNode(next(data))
        queue = deque([root])
        while queue:
            tmp = queue.pop()
            left_val = next(data)
            if left_val != "#":
                tmp.left = TreeNode(int(left_val))
                queue.appendleft(tmp.left)
            right_val = next(data)
            if right_val != "#":
                tmp.right = TreeNode(int(right_val))
                queue.appendleft(tmp.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))