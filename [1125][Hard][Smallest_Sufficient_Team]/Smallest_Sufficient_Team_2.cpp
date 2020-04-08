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
                // skills[i]--->current person skill, kv.first is the skills combination, 
                // kv.second is the current in using people index list
                int new_skills = kv.first | skills[i];
                // skills combination new_skills not set, or use i to jump from kv.first to new_skills is better
                if (!tmp.count(new_skills) || kv.second.size() + 1 < tmp[new_skills].size())
                {
                    tmp[new_skills] = kv.second;
                    tmp[new_skills].push_back(i);
                }
            }
            tmp.swap(dp);
        }
        // return min people list for the requested skills combination
        return dp[(1 << n) - 1];
    }
};