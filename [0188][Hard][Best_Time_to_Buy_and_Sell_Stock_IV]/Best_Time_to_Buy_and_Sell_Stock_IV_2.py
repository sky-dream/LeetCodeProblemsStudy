# solution 2, DP with status compress
# leetcode time     cost : 112 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, K_max, prices):
        if len(prices) <= 1: return 0
        if (K_max < len(prices) // 2) :
            # dp[k][j], j =0 is sell or not buy, j =i is buy or hold stock.
            dp = [[0, -prices[0]] for i in range(K_max+1)]
            # price is the daily stock price
            for price in prices[1:]:
                # k is the transaction times.
                for k in range(1, K_max+1):
                    dp[k] = [max(dp[k][0], dp[k][1]+price), max(dp[k][1], dp[k-1][0]-price)]
            return dp[K_max][0]
        else:
            dp = [-prices[0], 0]
            for price in prices[1:]:
                dp = [max(dp[0], dp[1]-price), max(dp[1], dp[0]+price)]
            return dp[1]
        
def main(): 
    k1 = 4   
    nums1 = [5,7,2,7,3,3,5,3,0] #expect is 9
    k2 = 2   
    nums2 = [3,2,6,5,0,3] #expect is 7    
    obj = Solution()
    result = obj.maxProfit(k2,nums2)
    print("return result is "+str(result));
    
if __name__ =='__main__':
    main() 