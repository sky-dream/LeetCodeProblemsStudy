// leetcode time     cost : 15 ms
// leetcode memory   cost : 40.5 MB 
// Time  Complexity: O(S*n), S is the needed money amount
// Space Complexity: O(S)
// slolution 3, Dynamic programming - Bottom up,loop money amount with recursion
public class Solution {
  public int coinChange(int[] coins, int amount) {
    int max = amount + 1;
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, max);
    dp[0] = 0;
    // loop the money amout in the outer iteration,then do the deeper recursion.
    for (int i = 1; i <= amount; i++) {
      for (int j = 0; j < coins.length; j++) {
        if (coins[j] <= i) {
          dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
        }
      }
    }
    return dp[amount] > amount ? -1 : dp[amount];
  }
}