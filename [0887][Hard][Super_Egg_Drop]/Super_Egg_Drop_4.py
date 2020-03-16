# -*- coding: utf-8 -*-  
# leetcode time     cost : max time exceeded
# leetcode memory   cost : --- MB
# Time  Complexity: O(K∗N*N)
# Space Complexity: O(K∗N)
# solution 4, brute force
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
        
        for i in range(2, K+1):
            for j in range(2, N+1):
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[K][N]


def main():
    K,N = 4,50      #expect is 6  
    obj = Solution()
    res = obj.superEggDrop(K,N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()