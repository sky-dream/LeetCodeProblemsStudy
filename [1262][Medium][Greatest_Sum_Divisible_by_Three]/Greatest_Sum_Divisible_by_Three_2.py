# leetcode time     cost : 520 ms
# leetcode memory   cost : 18.8 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
from typing import  List
# solution 2,greedy. delete min numbers that can not be used
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        tot = sum(nums)
        ans = 0

        if tot % 3 == 0:
            ans = tot
        if tot % 3 == 1:
            if len(b) >= 1:
                ans = max(ans, tot - b[-1])
            if len(c) >= 2:
                ans = max(ans, tot - sum(c[-2:]))
        elif tot % 3 == 2:
            if len(b) >= 2:
                ans = max(ans, tot - sum(b[-2:]))
            if len(c) >= 1:
                ans = max(ans, tot - c[-1])

        return ans


def main():
    nums = [3,6,5,1,8]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.maxSumDivThree(nums)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  