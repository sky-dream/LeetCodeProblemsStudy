# leetcode time     cost : 756 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N*N)
# Space Complexity: O(N)
#solution1.DP
class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 1
    obj = Solution()
    result = obj.findNumberOfLIS(nums)
    print("return result is ",result);

if __name__ =='__main__':
    main() 