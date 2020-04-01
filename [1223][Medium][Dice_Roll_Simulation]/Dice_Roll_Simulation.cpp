// leetcode time     cost : 304 ms
// leetcode memory   cost : 34.3 MB 
// Time  Complexity: O(N*J*K)
// Space Complexity: O(N*J*K)
// solution 1, DP, 
#include <vector>
using namespace std;
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        const int divider = 1e9 + 7;
        vector<vector<vector<int>>> dp(n,vector<vector<int>>(7,vector<int>(16,0)));//与用三维数组同理
        for (int i = 1; i < 7; ++i) {
            dp[0][i][1] = 1;
        }
        for (int i = 1; i < n; ++i) {//第i + 1次投掷
            for (int j = 1; j < 7; ++j) {//出现的点数为j
                for (int k = 1; k < 7; ++k) {//上一次出现的点数为k
                    if (j != k) {
                        for (int t = 1; t <= rollMax[k-1]; ++t) {
                            dp[i][j][1] += dp[i - 1][k][t];
                            dp[i][j][1] %= divider;
                        }
                    }
                    else {
                        for (int t = 1; t < rollMax[k-1]; ++t) {
                            dp[i][j][t + 1] += dp[i - 1][k][t];
                            dp[i][j][t + 1] %= divider;
                        }
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 1; i < 7; ++i) {
            for (int t = 1; t <= rollMax[i-1]; ++t) {
                sum = (sum + dp[n - 1][i][t]) % divider;
            }
        }
        return sum;

    }
};