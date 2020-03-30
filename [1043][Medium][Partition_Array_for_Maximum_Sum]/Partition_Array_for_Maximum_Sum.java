// leetcode time     cost : 8 ms
// leetcode memory   cost : 39.6 MB 
// Time  Complexity: O(A.length*K)
// Space Complexity: O(A.length)
// solution 1, DP
class Solution {
    public int maxSumAfterPartitioning(int[] A, int K) {
        int len = A.length;
        int[] dp = new int[len];
        for (int i = 0; i < len; i++) {
            /* 分别计算最后一段区间长度 j ∈[1, K]时的解，并更新位置i时的最优解 */
            int domainMax = A[i];
            for (int j = 1; j <= K && i - j + 1 >= 0; j++) {
                domainMax = Math.max(domainMax, A[i-j+1]);
                if (i - j >= 0) {
                    dp[i] = Math.max(dp[i], dp[i-j] + j*domainMax);
                } else {
                    dp[i] = Math.max(dp[i], j*domainMax);
                }
            }
        }
        return dp[len-1];
    }
}