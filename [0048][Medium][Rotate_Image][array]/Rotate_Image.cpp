// -*- coding: utf-8 -*- 
// leetcode time     cost : 4 ms
// leetcode memory   cost : 7.1 MB
// Time  Complexity: O(n*n)
// Space Complexity: O(1)
// solution 3, swap 4 rectangles in the loop once
#include <stdlib.h>
#include <vector>
using namespace std;
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i = 0; i < (n >> 1); ++i){
            for(int j = i; j < n - 1 - i; ++j){
                swap(matrix[i][j], matrix[j][n - 1 - i]);
                swap(matrix[i][j], matrix[n - 1 - i][n - 1 - j]);
                swap(matrix[i][j], matrix[n - 1 - j][i]);
            }
        }
    }
};