// leetcode time     cost : 876 ms
// leetcode memory   cost : 131.3 MB
// Time  Complexity: O(M * 2**N), M is the people number, N is the req skills number
// Space Complexity: O(M * 2**N)
// solution 2，dp with hash table
#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    vector<int> smallestSufficientTeam(vector<string> &req_skills, vector<vector<string>> &people)
    {
        const int n = req_skills.size();

        vector<int> skills;
        for (const auto &p : people)
        {
            int mask = 0;
            for (const string &s : p)
                mask |= (1 << find(begin(req_skills), end(req_skills), s) - begin(req_skills));
            skills.push_back(mask);
        }

        unordered_map<int, vector<int>> dp;
        dp[0] = {};

        for (int i = 0; i < people.size(); ++i)
        {
            unordered_map<int, vector<int>> tmp(dp);
            for (const auto &kv : dp)
            {
                int k = kv.first | skills[i];
                if (!tmp.count(k) || kv.second.size() + 1 < tmp[k].size())
                {
                    tmp[k] = kv.second;
                    tmp[k].push_back(i);
                }
            }
            tmp.swap(dp);
        }

        return dp[(1 << n) - 1];
    }
};