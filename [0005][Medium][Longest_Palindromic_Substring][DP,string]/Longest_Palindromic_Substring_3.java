// leetcode time     cost : 153 ms
// leetcode memory   cost : 42.9 MB
// Time  Complexity: O(n**2)
// Space Complexity: O(n)
// solution 2, DP
public class Solution {
    public String longestPalindrome(String s) {
    int n = s.length();
    String res = "";
        
    boolean[][] dp = new boolean[n][n];
        
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
        dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
                
        if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
            res = s.substring(i, j + 1);
        }
        }
    }
        
    return res;
    }
}