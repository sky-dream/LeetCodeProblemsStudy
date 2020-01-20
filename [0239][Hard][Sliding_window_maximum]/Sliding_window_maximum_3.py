from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k > len(nums):
            return []
        if k == 1:
            return nums
        l = r = 0
        deck = deque([r])
        res = []
        while r < len(nums)-1:
            r += 1
            while deck and nums[deck[-1]] < nums[r]:
                deck.pop()
            deck.append(r)

            if r-l == k-1:
                res.append(nums[deck[0]])
                if l == deck[0]:
                    deck.popleft()
                l += 1
        return res

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