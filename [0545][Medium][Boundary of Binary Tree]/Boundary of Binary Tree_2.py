# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.8 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution 2, 2 times loop for left boundary, leaves in left branch, right boundary,leaves in right branch,


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root:
            return []

        left_result = []
        right_result = []
        left_stack = []
        right_stack = []

        if root.left:
            left_boundary_traversal_done = False
            left_stack.append(root.left)

            while left_stack:
                node = left_stack.pop()
                left = node.left
                right = node.right

                if right:
                    left_stack.append(right)
                if left:
                    left_stack.append(left)
                # if reached first leaf node, set left flag on, then only handle leaf node
                if (not left and not right) or not left_boundary_traversal_done:
                    if not left and not right:
                        left_boundary_traversal_done = True
                    left_result.append(node.val)

        if root.right:
            right_boundary_traversal_done = False
            right_stack.append(root.right)

            while right_stack:
                node = right_stack.pop()
                left = node.left
                right = node.right

                if left:
                    right_stack.append(left)
                if right:
                    right_stack.append(right)
                # if reached first leaf node, set right flag on, then only handle leaf node
                if (not left and not right) or not right_boundary_traversal_done:
                    if not left and not right:
                        right_boundary_traversal_done = True
                    right_result.append(node.val)
        if not root.left and not root.right:
            return [root.val]

        right_result.reverse()

        return [root.val] + left_result + right_result
