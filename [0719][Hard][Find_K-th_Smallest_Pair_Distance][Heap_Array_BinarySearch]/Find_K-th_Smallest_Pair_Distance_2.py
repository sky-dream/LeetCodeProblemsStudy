# leetcode time     cost : 128 ms
# leetcode memory   cost : 14.7 MB
# Time  Complexity: O(NlogW+NlogN),w = max(nums)
# Space Complexity: O(1)
# solution 3, binary search and 2 pointers
# time : O(NlogW+NlogN)
# memory : O(1)
class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

def main():
    nums = [1,3,1]; k = 1;expectRes = 0
    obj = Solution()
    result = obj.smallestDistancePair(nums, k)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ", expectRes)
    
if __name__ =='__main__':
    main() 