# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(K∗logN)
# Space Complexity: O(1)
# solution 3, based on math analysis
class Solution(object):
    def superEggDrop(self, K, N):
        # 计算 K 个鸡蛋，扔 T 次，可以覆盖多少个区间
        # 通过递归计算
        floorX = [[0]*(N+1) for _ in range(K+1)]
        def fun(t,k):
            if (k >=1 and t==1): 
                return 1             
            if (t >=1 and k==1): 
                return t 
            #print("k,",k,",t,",t,"floorX[k][t]",floorX[k][t])
            if not floorX[k][t]:   
                floorX[k][t] = 1 + fun(t - 1, k - 1) + fun(t-1, k)     
            return floorX[k][t]
        # 通过数学传递函数计算
        def fun_1(x,k):
            ans = 0
            r = 1
            for i in range(1, k+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans
        # 最小drop次数在[1, N]范围内，可覆盖楼层与次数t为单调递增关系，由二分法可以加速求解
        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if fun(mi,K) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo


def main():
    K,N = 4,50      #expect is 6  
    obj = Solution()
    res = obj.superEggDrop(K,N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()