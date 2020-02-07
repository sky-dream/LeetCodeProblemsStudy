// solution 1, dp simplified version.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 34.7 MB 
// Time  Complexity: O(kN)
// Space Complexity: O(k+N)
class Solution {
    public int maxProfit(int[] prices) { 
        if (prices == null || prices.length <= 1) {
             return 0;
         }
        int cost_1 = Integer.MAX_VALUE, cost_2 = Integer.MAX_VALUE, profit_1 = 0, profit_2 = 0;
        for (int price : prices){
            cost_1 = Math.min(cost_1, price);
            profit_1 = Math.max(profit_1, price - cost_1);
            cost_2 = Math.min(cost_2, price - profit_1);
            profit_2 = Math.max(profit_2, price - cost_2);
        }
        return profit_2;
    }

    //a another similar solution.
    public int maxProfit_2(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for(int i:prices){                              // Assume we only have 0 money at first
            release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
            hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
            release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
            hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far. 
        }
        return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}