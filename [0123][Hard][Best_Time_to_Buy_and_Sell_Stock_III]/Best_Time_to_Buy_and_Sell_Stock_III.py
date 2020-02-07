# solution 1, dp general solution.
# leetcode time     cost : 156 ms
# leetcode memory   cost : 24.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
import sys
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        res = 0
        K_max = 2
        profit = [[ [0 for _ in range(2)] for _ in range(K_max+1)] for _ in range(len(prices))]
        
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = 0, -prices[0] 
        profit[0][2][0], profit[0][2][1] = 0, -prices[0]    

        # profit[i][k][j], i is the day, k is the transaction time, j is current holding status.
        for i in range(1,len(prices)):
            for k in range(1,K_max+1):
                profit[i][k][1] = max(profit[i-1][k][1], profit[i-1][k-1][0] - prices[i]) 
                profit[i][k][0] = max(profit[i-1][k][0], profit[i-1][k][1] + prices[i]) 
     
        end = len(prices) - 1
        res = profit[end][2][0]

        return res

def main():    
    nums1 = [1,3,5,0,0,3,1,4] #expect is 8
    obj = Solution()
    result = obj.maxProfit(nums1)
    print("return result is "+str(result));
    
    nums2 = [1,4,2] #expect is 3
    result = obj.maxProfit(nums2)
    print("return result is "+str(result));
    
    nums3 = [3,2,6,5,0,3] #expect is 7
    result = obj.maxProfit(nums3)
    print("return result is "+str(result));    
    
if __name__ =='__main__':
    main() 