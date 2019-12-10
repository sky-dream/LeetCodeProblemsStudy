class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums)        
        while (left <right):  
            sum_value = 0
            mid = left + int((right - left)/2)
            for i in range(len(nums)):
                sum_value = sum_value + int(nums[i]/mid) + (nums[i]%mid >0) 
            if(sum_value > threshold) :
                left = mid + 1
            else:
                right = mid 
        return left
nums = [1,2,5,9,12,7,10,23]
threshold = 10
s = Solution()
print(s.smallestDivisor(nums,threshold))