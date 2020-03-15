# leetcode time     cost : 68 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 3, decreasing stack, refer to No.84,85
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for current in range(0,len(height)):
            # pop out if current height is bigger than the top one in stack
            while ((len(stack)>0) and height[current] > height[stack[-1]]):
                # pop out last one in the stack
                top = stack.pop(-1)           
                if len(stack)==0:
                    break
                # for the top, l_max is the 2nd last one in the stack, r_max is the just met current height.
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height           
            stack.append(current)
            #print("index ", current,"stack ",stack)        
        return ans