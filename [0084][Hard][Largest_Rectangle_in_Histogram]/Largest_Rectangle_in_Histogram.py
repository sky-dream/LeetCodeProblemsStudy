# -*- coding: utf-8 -*-  
# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.2 MB
# solution 5, stack,
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea   