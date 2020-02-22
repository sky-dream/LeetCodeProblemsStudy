# leetcode time     cost : 96 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n*k)
# Space Complexity: O(n)
# slolution 1, num_i &= (num_i -1)
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for num_i in range(num+1):
            count = 0
            while num_i:
                count+=1
                num_i &= (num_i -1)
            result.append(count)
        return result