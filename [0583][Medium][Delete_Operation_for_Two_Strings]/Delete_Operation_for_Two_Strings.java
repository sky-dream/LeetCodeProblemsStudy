// leetcode time     cost : max time exceed
// leetcode memory   cost : -- MB 
// Time  Complexity: O(2**max(m,n))
// Space Complexity: O(max(m,n))
// solution 1, LCS,
class Solution {
    public int minDistance(String s1, String s2) {
        return s1.length() + s2.length() - 2 * lcs(s1, s2, s1.length(), s2.length());
    }
    public int lcs(String s1, String s2, int m, int n) {
        if (m == 0 || n == 0)
            return 0;
        if (s1.charAt(m - 1) == s2.charAt(n - 1))
            return 1 + lcs(s1, s2, m - 1, n - 1);
        else
            return Math.max(lcs(s1, s2, m, n - 1), lcs(s1, s2, m - 1, n));
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