# -*- coding: utf-8 -*-  
# leetcode time     cost : 112 ms
# leetcode memory   cost : 14.4 MB
# solution 3, refer to No.84,
class Solution():
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m, n, maxarea = len(matrix), len(matrix[0]), 0
        height = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                height[j] = height[j]+1 if matrix[i][j]=="1" else 0
            maxarea = max(maxarea, self.largestRectangleArea(height))
        return maxarea
                
    def largestRectangleArea(self, height):
        height.append(0)
        stack, maxarea = [0], 0
        for i in range(1, len(height)):
            while stack and height[stack[-1]] > height[i]: 
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1 
                maxarea = max(maxarea, w*h)
            stack.append(i)
        return maxarea

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 6
    Solution_obj = Solution()
    result = Solution_obj.maximalRectangle(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  