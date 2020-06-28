// -*- coding: utf-8 -*- 
// leetcode time     cost : 4 ms
// leetcode memory   cost : 7.9 MB
// Time  Complexity: O(N*N!)
// Space Complexity: O(N*N!)
//https://leetcode-cn.com/problems/permutations-ii/solution/shuang-bai-si-lu-chao-ji-jian-ji-by-tai-yang-tian/
// solution 1,backtrack with swapping elements
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
private:
    vector<vector<int>> res;
    void generatePermutation(vector<int> &nums, int begin) {
        if (begin == nums.size()) {
            res.push_back(nums);
            return;
        }
        generatePermutation(nums, begin + 1);
        for (int i = 0; i < begin; i++) {
            swap(nums[i], nums[begin]);
            generatePermutation(nums, begin + 1);
            swap(nums[i], nums[begin]);
        }
    }
public:
    vector<vector<int>> permute(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        generatePermutation(nums, 0);
        return res;
    }
};