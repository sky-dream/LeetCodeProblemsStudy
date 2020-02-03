// solution 3, one time traversal based on solution 2.
// leetcode time     cost : 1 ms
// leetcode memory   cost : 37.3 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}