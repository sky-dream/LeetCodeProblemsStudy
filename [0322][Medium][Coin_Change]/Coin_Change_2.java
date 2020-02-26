// leetcode time     cost : 43 ms
// leetcode memory   cost : 41 MB 
// Time  Complexity: O(S*n), S is the needed money amount
// Space Complexity: O(S)
// https://leetcode-cn.com/problems/coin-change/solution/ling-qian-dui-huan-by-leetcode/
// slolution 2, Dynamic programming - Top down,loop coin with recursion
public class Solution {

    public int coinChange(int[] coins, int amount) {
      if (amount < 1) return 0;
      return coinChange(coins, amount, new int[amount]);
    }
  
    private int coinChange(int[] coins, int rem, int[] count) {
      if (rem < 0) return -1;
      if (rem == 0) return 0;
      if (count[rem - 1] != 0) return count[rem - 1];
      int min = Integer.MAX_VALUE;
      // loop the all possible coin in the outer iteration,then do the deeper recursion.
      for (int coin : coins) {
        int res = coinChange(coins, rem - coin, count);
        if (res >= 0 && res < min)
          min = 1 + res;
      }
      count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
      return count[rem - 1];
    }
}