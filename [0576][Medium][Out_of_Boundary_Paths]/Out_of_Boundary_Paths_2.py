# leetcode time     cost : 236 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(m*n*N)
# Space Complexity: O(m*n)
# solution 1, DP,refer to No.688
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # assuming a virtual boundary for the grid
        dp = dp2 = [[0]*(n+2) for _ in range(m+2)]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        max_divider = 10**9+7
        # init the start point,adjust the index due to the new boundary
        i,j = i+1,j+1
        dp[i][j] = 1 
        res = 0
        if N ==0:
            return 0
        if m==1 and n==1:
            return 4

        # if the point will reach the virtual boundary(index=0 or m+1 or n+1) by row or col, sum the path number
        def outOfBoundCount(row,col,count):
            new_count = 0
            # need check 4 direction individually, if m ==1, then row==1,also row==m
            if row==1:
                new_count +=count
            if row==m:
                new_count +=count
            if col==1:
                new_count +=count
            if col==n:
                new_count +=count                
            return new_count
        # check 1st step    
        res = (res + outOfBoundCount(i,j,dp[i][j]) ) % max_divider 
        # skip already checked 1st step
        for k in range(1,N):
            dp2 = [[0]*(n+2) for _ in range(m+2)]
            for row in range(1,m+1):
                for col in range(1,n+1):
                    dp2[row][col] = (dp[row-1][col] + dp[row+1][col] \
                                    +dp[row][col-1] + dp[row][col+1])
                    dp2[row][col] = dp2[row][col] % max_divider                
                    res = (res + outOfBoundCount(row,col,dp2[row][col]) ) % max_divider 
                    #print(row,col,",dp2[row][col]:",dp2[row][col],",k:",k,",res:",res)
            dp = dp2
        return res
    
def main():
    m, n, N, i, j = 1,3,1,0,1  # ans 2
    obj = Solution()
    res = obj.findPaths(m, n, N, i, j)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     