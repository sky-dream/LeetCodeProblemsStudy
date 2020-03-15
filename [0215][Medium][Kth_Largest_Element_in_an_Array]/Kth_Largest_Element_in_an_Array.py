# leetcode time     cost : 168 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(N*KlogK)
# Space Complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            if len(kLargest)<k:
                kLargest.append(nums[i])
                kLargest.sort(reverse=True)
            elif len(kLargest)==k and kLargest[-1]<nums[i]:
                kLargest[-1] = nums[i]
                kLargest.sort(reverse=True)
        return kLargest[-1]

def main():
    array,k = [2,1,3,5,6,12,84,4],2      #expect is 12   
    obj = Solution()
    res = obj.findKthLargest(array,k)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 