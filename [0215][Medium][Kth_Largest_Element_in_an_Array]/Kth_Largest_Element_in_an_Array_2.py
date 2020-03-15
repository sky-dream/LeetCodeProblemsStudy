# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N*KlogK)
# Space Complexity: O(1)
# solution 2, heap
import heapq
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        kLargest = [nums[0]]
        n = len(nums)
        # get a min heap
        heapq.heapify(kLargest)
        for i in range(1,n):
            if i<=(k-1):
                heapq.heappush(kLargest, nums[i])
            else: 
                tmp = heapq.heappop(kLargest)
                if tmp < nums[i]:
                    heapq.heappush(kLargest, nums[i])
                else:
                    heapq.heappush(kLargest, tmp)
        result =  heapq.heappop(kLargest) 
        return result

def main():
    array,k = [2,1,3,5,6,12,84,4],2      #expect is 12   
    obj = Solution()
    res = obj.findKthLargest(array,k)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 