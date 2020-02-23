# -*- coding: utf-8 -*-  
# leetcode time     cost : 72 ms
# leetcode memory   cost : 14.4 MB
# solution 1, DP by iterate from the last 2nd row to the top row.
# 4 coding solutions as below.
# https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up).
class Solution:
    # O(n*n/2) space, top-down 
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
        
    # Modify the original triangle, top-down
    def minimumTotal_2(self, triangle):
        if not triangle:
            return 
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
        
    # Modify the original triangle, bottom-up
    def minimumTotal_3(self, triangle):
        if not triangle:
            return 
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal_4(self, triangle):
        if not triangle:
            return 
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0] 

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]        #expect is 11
    obj = Solution()
    result = obj.minimumTotal(triangle)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   