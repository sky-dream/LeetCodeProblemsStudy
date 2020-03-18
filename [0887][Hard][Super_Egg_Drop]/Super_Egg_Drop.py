# -*- coding: utf-8 -*-  
# leetcode time     cost : max time exceeded when K=100,N=8191
# leetcode memory   cost : --
# Time  Complexity: O(K∗NlogN)
# Space Complexity: O(K∗N)
# solution 1, bynary search and DP
class Solution(object):
    def superEggDrop(self, K, N):
        dp = [[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(K+1):
            dp[i][0] = 0            # if the floor is 0 with i eggs
            dp[i][1] = 1            # if the floor is 1 with i eggs
        for j in range(1,N+1):
            dp[1][j] = j            # if the floor is j with 1 egg
            
        for i in range(2,K+1):
            for j in range(2,N+1):
                # binary search, where the previous egg drop k th floor can make the current drop time is smallest
                lo, hi = 0, j
                # (lo+1) < hi to prevent stuck of [1 = (0+2)//2,====> 1 = (1+2)//2]
                while lo+1 < hi:
                    mid = (lo+hi)//2
                    # find k for ===> dp[i][j] = min(1 + max(dp[i-1][k-1], dp[i][j-k]))
                    left, right = dp[i-1][mid-1],dp[i][j-mid]       # dp[1][1]=0 ,dp[2][1]=1                     
                    if left < right:
                        lo = mid
                    elif left > right:
                        hi = mid
                    else:
                        lo = hi = mid
                        break
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][lo-1], dp[i][j-lo]))
            #print("egg: ",i,"floor: ",j,",egg drop min time ",dp[i][j]) 
        return dp[K][N]

def main():
    K,N = 3,10      #expect is 6  
    obj = Solution()
    res = obj.superEggDrop(K,N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 