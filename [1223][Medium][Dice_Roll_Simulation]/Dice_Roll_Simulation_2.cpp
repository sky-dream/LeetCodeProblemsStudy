// leetcode time     cost : 156 ms
// leetcode memory   cost : 7.1 MB 
// Time  Complexity: O(N*J*K)
// Space Complexity: O(N*J*K)
// solution 1, DP, 
#include <vector>
using namespace std;
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        const int divider = 1e9 + 7;
        vector<vector<int>> dp(7,vector<int>(16,0));
        for (int i = 1; i < 7; ++i) {
            dp[i][1] = 1;
        }
        vector<vector<int>> temp ;//暂时存储上一次投掷后的结果
        for (int i = 1; i < n; ++i) {
            temp = dp; 
            for (int j = 1; j < 7; ++j) {
                dp[j][1] = 0;
                for (int k = 1; k < 7; ++k) {
                    if (j != k) {
                        for (int t = 1; t <= rollMax[k-1]; ++t) {
                            dp[j][1] += temp[k][t];
                            dp[j][1] %= divider;
                        }
                    }
                    else {
                        for (int t = 1; t < rollMax[k-1]; ++t) {
                            dp[j][t + 1] = temp[k][t];
                        }
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 1; i < 7; ++i) {
            for (int t = 1; t <= rollMax[i-1]; ++t) {
                sum = (sum + dp[i][t]) % divider;
            }
        }
        return sum;

    }
};