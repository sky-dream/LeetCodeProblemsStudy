# -*- coding: utf-8 -*-  
# Time  Complexity: O(A+B)
# Space Complexity: O(1)
# solution 1, Math analysis
# https://leetcode-cn.com/problems/nth-magical-number/solution/di-n-ge-shen-qi-shu-zi-by-leetcode/
from math import gcd 
# 贝祖定理，ax+by=z，当且仅当 z 是 x,y 的最大公约数的倍数 有解
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        
        MOD = 10**9 + 7
        # math.gcd(x, y)求x,y 的最大公约数，辗转相除定理
        L = A // gcd(A, B) * B
        M = L // A + L // B - 1
        q, r = divmod(N, M)  # 同时求商和余数

        if r == 0:
            return q * L % MOD

        heads = [A, B]
        for _ in range(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return (q * L + min(heads)) % MOD

def main():
    N,A,B = 5,2,4      #expect is 10  
    obj = Solution()
    res = obj.nthMagicalNumber(N, A, B)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 