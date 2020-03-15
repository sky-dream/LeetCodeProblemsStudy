# leetcode time     cost : time exceeded
# leetcode memory   cost : time exceeded
# Time  Complexity: O(N*N)
# Space Complexity: O(1)
# solution 1, brute force
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(1,n):
            max_left, max_right = 0, 0
            for j in range(i,-1,-1): #Search the left part for max bar size
                max_left = max(max_left, height[j])
            for j in range(i,n): #Search the right part for max bar size
                max_right = max(max_right, height[j])            
            ans += min(max_left, max_right) - height[i]        
        return ans