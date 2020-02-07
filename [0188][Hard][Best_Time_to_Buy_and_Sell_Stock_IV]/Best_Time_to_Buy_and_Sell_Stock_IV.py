# solution 1, dp general solution.
# leetcode time     cost : 212 ms
# leetcode memory   cost : 24.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
import sys
class Solution:
    def maxProfit(self, K_max, prices) :
        if not prices:
            return 0
        n = len(prices)
        res = 0
        # 1 transaction consists of 1 buy and 1 sell, need at least 2 days, 
        # so for a effective constraint k_max, it must be smaller than n/2, otherwise k_max constraint will have no effect,
        # then it will be a infinity k_max, like problem 122.
        if (K_max > n//2):
            # also can use K_max = (n//2) to update K_max to a effective value.
            return self.maxProfit_k_inf(prices)
        profit = [[ [0 for _ in range(2)] for _ in range(K_max+1)] for _ in range(len(prices))] 

        # profit[i][k][j], i is the day, k is the transaction time, j is current holding status.
        # when k = any integer, i need to start from 0, initial value will be set in the loop k.
        for i in range(0,len(prices)):
            for k in range(1,K_max+1):
                if i == 0:
                   profit[i][k][0], profit[i][k][1] = 0, -prices[0] 
                   continue
                profit[i][k][1] = max(profit[i-1][k][1], profit[i-1][k-1][0] - prices[i]) 
                profit[i][k][0] = max(profit[i-1][k][0], profit[i-1][k][1] + prices[i]) 
     
        end = len(prices) - 1
        res = profit[end][K_max][0]
        return res 

    def maxProfit_k_inf(self, prices):
        print("maxProfit_k_inf is call")
        n = len(prices)
        dp_i_0 ,dp_i_1 =  0, -prices[0]
        for i in range(1,n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0; 

def main(): 
    k1 = 4   
    nums1 = [5,7,2,7,3,3,5,3,0] #expect is 9
    k2 = 2   
    nums1 = [3,2,6,5,0,3] #expect is 7    
    obj = Solution()
    result = obj.maxProfit(k1,nums1)
    print("return result is "+str(result));
    
if __name__ =='__main__':
    main() 