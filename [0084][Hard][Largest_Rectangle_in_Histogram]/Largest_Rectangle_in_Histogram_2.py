# -*- coding: utf-8 -*-  
# leetcode time     cost : 64 ms
# leetcode memory   cost : 15.4 MB
# solution 5, stack,
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, maxarea = [0], 0
        # loop i from 1 to len(heights),use the last 0 to pop all data in the stack
        for i in range(1,len(heights)):
            while stack and heights[stack[-1]] > heights[i]: 
                #print("in while,i: ",i,",height[i]: ",heights[i],",stack: ",stack)
                h = heights[stack.pop()]
                # after pop, the stack[-1] is the index before h in the stack
                w = i if not stack else i-stack[-1]-1 
                # (i−stack[top−1]−1) × heights[stack[top]]
                maxarea = max(maxarea, w*h)
            stack.append(i)
            print("in for i: ",i,",height[i]: ",heights[i],",stack: ",stack)
        return maxarea

def main():
    histogram = [2,1,5,6,2,3]  # expect is 10
    Solution_obj = Solution()
    result = Solution_obj.largestRectangleArea(histogram)
    print("result value is ",result)
    
if __name__ =='__main__':
    main() 