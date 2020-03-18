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
        def fun(t,k):
            if (t == 1 or k == 1): 
                return (t + 1)
            return fun(k - 1, t - 1) + fun(k, t- 1)
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