# leetcode time     cost : 688 ms
# leetcode memory   cost : 18.8 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
from typing import  List
# solution 3,dp，
# f[i][j] 表示前 i 个数中选取了若干个数，并且它们的和模 3 余 j 时，这些数的和的最大值
# f[i][j] = max(f[i - 1][j], f[i - 1][(j - nums[i]) % 3] + nums[i])
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -1, -1]
        for num in nums:
            g = f[:]
            for i in range(3):
                if f[i] != -1:
                    g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]


def main():
    nums = [3,6,5,1,8]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.maxSumDivThree(nums)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  