// leetcode time     cost : 0 ms
// leetcode memory   cost : 36.2 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// slolution 3, DP
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}