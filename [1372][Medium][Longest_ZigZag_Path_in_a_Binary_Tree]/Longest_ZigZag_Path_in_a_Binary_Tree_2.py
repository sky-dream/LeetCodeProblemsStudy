# leetcode time     cost : 444 ms
# leetcode memory   cost : 52.6 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 2, set null node as the dfs terminal
class Solution:
    def __init__(self):
        self.maxZZLength = 0
    # return the left direction zz length and the right direction zz length of every node,
    def dfsHelper(self,root):
        # recursion terminal, return 0 for both direction if current node is none
        if not root:
            return (0,0)

        leftDirLength_LeftNode,rightDirLength_LeftNode = self.dfsHelper(root.left)
        leftDirLength_RightNode,rightDirLength_RightNode = self.dfsHelper(root.right)

        leftDirLength_Current = 1 + rightDirLength_LeftNode
        rightDirLength_Current = 1 + leftDirLength_RightNode

        self.maxZZLength = max(self.maxZZLength,leftDirLength_Current,rightDirLength_Current)
        return (leftDirLength_Current,rightDirLength_Current)

    def longestZigZag(self, root: TreeNode):

        self.dfsHelper(root)
        # remove the duplicate count when the counted node is leaf, since in dfs it is used as (1,1) 
        return (self.maxZZLength - 1)