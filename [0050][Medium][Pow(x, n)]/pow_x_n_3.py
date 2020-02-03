#solution 1, recursion, 5 lines concise version.
# leetcode time     cost : 20 ms
# leetcode memory   cost : 11.7 MB  
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: 
            return 1
        if n == -1: 
            return 1 / x
        return self.myPow(x * x, n / 2) * ([1, x][n % 2])