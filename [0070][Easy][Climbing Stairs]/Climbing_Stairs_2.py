class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        oneStepBefore = 2
        twoStepBefore = 1
        totalWays = 0
        for i in range(2,n):
            totalWays = oneStepBefore + twoStepBefore
            twoStepBefore = oneStepBefore
            oneStepBefore = totalWays        
        return totalWays
s = Solution()
print(s.climbStairs(30))