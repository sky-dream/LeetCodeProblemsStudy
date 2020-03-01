# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(n)
# solution 1 DP
class Solution:
    #def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, m, n):    # m is column number, n is the row number  
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # when not updated in this loop, cur[j] is the prev[j],
                cur[j] += cur[j-1]
        return cur[-1]


def main():
    m,n = 7,3       # expect is 28
    obj = Solution()
    result = obj.uniquePaths(m,n)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   