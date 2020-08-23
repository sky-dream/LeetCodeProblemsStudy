# -*- coding: utf-8 -*-  
# Time  Complexity: O(log(N∗max(A,B)))
# Space Complexity: O(1)
# solution 2, Binary search
# https://leetcode-cn.com/problems/nth-magical-number/solution/di-n-ge-shen-qi-shu-zi-by-leetcode/
from math import gcd 
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        MOD = 10**9 + 7
        L = A / gcd(A,B) * B

        def magic_below_x(x):
            # How many magical numbers are <= x?
            return (x // A + x // B - x // L)

        lo = 0
        hi = 10**15
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if magic_below_x(mid) < N:
                lo = mid + 1
            else:
                hi = mid

        return lo % MOD


def main():
    N,A,B = 5,2,4      #expect is 10  
    obj = Solution()
    res = obj.nthMagicalNumber(N, A, B)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 