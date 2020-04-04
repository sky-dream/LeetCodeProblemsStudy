// leetcode time     cost : 48 ms
// leetcode memory   cost : 7.3 MB
// solution 2. dp
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    // dp[i][j] = max{sums[N] - sums[i] - dp[i - k][max(k, j)]} (1 <= k <= 2 * j)
    int stoneGameII(vector<int>& piles) {
        int N = piles.size();
        vector<int> sums(N + 1, 0);
        for (int i = 0; i < N; ++i) {
            sums[i + 1] = sums[i] + piles[i];
        }
        vector<vector<int> > dp(N + 1, vector<int>(N + 1, 0));
        for (int i = 0; i <= N; ++i) {
            for (int j = i; j <= N; ++j) {
                dp[i][j] = sums[N] - sums[N - i];
            }
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                for (int k = 1; k <= 2 * j && k <= i; ++k) {
                    dp[i][j] = max(dp[i][j], sums[N] - sums[N - i] - dp[i - k][min(max(k, j), N)]);
                }
            }
        }
        return dp[N][1];
    }
};