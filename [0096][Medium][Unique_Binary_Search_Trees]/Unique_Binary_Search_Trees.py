# -*- coding: utf-8 -*-  
# leetcode time     cost : 28 ms
# leetcode memory   cost : 13.5 MB
# solution 1,DP
# G(n)= sum [G(i−1)⋅G(n−i)],
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

def main():
    num = 3             #expect is 5
    obj = Solution()
    result = obj.numTrees(num)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   