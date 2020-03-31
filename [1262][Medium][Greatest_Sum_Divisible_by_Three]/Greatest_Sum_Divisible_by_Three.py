# leetcode time     cost : 428 ms
# leetcode memory   cost : 18.8 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
from typing import  List
# solution 1,greedy. get max numbers that can be used
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for j0 in [lb - 2, lb - 1, lb]:
            if j0 >= 0:
                for k0 in [lc - 2, lc - 1, lc]:
                    if k0 >= 0 and j0 % 3 == k0 % 3:
                        ans = max(ans, sum(b[:j0]) + sum(c[:k0]))
        return ans + sum(a)


def main():
    nums = [3,6,5,1,8]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.maxSumDivThree(nums)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  