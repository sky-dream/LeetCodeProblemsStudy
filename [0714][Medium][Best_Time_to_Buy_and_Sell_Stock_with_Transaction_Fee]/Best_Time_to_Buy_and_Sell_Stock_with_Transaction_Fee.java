// solution 1, brute force calculation.
// leetcode time     cost : 7 ms
// leetcode memory   cost : 52.3 MB 
// Time  Complexity: O(N*N)
// Space Complexity: O(1)
class Solution {
    public int maxProfit(int prices[],int fee) {
        int n = prices.length;
        if (n == 0) 
            return 0;        
        int dp_pre_1_0 = 0 , dp_i_0 = 0, dp_i_1 = -prices[0];
        // need to pay attention to index i's start(0) point and end point(n-1).
        for (int i = 0; i < prices.length; i++) {
            dp_pre_1_0 = dp_i_0;     // represents dp[i-1][0]
            dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i] - fee);
            dp_i_1 = Math.max(dp_i_1, dp_pre_1_0 - prices[i]);
        }
        return dp_i_0;
    }
}

public class Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee {
    public static void main(String args[]) {
        int fee = 1;
        int prices[] = {1,3,5,0,0,3,1,4}; // #expect is 7 for fee =1
        int prices_2[] = {3,2,6,5,0,3}; // #expect is 5 for fee =1
        Solution Solution_obj = new Solution();
        int result = Solution_obj.maxProfit(prices,fee);
        System.out.println("In java code, 1st result is :" + result );
        int result2 = Solution_obj.maxProfit(prices_2,fee);
        System.out.println("In java code, 2nd result is "+ result2);
    }
}