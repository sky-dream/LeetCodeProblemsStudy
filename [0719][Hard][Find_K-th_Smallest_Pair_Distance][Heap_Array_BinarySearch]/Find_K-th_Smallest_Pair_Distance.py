# leetcode time     cost : over  due
# leetcode memory   cost : -- MB
# Time  Complexity: O((k+N)logN),K = N*N
# Space Complexity: O(N)
# solution 1, heap, time over due,
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1)
                for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap,(nums[nei + 1] - nums[root], root, nei + 1))

        return d
    
def main():
    nums = [1,3,1]; k = 1;expectRes = 0
    obj = Solution()
    result = obj.smallestDistancePair(nums, k)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ", expectRes)
    
if __name__ =='__main__':
    main() 