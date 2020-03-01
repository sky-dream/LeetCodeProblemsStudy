# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.3 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(2n)
# solution 1 DP
class Solution:
    #def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, m, n):    # m is column number, n is the row number  
        pre = [1] * n
        cur = [1] * n
        # only record previous row and current row data is enough
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

def main():
    m,n = 7,3       # expect is 28
    obj = Solution()
    result = obj.uniquePaths(m,n)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   