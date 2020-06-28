// -*- coding: utf-8 -*- 
// leetcode time     cost : 12 ms
// leetcode memory   cost : 8 MB
// Time  Complexity: O(N*N!)
// Space Complexity: O(N*N!)
//https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
// solution 1,backtrack with used notation
#include <iostream>
#include <vector>
#include <set>
#include <stdlib.h>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        permuteCore(nums);
        return results;
    }

    void permuteCore(vector<int>& nums) {
        if (used.size() == nums.size()) {  // 所有元素已被访问过
            results.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (used.find(nums[i]) == used.end()) {  // 当前元素未被访问时
                path.push_back(nums[i]);
                used.insert(nums[i]);
                permuteCore(nums);
                used.erase(nums[i]);
                path.pop_back();
            }
        }
    }

private:
    vector<int> path;  // 记录当前的排列
    set<int> used;  // 标记已在排列中的元素
    vector<vector<int>> results;  // 最终的结果
};