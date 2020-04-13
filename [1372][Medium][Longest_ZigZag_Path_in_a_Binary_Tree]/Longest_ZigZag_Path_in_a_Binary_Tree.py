# leetcode time     cost : 492 ms
# leetcode memory   cost : 52.5 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 1, set leaf node as the dfs terminal
class Solution:
    def __init__(self):
        self.maxZZLength = 0
    # return the left direction zz length and the right direction zz length of every node,
    def dfsHelper(self,root):
        # recursion terminal, return 0 for both direction if current node is leaf node
        if not root.left and not root.right:
            return (0,0)
        
        if root.left:
            leftDirLength_LeftNode,rightDirLength_LeftNode = self.dfsHelper(root.left)
            leftDirLength_Current = 1 + rightDirLength_LeftNode
        else: 
            leftDirLength_LeftNode,rightDirLength_LeftNode = (0,0) 
            leftDirLength_Current = 0

        if root.right:  
            leftDirLength_RightNode,rightDirLength_RightNode = self.dfsHelper(root.right)
            rightDirLength_Current = 1 + leftDirLength_RightNode
        else: 
            leftDirLength_RightNode,rightDirLength_RightNode  = (0,0)             
            rightDirLength_Current = 0
        

        self.maxZZLength = max(self.maxZZLength,leftDirLength_Current,rightDirLength_Current)
        #print(root.val,",leftDirLength_Current: ",leftDirLength_Current,",rightDirLength_Current: ",rightDirLength_Current)
        return (leftDirLength_Current,rightDirLength_Current)

    def longestZigZag(self, root: TreeNode):

        self.dfsHelper(root)

        return self.maxZZLength