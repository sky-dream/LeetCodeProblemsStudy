# -*- coding: utf-8 -*-  
# leetcode time     cost : max recursion depth exceed
# leetcode memory   cost : --
# Time  Complexity: O(K∗NlogN)
# Space Complexity: O(K∗N)
# solution 1, bynary search and DP
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def dfs(i, j):
            if i==1:
                return j
            if j==0:
                return 0
            if j==1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            while lo < hi:
                mid = (lo+hi)/2
                left, right = dfs(i-1, mid-1), dfs(i, j-mid)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            res = 1 + max(dfs(i-1, lo-1), dfs(i, j-lo))
            d[i, j]=res
            return res
        
        d={}
        return dfs(K, N)


def main():
    K,N = 2,10      #expect is 6  
    obj = Solution()
    res = obj.superEggDrop(K,N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 