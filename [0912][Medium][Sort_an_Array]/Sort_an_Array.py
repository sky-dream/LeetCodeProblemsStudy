# leetcode time     cost : 344 ms
# leetcode memory   cost : 19.8 MB 
# Time  Complexity: O(N*logN) 
# Space Complexity: O(logN)
# solution 1, fast sort
import random
class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

def main():
    nums = [5,2,3,1]      #expect is [1,2,3,5]
    obj = Solution()
    res = obj.sortArray(nums)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   