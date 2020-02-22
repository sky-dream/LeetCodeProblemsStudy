# -*- coding: utf-8 -*-  
# leetcode time     cost : 72 ms
# leetcode memory   cost : 14.4 MB
# solution 1, DP by iterate from the last 2nd row to the top row.
class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    def minimumTotal(self, triangle):
        row_size = len(triangle)
        dp = [0 for i in range(row_size)]
        max_clo_size = len(triangle[row_size - 1])
        # init the dp[] list
        for i in range(row_size):
            dp[i] = triangle[row_size - 1][i]
        # iterate from the last 2nd row to the top row.
        for i in range(row_size-2,-1,-1):
            row = triangle[i]
            for j in range(len(row)):
                # dp[j] consists of row[j] and the smaller adjacent value of the lower row
                dp[j] = row[j] + min(dp[j], dp[j+1])
        return dp[0]

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]        #expect is 11
    obj = Solution()
    result = obj.minimumTotal(triangle)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   