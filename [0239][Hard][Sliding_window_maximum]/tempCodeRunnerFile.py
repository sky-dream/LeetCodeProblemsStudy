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
            if i >k and window[0] <k-1: # note, need to note that it should not be i >=k, otherwise the left element will be pop unintentionally.
                window.pop(0)   #discard the left element at the start of the queue
            while window and nums[ window[-1] ] <=x:
                window.pop()    #discard the right element at the end of the queue
            window.append(i)
            if i >= k-1:
                result.append(nums[window[0]])
        return result