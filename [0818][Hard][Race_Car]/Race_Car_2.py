# -*- coding: utf-8 -*-  
# leetcode time     cost : max recursion depth
# leetcode memory   cost : -- MB
# Time  Complexity: O(T∗logT)
# Space Complexity: O(T)
# solution 2, DP with recursion,
import math
class Solution:
    def racecar(self, target: int) -> int:
        #dp[i] is the least step used to reach position i.dp[target] is the answer
        dp = [0]*(target+1)

        def racecarHelper(t):
            if dp[t] >0: return dp[t]
            # least step that we can get nearest to t, continue A,position,1(step1),3(step2),7(step3),15,
            leastStep = int(math.log(8,2))
            # leastStep just get to t position
            if (1<<leastStep == (t+1)):
                dp[t] = leastStep
                return leastStep
            # if not, solve sub deviation in t and position(leastStep)
            dp[t] = leastStep + 1 + racecarHelper( (1<<leastStep) -1-t)
            # go back A for j step
            for j in range(leastStep):
                thirdForward = 1<<(leastStep-1) - 1<<j
                dp[t] = min(dp[t], leastStep+j+ racecarHelper(t-thirdForward) )

        return racecarHelper(target)


def main():
    target = 6      #expect is 5  
    obj = Solution()
    res = obj.racecar(target)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 