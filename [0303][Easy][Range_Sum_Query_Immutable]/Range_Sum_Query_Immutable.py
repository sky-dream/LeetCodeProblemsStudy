class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        # init sum_x[0] if nums is mull or empty
        self.sum_x = [0 for i in range(self.size+1)]
        if self.size>0:
            self.sum_x[0] = nums[0]
            for i in range(1,self.size):            
                self.sum_x[i] = self.sum_x[i-1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i >= self.size:
            i = j = self.size
        if j>= self.size:
            j = self.size
        if i is 0:
            return self.sum_x[j]
        return self.sum_x[j] - self.sum_x[i-1]


# Your NumArray object will be instantiated and called as such:
nums1 = [-2, 0, 3, -5, 2, -1]
nums2 = []
obj = NumArray(nums2)
print(obj.sumRange(0, 2))   # -> 1
print(obj.sumRange(2, 5))   # -> -1
print(obj.sumRange(0, 5))   # -> -3
       