# leetcode time     cost : 68  ms
# leetcode memory   cost : 16.4 MB 
# Time  Complexity: O(n*n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution 1, numerate every node as root to check
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def isValidBST(root,min_val = -float('inf'),max_val = float('inf')):
            isBST =  False
            if not root:
                return True
            # validate BST for current node
            if min_val< root.val < max_val:  
               isBST =  True
            
            subLeft = isValidBST(root.left,min_val,root.val)
            subRight =  isValidBST(root.right,root.val,max_val)
            return isBST and subLeft and subRight 

        def nodeCnt(root):
            if not root:
                return 0
            return 1 + nodeCnt(root.left) + nodeCnt(root.right)

        if not root: return 0
        if isValidBST(root):
            return nodeCnt(root)
        else:
            return max(self.largestBSTSubtree(root.left),self.largestBSTSubtree(root.right))