# leetcode time     cost : 624 ms
# leetcode memory   cost : 26.2 MB
# Time  Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 3, DP with memo
import collections
class Solution:
    def longestZigZag(self, root: TreeNode):

        leftDirLengthDict, rightDirLengthDict = collections.defaultdict(int), collections.defaultdict(int)

        q = collections.deque([(root, None)])
        while len(q) > 0:
            node, parent = q.popleft()
            if parent:
                if parent.left == node:
                    leftDirLengthDict[node] = rightDirLengthDict[parent] + 1
                else:
                    rightDirLengthDict[node] = leftDirLengthDict[parent] + 1
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))
        
        maxZZLength = 0
        for _, val in leftDirLengthDict.items():
            maxZZLength = max(maxZZLength, val)
        for _, val in rightDirLengthDict.items():
            maxZZLength = max(maxZZLength, val)
        return maxZZLength