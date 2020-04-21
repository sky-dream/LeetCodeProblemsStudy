# leetcode time     cost : 944 ms
# leetcode memory   cost : 20.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
from typing import List
# solution 2
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
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