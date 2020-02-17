# solution 2, Binary Search,
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right