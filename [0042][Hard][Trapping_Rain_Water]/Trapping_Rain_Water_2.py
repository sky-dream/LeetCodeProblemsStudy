# leetcode time     cost : 48 ms
# leetcode memory   cost : 14.2 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 2, loop with left_max, right_max memory
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max = [0]*size 
        right_max = [0]*size
        # init the memory
        left_max[0] = height[0]
        right_max[size - 1] = height[size - 1]

        for i in range(1,size):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(size-2,-1,-1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1,size):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans