# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.7 MB
# solution 1, 
# solution 2, bit operation
class Solution:
    def grayCode(self, n: int) -> [int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] ^ (1 << i))
        return res
    
def main():
    code = 2             #expect is [0,1,3,2]
    obj = Solution()
    result = obj.grayCode(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   