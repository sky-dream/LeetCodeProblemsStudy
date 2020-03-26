// leetcode time     cost : 73 ms
// leetcode memory   cost : 41.6 MB 
// Time  Complexity: O(m*n)
// Space Complexity: O(m*n)
// solution 2, LCS with memo,
public class Solution {
    public int minDistance(String s1, String s2) {
        int[][] memo = new int[s1.length() + 1][s2.length() + 1];
        return s1.length() + s2.length() - 2 * lcs(s1, s2, s1.length(), s2.length(), memo);
    }
    public int lcs(String s1, String s2, int m, int n, int[][] memo) {
        if (m == 0 || n == 0)
            return 0;
        if (memo[m][n] > 0)
            return memo[m][n];
        if (s1.charAt(m - 1) == s2.charAt(n - 1))
            memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo);
        else
            memo[m][n] = Math.max(lcs(s1, s2, m, n - 1, memo), lcs(s1, s2, m - 1, n, memo));
        return memo[m][n];
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