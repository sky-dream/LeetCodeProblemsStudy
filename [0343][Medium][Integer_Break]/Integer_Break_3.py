# solution 3, backtracking with memory
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def integerBreak(self, n: int) -> int:
        # backtracking
        if n==2:
            return 1
        if n==3:
            return 2
        memo = [0 for _ in range(n+1)]
        def helper(n):
            if memo[n]!=0:
                return memo[n]
            if n <=3:
                return n
            halfsize = (n+1)//2
            res = 0
            for i in range(1,halfsize+2):
                left = helper(n-i)
                res = max(res,i*left)
            memo[n] = res
            return res
        return helper(n)
        
