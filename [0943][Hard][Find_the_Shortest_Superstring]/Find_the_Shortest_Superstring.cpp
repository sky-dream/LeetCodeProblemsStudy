// leetcode time     cost : 1560 ms
// leetcode memory   cost : 8.8 MB
// Time complexity: O(n!)
// Space complexity: O(n)
// Solution 1: Search + Pruning
// Author: https://zxi.mytechroad.com/blog/searching/leetcode-943-find-the-shortest-superstring/
#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
  string shortestSuperstring(vector<string>& A) {    
    const int n = A.size();
    cost = vector<vector<int>>(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        cost[i][j] = A[j].length();
        for (int k = 1; k <= min(A[i].length(), A[j].length()); ++k)
          if (A[i].substr(A[i].size() - k) == A[j].substr(0, k))            
            cost[i][j] = A[j].length() - k;
      }
    vector<int> path(n);
    best_len_ = INT_MAX;
    dfs(A, 0, 0, 0, path);    
    string ans = A[best_path_[0]];
    for (int k = 1; k < best_path_.size(); ++k) {
      int i = best_path_[k - 1];
      int j = best_path_[k];
      ans += A[j].substr(A[j].length() - cost[i][j]);
    }
    return ans;
  }
private:
  vector<vector<int>> cost;
  vector<int> best_path_;
  int best_len_;
  void dfs(const vector<string>& A, int d, int used, int cur_len, vector<int>& path) {
    if (cur_len >= best_len_) return;
    if (d == A.size()) {
      best_len_ = cur_len;
      best_path_ = path;
      return;
    }
    
    for (int i = 0; i < A.size(); ++i) {
      if (used & (1 << i)) continue;      
      path[d] = i;
      dfs(A,
          d + 1, 
          used | (1 << i),
          d == 0 ? A[i].length() : cur_len + cost[path[d - 1]][i],
          path);
    }
  }
};