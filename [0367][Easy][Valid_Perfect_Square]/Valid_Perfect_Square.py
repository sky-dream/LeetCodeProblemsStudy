# solution 2, Binary Search, pls refer to No.69
# leetcode time     cost : 92 ms
# leetcode memory   cost : 29.1 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False 