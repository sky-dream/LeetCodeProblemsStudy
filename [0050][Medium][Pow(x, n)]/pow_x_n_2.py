#solution 1, recursion
# leetcode time     cost : 20 ms
# leetcode memory   cost : 11.7 MB 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)