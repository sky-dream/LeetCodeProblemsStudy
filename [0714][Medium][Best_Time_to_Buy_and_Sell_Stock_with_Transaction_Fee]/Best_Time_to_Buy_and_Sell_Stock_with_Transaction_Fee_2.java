// solution 1, brute force calculation.
// leetcode time     cost : 6 ms
// leetcode memory   cost : 51.8 MB 
// Time  Complexity: O(N*N)
// Space Complexity: O(1)
class Solution {
    public int maxProfit(int prices[],int fee) {
        int free = 0;
        int have = -prices[0];
        
        for(int i = 0; i < prices.length; i++) {            
            free = Math.max(free, have + prices[i] - fee);
            have = Math.max(have, free - prices[i]);
        }
        
        return free;
    }
}

public class Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee_2 {
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