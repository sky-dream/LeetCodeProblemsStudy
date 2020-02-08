// solution 1, brute force calculation.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 35.9 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
import java.math.*;
class Solution {
    //buy[i] = Math.max(buy[i - 1], sell[i - 2] - prices[i]);   
    //sell[i] = Math.max(sell[i - 1], buy[i - 1] + prices[i]); 
    //buy_pre_2, buy_pre_1, buy_i represent buy[i - 2], buy[i - 1], buy[i]
    //sell_pre_2, sell_pre_1, sell_i represent sell[i - 2], sell[i - 1], sell[i]       
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length <= 1) return 0;
      
        int buy_i = -prices[0], buy_pre_1 = buy_i;
        int sell_i = 0, sell_pre_1 = 0, sell_pre_2 = 0;
     
        for(int i = 1; i < prices.length; i++) {
            buy_i = Math.max(buy_pre_1, sell_pre_2 - prices[i]);
            sell_i = Math.max(sell_pre_1, buy_pre_1 + prices[i]);
            buy_pre_1 = buy_i; sell_pre_2 = sell_pre_1; sell_pre_1 = sell_i; 
        }
        return sell_i;
    }
}

public class Best_Time_to_Buy_and_Sell_Stock_with_cooldown_3 {
    public static void main(String args[]) {
        int prices[] = {1,3,5,0,0,3,1,4}; // #expect is 8
        int prices_2[] = {3,2,6,5,0,3}; // #expect is 7
        Solution Solution_obj = new Solution();
        int result = Solution_obj.maxProfit(prices);
        System.out.println("In java code, 1st result is :" + result );
        int result2 = Solution_obj.maxProfit(prices_2);
        System.out.println("In java code, 2nd result is "+ result2);
    }
}