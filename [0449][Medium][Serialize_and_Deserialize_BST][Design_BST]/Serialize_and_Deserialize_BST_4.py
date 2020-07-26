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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorderTraversal(root):#前序遍历
            if root == None:
                return  []
            left = preorderTraversal(root.left)
            right = preorderTraversal(root.right)
            return [root.val] + left + right
        L =preorderTraversal(root)
        return ' '.join([str(i) for i in L])#转化为字符串

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split()
        data = [int(i) for i in data]#将字符串转化为数值的列表
        
        def buildTree(data):
            if not data:
                return None
            root = TreeNode(data[0])
            left = [i for i in data if i < data[0]]#左子树的节点值小于根节点
            right = [i for i in data if i > data[0]]#右子树的节点值大于根节点的值
            root.left = buildTree(left)#重建左子树
            root.right =buildTree(right)#重建右子树
            return root
        return buildTree(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))