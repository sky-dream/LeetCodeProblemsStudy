// leetcode time     cost : 544 ms
// leetcode memory   cost : 8.7 MB 
#include <stdlib.h>
#include<iostream>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res (nums.size(), 0);
        vector<pair<int, int>> v;
        for (int i = 0; i < nums.size(); i++) {
            v.emplace_back(nums[i], i);
        }
        mergeSort(v, res, 0, nums.size()-1);
        return res;
    }
    
    void mergeSort(vector<pair<int, int>>& v, vector<int>& res, int l, int r) {
        if (l >= r) return;
        int mid = l + (r - l) / 2;
        mergeSort(v, res, l, mid);
        mergeSort(v, res, mid+1, r);
        auto compare = [](pair<int, int> a, pair<int, int> b) { return a.first < b.first;};
        for (int i = mid; i >= l; i--) {
            //lower_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个大于或等于num的数字，找到返回该数字的地址，不存在则返回end
            //upper_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个大于num的数字，找到返回该数字的地址，不存在则返回end
            auto it = lower_bound(v.begin()+mid+1, v.begin()+r+1, v[i], compare);
            //通过返回的地址减去起始地址begin,得到找到数字在数组中的下标
            int dis = distance(v.begin()+mid+1, it);
            if (dis == 0) break;
            res[v[i].second] += dis;
        }
        inplace_merge(v.begin()+l, v.begin()+mid+1, v.begin()+r+1, compare);
    }
};