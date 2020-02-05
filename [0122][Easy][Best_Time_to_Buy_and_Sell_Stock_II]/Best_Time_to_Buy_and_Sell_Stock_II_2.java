// solution 2, calculation based on the price peak and valley.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 37.6 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) 
            return 0;
        int i = 0;
        int valley = prices[0];
        int peak = prices[0];
        int maxprofit = 0;
        while (i < prices.length - 1) {
            while (i < prices.length - 1 && prices[i] >= prices[i + 1])
                i++;
            valley = prices[i];
            while (i < prices.length - 1 && prices[i] <= prices[i + 1])
                i++;
            peak = prices[i];
            maxprofit += peak - valley;
        }
        return maxprofit;
    }
}