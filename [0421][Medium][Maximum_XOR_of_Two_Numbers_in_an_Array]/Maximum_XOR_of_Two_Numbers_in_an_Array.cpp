// leetcode time     cost : 112 ms
// leetcode memory   cost : 27.6 MB 
#include<bits\stdc++.h> 
using namespace std; 
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int res = 0;
        unordered_set<int> pre;
        for (int i = 31; i >= 0; i--) {
            res <<= 1;
            pre.clear();
            for (auto n : nums) 
                pre.insert(n >> i);
            for (auto p : pre)
                if (pre.find((res ^ 1) ^ p) != pre.end()) {
                    res++;
                    break;
                }
        }
        return res;
    }
};