// solution 1, brute force calculation.
// leetcode time     cost : 318 ms
// leetcode memory   cost : 38.5 MB 
// Time  Complexity: O(N*N)
// Space Complexity: O(1)
public class Solution {
    public int maxProfit(int prices[]) {
        int maxprofit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                if (profit > maxprofit)
                    maxprofit = profit;
            }
        }
        return maxprofit;
    }
}