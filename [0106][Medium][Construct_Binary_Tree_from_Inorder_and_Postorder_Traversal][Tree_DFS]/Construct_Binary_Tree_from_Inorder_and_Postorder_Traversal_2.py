# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution 2, stack and iteration, based on 105, solution 2,
# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.5 MB
# Time  Complexity: O(n)
# Space Complexity: O(h)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        stack = [root]
        inorderIndex = len(inorder)-1
        for i in range(len(postorder)-2,-1,-1):
            postorderVal = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorderVal) 
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex -= 1
                node.left = TreeNode(postorderVal)
                stack.append(node.left)

        return root