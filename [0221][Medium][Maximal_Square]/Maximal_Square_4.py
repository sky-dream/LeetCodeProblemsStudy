# https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm
# leetcode time     cost : 112 ms
# leetcode memory   cost : 14.4 MB 
# 类型：二维DP
# Time Complexity O(N^2)
# Space Complexity O(N^2)
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        res = max(max(row) for row in dp)
        return res ** 2

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  