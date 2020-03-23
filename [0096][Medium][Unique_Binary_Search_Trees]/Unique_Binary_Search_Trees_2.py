# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.5 MB
# solution 2, math
# G(n) = 卡塔兰数 C_n, C_0=1, C_(n+1) = 2*(2n+1)/(n+2) * C_(n+1)
class Solution(object):
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

def main():
    num = 3             #expect is 5
    obj = Solution()
    result = obj.numTrees(num)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   