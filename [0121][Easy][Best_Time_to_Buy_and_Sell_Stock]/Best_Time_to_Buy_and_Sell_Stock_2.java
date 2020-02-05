// solution 2, calculation based on the price min valley and comeing with max peak.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 34.7 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}