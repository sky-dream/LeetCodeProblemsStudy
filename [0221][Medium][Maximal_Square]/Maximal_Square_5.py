# https://leetcode.com/problems/maximal-square/discuss/61845/9-lines-Python-DP-solution-with-explaination
# leetcode time     cost : 112 ms
# leetcode memory   cost : 14.4 MB 
class Solution(object): 
    def maximalSquare(self, matrix):
        dp, maxLength = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxLength = max(maxLength, dp[i][j])
        return maxLength*maxLength

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  