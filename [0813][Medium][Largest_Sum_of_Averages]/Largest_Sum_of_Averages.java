// leetcode time     cost : 9 ms
// leetcode memory   cost : 37.8 MB 
// Time  Complexity: O(N*N*K)
// Space Complexity: O(N*K)
// solution 1, DFS
class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        int n = A.length;
        /**
        dp[i][k]表示前i个数构成k个子数组时的最大平均值, 那么对于所有 0 <= j <= i-1
        dp[i][k] = Math.max(dp[i][k], dp[j][k-1] + (A[j+1] + ... + A[i+1]) / (i-j))
        **/
        double[][] dp = new double[n + 1][K + 1];
        double sum[] = new double[n + 1];
        for(int i = 1; i <= n; i++){
            sum[i] = sum[i - 1] + A[i - 1];
            dp[i][1] = sum[i] / i;
        }
        for(int i = 1; i <= n; i++){
            for(int k = 2; k <= K; k++){
                //由于要求每组非空，所以从k - 1开始
                for(int j = k - 1; j < i; j++){
                    dp[i][k] = Math.max(dp[i][k],dp[j][k - 1] + (sum[i] - sum[j]) / (i - j));
                }
            }
        }
        return dp[n][K];
    }
}