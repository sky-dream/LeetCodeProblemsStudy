# https://leetcode-cn.com/problems/maximal-square/solution/dong-tai-gui-hua-by-powcai-9/
# leetcode time     cost : 2388 ms
# leetcode memory   cost : 15.3 MB 
class Solution:
    def maximalSquare(self, matrix: '''List[List[str]]''') -> int:
        if not matrix:  return 0	
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = int(matrix[i - 1][j - 1]) + dp[i][j - 1]
        # pprint(dp)
        for j in range(1, col + 1):
            for i in range(1, row + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j]
        # 思路一 
        # res = 0
        # for i in range(1, row + 1):
        #     for j in range(1, col + 1):
        #         for k in range(0, i):
        #             if j - i + k >= 0 and (i - k) ** 2 == dp[i][j] - dp[k][j] - dp[i][j - i + k] + dp[k][j - i + k]:
        #                 res = max(res, (i - k) ** 2)
        # return res
        # 思路二 卷积里滑动窗口的感觉
        max_edge = min(row, col)
        res = 0
        while max_edge:
            for i in range(row - max_edge + 1):
                for j in range(col - max_edge + 1):
                    if max_edge ** 2 == dp[i + max_edge][j + max_edge] - dp[i+max_edge][j] - dp[i][j + max_edge] + dp[i][j]:
                        return max_edge ** 2
            max_edge -= 1
        return res

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  