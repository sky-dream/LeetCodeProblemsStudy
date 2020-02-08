# solution 2, one time traversal of the price list.
# leetcode time     cost : 920 ms
# leetcode memory   cost : 20 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices,fee):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0        
        dp_i_0 ,dp_i_1 =  0, -prices[0]     #or dp_i_0 ,dp_i_1 =  0, -prices[0]-fee
        for i in range(0,n):
            dp_pre_1_0 = dp_i_0     # represents dp[i-1][0]
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]-fee)
            dp_i_1 = max(dp_i_1, dp_pre_1_0 - prices[i] )
            # or dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # or dp_i_1 = max(dp_i_1, dp_pre_1_0 - prices[i]-fee )            
        return dp_i_0; 

def main():  
    nums1 = [5,7,2,7,3,3,5,3,0] #expect is 6 for fee =1
    nums2 = [3,2,6,5,0,3] #expect is 5 for fee =1
    fee = 1    
    obj = Solution()
    result = obj.maxProfit(nums2,fee)
    print("return result is "+str(result));
    
if __name__ =='__main__':
    main() 