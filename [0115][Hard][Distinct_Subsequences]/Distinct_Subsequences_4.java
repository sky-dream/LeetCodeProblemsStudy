// leetcode time     cost : 7 ms
// leetcode memory   cost : 37.4 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(M)
// solution 3, DP from right to left with space optimization
class Solution {
    public int numDistinct(String s, String t) {
        int s_len = s.length();
        int t_len = t.length();
        int[]dp = new int[s_len + 1];
        for (int i = 0; i <= s_len; i++) {
            dp[i] = 1;
        }
    //倒着进行，T 每次增加一个字母
        for (int t_i = t_len - 1; t_i >= 0; t_i--) {
            int pre = dp[s_len];
            dp[s_len] = 0; 
            //倒着进行，S 每次增加一个字母
            for (int s_i = s_len - 1; s_i >= 0; s_i--) {
                int temp = dp[s_i];
                if (t.charAt(t_i) == s.charAt(s_i)) {
                    dp[s_i] = dp[s_i + 1] + pre;
                } else {
                    dp[s_i] = dp[s_i + 1];
                }
                pre = temp;
            }
        }
        return dp[0];
    }
}