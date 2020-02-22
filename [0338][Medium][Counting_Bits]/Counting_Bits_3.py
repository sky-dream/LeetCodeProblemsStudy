# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.3 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# slolution 3, DP and lowest effective bit,
# P(i)=P(i/2) + (i % 2), (i % 2)--->(i & 1)
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0 for i in range(num+1)]
        for num_i in range(num+1):
            result[num_i] = result[num_i>>1] + (num_i & 1)
        return result