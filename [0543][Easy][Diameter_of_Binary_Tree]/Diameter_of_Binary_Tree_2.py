# solution 1,DFS.
# leetcode time     cost : 52 ms
# leetcode memory   cost : 15.3 MB 
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
        self.maxDiameter = 1 # set init to 1 to fit the return expression for not none tree.

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.dfs(root)
        # the top node path "1" of max diameter is added twice, need remove one,
        return self.maxDiameter - 1

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        currentDiameter = left + right + 1
        # update the max brach diameter to return to the top layer,
        maxBranchDiameter = max(left,right)+1
        # update the result,maxDiameter is not used to return to top layer
        self.maxDiameter = max(self.maxDiameter,currentDiameter)
        return maxBranchDiameter