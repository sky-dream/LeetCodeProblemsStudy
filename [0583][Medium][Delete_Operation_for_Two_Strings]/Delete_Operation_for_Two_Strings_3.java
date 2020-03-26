// leetcode time     cost : 11 ms
// leetcode memory   cost : 41 MB 
// Time  Complexity: O(m*n)
// Space Complexity: O(m*n)
// solution 3, DP with LCS,
public class Solution {
    public int minDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0 || j == 0)
                    continue;
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return s1.length() + s2.length() - 2 * dp[s1.length()][s2.length()];
    }
}


public class Delete_Operation_for_Two_Strings {
    public static void main(String args[]) {
        String word1 = "aeaswqsdaf"; 
        String word2="befdswerw" ;// expect is 13,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.minDistance(word1,word2);
        System.out.println("In java code,result is :" + result);
    }
}