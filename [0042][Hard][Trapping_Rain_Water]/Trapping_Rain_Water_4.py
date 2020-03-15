# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 4, double index pointer
"""              top
              __
            _/  \       __
     __    /     \     /  \
_   /  \__/       \___/    \     __
 \_/                        \___/      """
class Solution:
    def trap(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        left_max = right_max = 0
        # left_max is max value  in  height[0,    left]
        # right_max is max value  in height[right, n-1]
        while (left < right):
            left_max = max(left_max, height[left])
            right_max =  max(right_max, height[right])

            if (left_max < right_max):
                ans += (left_max - height[left])
                left +=1            
            else:
                ans += right_max - height[right]
                right -=1   
        return ans