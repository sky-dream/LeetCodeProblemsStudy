// solution 2, DP with status compress
// leetcode time     cost : 8 ms
// leetcode memory   cost : 9.4 MB 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.size() < 2 || k < 1) return 0;
        int N = prices.size();
        if (k >= N / 2) {
            int res = 0;
            for (int i = 1; i < N; ++i) {
                if (prices[i] > prices[i - 1]) {
                    res += prices[i] - prices[i - 1];
                }
            }
            return res;
        }
        vector<vector<int> > dp(k + 1, vector<int>{0, INT_MIN});
        for (int i = 0; i < N; ++i) {
            for (int j = k; j > 0; --j) {
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i]);
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i]);
            }
        }
        return dp[k][0];
    }
};