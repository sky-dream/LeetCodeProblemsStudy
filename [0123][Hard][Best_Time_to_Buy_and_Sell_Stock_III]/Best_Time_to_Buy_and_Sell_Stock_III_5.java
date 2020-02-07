// solution 1, dp .
// leetcode time     cost : 2 ms
// leetcode memory   cost : 37.5 MB 
// Time  Complexity: O(kN)
// Space Complexity: O(k+N)
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int dp[][] = new int[3][prices.length];
        int min[] = new int[3];
        Arrays.fill(min, prices[0]);        //init all min elements with the value of the start price, price[0],
        for (int i = 1; i < prices.length; i++) {
            for (int k = 1; k <= 2; k++) {
                min[k] = Math.min(min[k], prices[i] - dp[k-1][ i-1]);
                dp[k][ i] = Math.max(dp[k][ i-1], prices[i] - min[k]);
            }
        }
        return dp[2][ prices.length - 1];
    }
}