#solution 1, recursion.
# leetcode time     cost : 16 ms
# leetcode memory   cost : 11.7 MB 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        return self.fastPow(x, N); 

    def fastPow(self, x,  n):
        if n == 0:
            return 1.0
        half = self.fastPow(x, n / 2)
        if n % 2 == 0:
            return half * half
        else: 
            return half * half * x 