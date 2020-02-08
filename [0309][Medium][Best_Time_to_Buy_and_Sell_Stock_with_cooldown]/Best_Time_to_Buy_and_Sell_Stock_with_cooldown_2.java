// solution 1, brute force calculation.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 35.9 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
import java.math.*;
class Solution {
    public int maxProfit(int[] prices) {
        
        int free = 0;
        int have = Integer.MIN_VALUE;
        int cool = Integer.MIN_VALUE;
        
        for(int i = 0; i < prices.length; i++) {
            
            int freeToday = free;
            int coolToday = cool;
            int haveToday = have;
            
            free = Math.max(freeToday, coolToday);
            have = Math.max(haveToday, freeToday - prices[i]);
            cool = haveToday + prices[i];
        }
        
        return Math.max(free, cool);
    }
}

public class Best_Time_to_Buy_and_Sell_Stock_with_cooldown {
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