# solution 1,DFS.
# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.4 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxDiameter = 0 

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.dfs(root)
        # no need to -1 if maxDiameter initial value is 0
        return self.maxDiameter

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # no need to +1 if maxDiameter initial value is 0
        currentDiameter = left + right 
        # update the max brach diameter to return to the top layer,
        maxBranchDiameter = max(left,right)+1
        # update the result,maxDiameter is not used to return to top layer
        self.maxDiameter = max(self.maxDiameter,currentDiameter)
        return maxBranchDiameter