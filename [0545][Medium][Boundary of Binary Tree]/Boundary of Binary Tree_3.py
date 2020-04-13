# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.9 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution 3, 2 times scan, 1st scan the left boundary, then scan the right boundary


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root:
            return []

        result = []
        stack = []
        stack.append(root)

        if root.left:
            left_boundary_traversal_done = False
        elif root.right:
            left_boundary_traversal_done = True
            result.append(root.val)
        else:
            return [root.val]

        while stack:
            node = stack.pop()
            left = node.left
            right = node.right

            if right:
                stack.append(right)
            if left:
                stack.append(left)
            # if reached first leaf node, set left flag on, then only handle leaf node
            if (not left and not right) or not left_boundary_traversal_done:
                if not left and not right:
                    # No longer registering non-latest node as the left boundary is traversed.
                    left_boundary_traversal_done = True
                result.append(node.val)

        # Register nodes on right boundary.
        right_boundry = []
        root = root.right
        while root:
            if (root.left and root.right) or (not root.left and root.right):
                right_boundry.append(root.val)
                root = root.right
            elif root.left:
                right_boundry.append(root.val)
                root = root.left
            # if reached the leaf node, exit the loop
            else:
                break
        right_boundry.reverse()

        return result + right_boundry
