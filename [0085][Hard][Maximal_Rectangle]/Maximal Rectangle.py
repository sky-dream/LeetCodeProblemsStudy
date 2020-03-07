# -*- coding: utf-8 -*-  
# leetcode time     cost : -- ms
# leetcode memory   cost : -- MB
# solution 2, optimized brute force, time exceeded,
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = (dp[i][j-1] + 1) if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea  


def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 6
    Solution_obj = Solution()
    result = Solution_obj.maximalRectangle(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  