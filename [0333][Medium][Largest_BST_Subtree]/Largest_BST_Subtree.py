# leetcode time     cost : 132  ms
# leetcode memory   cost : 16.3 MB 
# Time  Complexity: O(n*n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# slolution 1, enumerate all cases,from my own,  
class Solution:
    ans = 0
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def helper(root,min_val,max_val):
            isBST, count = isBST_l, count_l = isBST_r, count_r = False, 0

            # 1,root is none
            if not root :
                return True,0

            # validate BST for current node
            if min_val< root.val < max_val:  
               isBST =  True

            # 2, only one root node,no sub tree
            if not root.left and not root.right :
                count = 1
                self.ans = max(self.ans,count)
                return isBST,count

            # do recursive check the entire tree, recursive pass min,max
            isBST_l, count_l = helper(root.left,min_val,root.val)
            isBST =  isBST and isBST_l

            isBST_r, count_r = helper(root.right,root.val,max_val)  
            isBST =  isBST and isBST_r

            # 3. the root is the BST tree, sum all nodes, include left or right is null
            if isBST:
                count = 1 + count_l + count_r 
                # take max count from sub node
                self.ans = max(self.ans,count)

            # 4. current root is not the BST, take left or right as root
            else:
                # take the left as the new root
                helper(root.left,-float('inf'),float('inf'))
                # take the right as the new root
                helper(root.right,-float('inf'),float('inf')) 

            return isBST, count
        helper(root,-float('inf'),float('inf'))

        return self.ans