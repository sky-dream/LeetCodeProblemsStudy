# solution 4, Integer Newton,pls refer to No.69
# leetcode time     cost : 100 ms
# leetcode memory   cost : 28.1 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num