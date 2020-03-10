# -*- coding: utf-8 -*-  
# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.2 MB
# solution 5, stack,
class Solution:
    #def largestRectangleArea(self, heights: List[int]) -> int:
    def largestRectangleArea(self, heights):    
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                print("i: ",i,",height[i]: ",heights[i],",stack: ",stack)
                # after pop, the stack[-1] is the index before heights[stack.pop()] in the stack
                # (i−stack[top−1]−1) × heights[stack[top]]
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            print("stack: ",stack)
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea   

def main():
    histogram = [2,1,5,6,2,3]  # expect is 10
    Solution_obj = Solution()
    result = Solution_obj.largestRectangleArea(histogram)
    print("result value is ",result)
    
if __name__ =='__main__':
    main() 