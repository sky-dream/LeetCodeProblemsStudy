# leetcode time     cost : 944 ms
# leetcode memory   cost : 20.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
from typing import List
# solution 1
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

def main():
    array,k = [2,2,2,1,2,2,1,2,2,2],2        # expect is 16
    obj = Solution()
    result = obj.numberOfSubarrays(array,k)
    try:
        assert result==16
        print("passed, result is follow expectation:",result)
    except AssertionError as aeeor:
        print('failed, result is wrong', aeeor.__str__())
    
    
if __name__ =='__main__':
    main() 