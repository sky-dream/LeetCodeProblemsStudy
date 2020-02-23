# -*- coding: utf-8 -*-  
# leetcode time     cost : 72 ms
# leetcode memory   cost : 14.4 MB
# solution 1, DP by iterate from the last 2nd row to the top row.
# 6 coding solutions as below.
# https://leetcode.com/problems/triangle/discuss/38827/One-liner-in-Python
from functools import reduce
# reduce(function, iterable[, initializer])
class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    def minimumTotal(self, t):
        return reduce(lambda a,b:[f+min(d,e)for d,e,f in zip(a,a[1:],b)],t[::-1])[0]
    
    def minimumTotal_2(self, triangle):
        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_right)
                    for upper, lower_left, lower_right in
                    zip(upper_row, lower_row, lower_row[1:])]
        return reduce(combine_rows, triangle[::-1])[0]
    
    def minimumTotal_3(self, triangle):
        return reduce(lambda a, b:[min(a[i], a[i+1])+n for i, n in enumerate(b)], triangle[::-1])[0]
    
    def minimumTotal_4(self, triangle):
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0] 

    def minimumTotal_5(self, triangle):
        return min(reduce(lambda a, b: [c+min(d,e) for c,d,e in zip(b,['']+a,a+[''])], triangle, [0])) 
    
    def minimumTotal_6(self, triangle):
        r = [0]
        for row in triangle:
            r = [row[i] + min (r[max(i-1,0)], r[min(i,len(r)-1)]) for i in range(len(row))]
        return min(r)  

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]        #expect is 11
    obj = Solution()
    result = obj.minimumTotal(triangle)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   