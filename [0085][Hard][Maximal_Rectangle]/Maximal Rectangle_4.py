# -*- coding: utf-8 -*-  
# leetcode time     cost : 88 ms
# leetcode memory   cost : 14.2 MB
# solution 4, DP, calculate the heigth and width with stack
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        # n is the column of the matrix
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 6
    Solution_obj = Solution()
    result = Solution_obj.maximalRectangle(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  