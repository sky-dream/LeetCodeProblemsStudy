# solution 1, bit manipulation, xor
# leetcode time     cost : 32 ms
# leetcode memory   cost : 15.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# a^0 = a, a^a = 0, a ^ b ^ c = a ^ c ^ b,
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number