# leetcode time     cost : 360 ms
# leetcode memory   cost : 19.7 MB 
# Time  Complexity: O(N*logN) 
# Space Complexity: O(N)
# solution 3, merge sort
class Solution:
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

def main():
    nums = [5,2,3,1]      #expect is [1,2,3,5]
    obj = Solution()
    res = obj.sortArray(nums)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   