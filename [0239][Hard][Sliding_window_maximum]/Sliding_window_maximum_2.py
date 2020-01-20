class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        # Find max number (maxN) in first k elements
        maxN = max(nums[:k])
        # Store maxN index as maxPos
        maxPos = nums[:k].index(maxN)
        ans = [maxN]
        i = k
        step = k - 1
        for i in range(k, len(nums)):
            # If new number > maxNum, store new maxN and maxPos
            if nums[i] > maxN:
                maxN, maxPos = nums[i], i
            # If window doesn't contain maxN anymore: i - step >= maxPos
            elif i - step >= maxPos:
                # Find new maxN and maxPos from what we currently have in the window
                arr = nums[i - step:i + 1]
                maxN = max(arr)
                maxPos = i - step + arr.index(maxN)
            # On each iteration add maxN to the answers
            ans.append(maxN)
        return ans

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