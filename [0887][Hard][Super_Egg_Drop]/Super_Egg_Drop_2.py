# -*- coding: utf-8 -*-  
# leetcode time     cost : 3880 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(K∗N)
# Space Complexity: O(N)
# solution 2, optimized DP
class Solution(object):
    def superEggDrop(self, K, N):

        # Right now, dp[i] represents dp(1, i)
        dp = range(N+1)

        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > \
                                max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2

        return dp[-1]


def main():
    K,N = 4,50      #expect is 6  
    obj = Solution()
    res = obj.superEggDrop(K,N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()