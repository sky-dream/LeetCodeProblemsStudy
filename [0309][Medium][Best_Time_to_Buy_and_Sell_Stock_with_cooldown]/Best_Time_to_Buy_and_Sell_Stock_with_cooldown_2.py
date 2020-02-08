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
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)
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