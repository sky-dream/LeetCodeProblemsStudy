from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

def main():
    k = 3
    
    nums1 = [9,3,-1,-3,5,3,6,7,-3] #expect is [9,3,5,5,6,7,7]
    obj = Solution()
    result = obj.maxSlidingWindow(nums1, k)
    print("last return result is "+str(result));
    
    nums2 = [1,3,-1,-3,5,3,6,7,-3] #expect is [3,3,5,5,6,7,7]
    result = obj.maxSlidingWindow(nums2, k)
    print("last return result is "+str(result));
if __name__ =='__main__':
    main() 