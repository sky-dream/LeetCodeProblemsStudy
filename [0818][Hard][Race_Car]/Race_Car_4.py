# -*- coding: utf-8 -*-  
# leetcode time     cost : 340 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(T∗logT)
# Space Complexity: O(T)
# solution 4, dp
# https://leetcode-cn.com/problems/race-car/solution/sai-che-by-leetcode/
class Solution(object):
    def racecar(self, target):
        # dp[i] is the min step come to position i, 2**(k-1) < i < 2**k, k is the steps of A
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            # use k-1 step A,not come to target, then R, then R, then go forward, use j step A to target.
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            # use k step A,come over target,then use R turn back, go left distance [target - (2**k) - 1 ] , use already got dp[j]
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]


def main():
    target = 16      #expect is 7  
    obj = Solution()
    res = obj.racecar(target)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 