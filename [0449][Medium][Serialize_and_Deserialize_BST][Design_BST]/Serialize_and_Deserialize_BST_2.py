# -*- coding: utf-8 -*-  
# leetcode time     cost : 84 ms
# leetcode memory   cost : 17.7 MB
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Solution 2, pre order
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def preorder(root):
            if not root:
                res.append("#")
                return 
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = iter(data.split(","))
        def helper():
            tmp = next(d)
            # print(tmp)
            if tmp == "#":return 
            node = TreeNode(int(tmp))
            node.left = helper()
            node.right = helper()
            return node
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))