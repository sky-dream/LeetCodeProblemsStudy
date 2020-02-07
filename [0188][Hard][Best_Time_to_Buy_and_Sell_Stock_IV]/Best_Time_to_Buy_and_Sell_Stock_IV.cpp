// solution 1, dp with general solution.
// leetcode time     cost : 8 ms
// leetcode memory   cost : 9.2 MB 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.size() <= 1) return 0;
        //std::vector<std::pair<int, int>> dp(k+1, {-prices[0], 0});
        // there is a hidden bug, if the value of k is very big, the stack will be overflowed.
        // so the value of k need to be optimized,  vector is declared in the if statement
        if (k < prices.size() / 2)  {
                std::vector<std::pair<int, int>> dp(k+1, {-prices[0], 0});
                for(int i=1;i<prices.size();i++)
                {
                    for(int j=1; j < k+1; j++)
                    {
                        int hold = std::max(dp[j].first, dp[j-1].second-prices[i]);
                        int not_hold = std::max(dp[j].second, dp[j].first+prices[i]);
                        dp[j].first = hold; dp[j].second = not_hold;
                    }
                }
            return dp[k].second; //max(dp[k].first, dp[k].second);
        } else  {
            std::pair<int, int> dp = {-prices[0], 0};
            for (int i=1; i<prices.size(); i++) {
                int hold = std::max(dp.first, dp.second-prices[i]);
                int not_hold = std::max(dp.second, dp.first+prices[i]);
                dp.first = hold; dp.second = not_hold;
            }
            return dp.second;
        }
    }
};