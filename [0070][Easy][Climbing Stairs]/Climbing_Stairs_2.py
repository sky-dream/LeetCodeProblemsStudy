# leetcode time     cost : 16 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# slolution 4, Fibonacci sequence,
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

def main():
    num = 10          # expect is 89,
    obj = Solution()
    result = obj.climbStairs(num)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 