// solution 1, dp with general solution.
// leetcode time     cost : 4 ms
// leetcode memory   cost : 40.6 MB 
// Time  Complexity: O(kN)
// Space Complexity: O(k+N)

import java.util.Arrays;
class Solution {
    public int maxProfit(int[] prices) {
        int max_k = 2;
        int n = prices.length;
        if (n == 0) 
            return 0;
        int dp[][][] = new int[n][max_k + 1][2];
        for (int i = 0; i < n; i++) {
            for (int k = max_k; k >= 1; k--) {
                if (i == 0) { 
                    dp[i][k][0]  = Math.max(0, Integer.MIN_VALUE + prices[i]) ;     //dp[i][k][0]  = 0;
                    dp[i][k][1]  = Math.max(Integer.MIN_VALUE, 0 - prices[i]) ;     //dp[i][k][0]  = - prices[0];
                    continue;
                }
                dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
            }
        }
        // enumerate n × max_k × 2 status.
        return dp[n - 1][max_k][0];
    }
}

public class Best_Time_to_Buy_and_Sell_Stock_III {
    public static void main(String args[]) {
        int prices[] = {1,3,5,0,0,3,1,4}; // #expect is 8
        int prices_2[] = {3,2,6,5,0,3}; // #expect is 7
        Solution Solution_obj = new Solution();
        int result = Solution_obj.maxProfit(prices);
        int result2 = Solution_obj.maxProfit(prices_2);
        System.out.println("In java code, 1st result is :" + result + ", 2nd result is "+ result2);
    }
}