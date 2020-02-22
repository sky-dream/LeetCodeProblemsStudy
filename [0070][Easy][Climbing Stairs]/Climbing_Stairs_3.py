# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
# slolution 3, DP
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        dp = [0 for i in range(n+1)]
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

def main():
    num = 10          # expect is 89,
    obj = Solution()
    result = obj.climbStairs(num)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 