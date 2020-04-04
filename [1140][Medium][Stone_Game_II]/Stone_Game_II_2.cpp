// leetcode time     cost : 8 ms
// leetcode memory   cost : 7.5 MB
// solution 2. dp
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int len = piles.size();
        int sum = 0; 
        // dp[i][j]表示当前是第i波，m = j;
        vector<vector<int>>dp(len + 1, vector<int>(len + 1, 0));
        for(int i = len - 1; i >= 0; i--){
            sum += piles[i];// 表示当前所剩下的所有棋子的和
            for(int M = 1; M <= len; M++){
                if(i + 2 * M >= len){
                    dp[i][M] = sum;
                    continue;
                }
                for(int x = 1; i + x <= len && x <= 2 * M; x++){
                    dp[i][M] = max(dp[i][M], sum - dp[i + x][max(M, x)]);
                }
            }
        }
        return dp[0][1];
    }
};
