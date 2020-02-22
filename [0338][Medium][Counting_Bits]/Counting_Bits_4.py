# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# slolution 4, DP and lowest set bit,
# P(i)=P( i&(i-1) ) + 1, use x &= x - 1 to get the lowest set bit,
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0 for i in range(num+1)]
        for num_i in range(1,num+1):
            result[num_i] = result[num_i & (num_i - 1)] + 1
        return result