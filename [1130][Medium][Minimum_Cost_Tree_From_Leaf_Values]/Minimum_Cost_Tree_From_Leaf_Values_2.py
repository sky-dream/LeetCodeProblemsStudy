from typing import List
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB 
# solution 2. stack.refer to leetcode 215
'''
这道题可以看做如下过程：在数组 arr 中，每次取相邻的两个数 a 和 b，然后去掉其中较小的一个，花费代价为 a * b，
求最终将数组消减为一个元素的最小代价。那么，要想获得最小代价，我们应该采取的策略是：
对于数组中的某一个数 a，分别向左和向右查询比它大的第一个数，在这两个数中选择较小的那个数把它消去，花费的代价最小。
这个过程我们可以用单调栈来一次遍历解决掉。
'''
class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
    
def main():
    arr = [6,2,4]        # expect is 32
    obj = Solution()
    result = obj.mctFromLeafValues(arr)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 