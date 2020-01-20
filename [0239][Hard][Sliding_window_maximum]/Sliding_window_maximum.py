class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:return []
        window, result = [] , []
        for i,x in enumerate(nums):
            if i >= k and window[0] <=i-k: 
                window.pop(0)   #discard the left element at the start of the queue
            while window and nums[ window[-1] ] <=x:
                window.pop()    #discard the right element at the end of the queue
            window.append(i)
            if i >= k-1:
                result.append(nums[window[0]])
        return result

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