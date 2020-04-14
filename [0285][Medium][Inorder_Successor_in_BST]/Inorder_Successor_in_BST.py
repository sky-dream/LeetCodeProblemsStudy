#-*- coding: utf-8 -*-  
# leetcode time     cost : 88 ms
# leetcode memory   cost : 17.8 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, loop 2 different cases,p has right sub node, p do not have right node
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode'):
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            while root:
                stack.append(root)
                root = root.left
                
            # 2. all logic around the node
            root = stack.pop()
            if inorder == p.val:    # if the previous node was equal to p
                return root         # then the current node is its successor
            inorder = root.val
            
            # 3. go one step right
            root = root.right

        # there is no successor
        return None