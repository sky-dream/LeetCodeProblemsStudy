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

# solution 2, record min,max, BST node count when take every node as the root
class Solution:
    def __init__(self):
        self.ans = 0
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            min_val,max_val, validCount = root.val,root.val,1
            if not root.left and not root.right:
                self.ans = max(self.ans,1)
                return min_val,max_val, validCount
            isBST =  True

            if root.left:
                min_valLeft,max_valLeft, validCountLeft =  dfs(root.left)
                if validCountLeft !=-1 and max_valLeft < root.val:
                   validCount +=validCountLeft
                   min_val = min_valLeft
                else:
                    isBST = False
            if  root.right:
                min_valRight,max_valRight, validCountRight =  dfs(root.right)
                if validCountRight !=-1 and root.val < min_valRight:
                   validCount +=validCountRight
                   max_val = max_valRight
                else:
                    isBST = False                
            
            if  isBST:                
                self.ans = max(self.ans,validCount)
            # if current node is not BST root,return invalid value,no need update the ans 
            else:
                min_val,max_val, validCount = -1,-1,-1
            #print("root,",root.val,",isBST,",isBST,",validCount,",validCount)   
            return (min_val,max_val, validCount)

        if not root: return 0
        dfs(root)
        return self.ans
