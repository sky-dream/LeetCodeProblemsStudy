// -*- coding: utf-8 -*- 
// leetcode time     cost : 12 ms
// leetcode memory   cost : 9 MB
// Time  Complexity: O(N*N!)
// Space Complexity: O(N*N!)
// solution 1,backtrack with swapping elements
/*
全排列的问题在题解和评论区主要有两种思路：
1. 使用 used[i] 布尔数组记录元素是否使用过；
2. 使用交换的方式，在深度优先遍历（回溯）的过程中生成。
*/
// https://leetcode-cn.com/problems/permutations-ii/solution/shuang-bai-si-lu-chao-ji-jian-ji-by-tai-yang-tian/
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
            if (nums[i] == nums[begin]) {
                break;
            }
            swap(nums[i], nums[begin]);
            generatePermutation(nums, begin + 1);
            swap(nums[i], nums[begin]);
        }
    }

public:
    vector<vector<int>> permuteUnique(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        generatePermutation(nums, 0);
        return res;
    }
};