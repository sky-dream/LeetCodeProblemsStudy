# leetcode time     cost : 536 ms
# leetcode memory   cost : 61.8 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.maxBSTSum = 0   
    # the recursive function need return (isBST,min_val,max_val,sum_val) when take current as root
    def dfsHelper(self,root):
        # set the ending condition
        if not root:
            isBST,min_val,max_val,sum_val = True,float('inf'),-float('inf'),0
            return (isBST,min_val,max_val,sum_val)
        isBST_L,min_val_L,max_val_L,sum_val_L = self.dfsHelper(root.left)
        isBST_R,min_val_R,max_val_R,sum_val_R = self.dfsHelper(root.right)
        # if current node is root, check it is BST or not
        if(isBST_L and isBST_R and max_val_L<root.val<min_val_R):
            isBST = True
            sum_val = root.val + sum_val_L + sum_val_R
            # get min,max for current sub tree root
            min_val = min(min_val_L,root.val)
            max_val = max(max_val_R,root.val)
            # update the result
            self.maxBSTSum = max(self.maxBSTSum,sum_val)

        else:
            # set result for none BST sub tree
            isBST,min_val,max_val,sum_val = False, -float('inf'),float('inf'),0
        return (isBST,min_val,max_val,sum_val)    

    def maxSumBST(self, root: TreeNode):
        self.dfsHelper(root)
        return self.maxBSTSum