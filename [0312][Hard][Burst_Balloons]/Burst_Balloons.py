# leetcode time     cost : 624 ms
# leetcode memory   cost : 15.7 MB 
# Time  Complexity: O(N*N*N)
# Space Complexity: O(N*N)
# SOLUTION 1, DP, from Top to Bottom
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # reframe the problem
        nums = [1] + nums + [1]

        # cache this
        @lru_cache(None)
        def dp(left, right):

            # no more balloons can be added
            if left + 1 == right: return 0

            # add each balloon on the interval and return the maximum score
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)

def main():
    nums = [3,1,5,8]         #expect is 167
    s = Solution()
    res = s.maxCoins(nums) 
    print("in python,res is : ",res)
if __name__ =='__main__':
    main() 