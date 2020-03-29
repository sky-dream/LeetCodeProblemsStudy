# leetcode time     cost : 292 ms
# leetcode memory   cost : 91.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, recursion
import sys
# Python 默认的递归深度不够，需要手动设置
sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)

def main():
    n, m = 5,9          #expect is 1
    Solution_obj = Solution()
    result = Solution_obj.lastRemaining(n, m)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  