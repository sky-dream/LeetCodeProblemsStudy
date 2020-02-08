# solution 1, one time traversal of the price list.
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0        
        dp_i_0 ,dp_i_1 =  0, -prices[0]
        dp_pre_2_0 = 0;       # represents dp[i-2][0]
        for i in range(0,n):
            dp_pre_1_0 = dp_i_0     # represents dp[i-1][0]
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_2_0 - prices[i])
            dp_pre_2_0 = dp_pre_1_0
        return dp_i_0; 
'''  
when k = +infinity  
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
since k will not change, no need to record k,
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
'''
def main():  
    nums1 = [5,7,2,7,3,3,5,3,0] #expect is 9
    nums2 = [3,2,6,5,0,3] #expect is 7    
    obj = Solution()
    result = obj.maxProfit(nums2)
    print("return result is "+str(result));
    
if __name__ =='__main__':
    main() 