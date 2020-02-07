// solution 1, dp with dp compacted.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 36.7 MB 
// Time  Complexity: O(kN)
// Space Complexity: O(k+N)
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int dp[] = new int[3];
        int cost[] = new int[3];
        Arrays.fill(cost, prices[0]);         //init all min elements with the value of the start price, price[0],
        for (int i = 1; i < prices.length; i++)  {
            for (int k = 1; k <= 2; k++) {
                cost[k] = Math.min(cost[k], prices[i] - dp[k-1]);
                dp[k] = Math.max(dp[k], prices[i] - cost[k]);
            }
        }
        return dp[2];
    }
}