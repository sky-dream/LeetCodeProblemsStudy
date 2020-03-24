# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB
# solution 1, 
class Solution:
    def grayCode(self, n: int) -> [int]:
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        return res
    
def main():
    code = 2             #expect is [0,1,3,2]
    obj = Solution()
    result = obj.grayCode(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   