# -*- coding: utf-8 -*-  
# Time  Complexity: O(n**2)
# Space Complexity: O(n)
# solution 1, extention of 2sum, use collections.defaultdict(int).
from typing import List
import collections
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lookup = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                lookup[a+b] += 1
        for c in C:
            for d in D:
                res += lookup[-(c + d)]
        return res

def main():
    A = [0,1,-1]
    B = [-1,1,0]
    C = [0,0,1]
    D = [-1,1,1]
    obj = Solution()
    res = obj.fourSumCount(A,B,C,D) # Expect is 17
    print("return value is ",res)
    
if __name__ =='__main__':
    main() 