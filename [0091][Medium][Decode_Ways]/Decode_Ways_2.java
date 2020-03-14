// leetcode time     cost : 3 ms
// leetcode memory   cost : 38.3 MB
public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if(first >= 1 && first <= 9) {
               dp[i] += dp[i-1];  
            }
            if(second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}

public class Decode_Ways {
    public static void main(String args[]) {
        String word = "172426543102320";                     // #expect is 16
        Solution Solution_obj = new Solution();
        Boolean result = Solution_obj.numDecodings(board, word);
        System.out.println("return value is :" + (result));
    }
}