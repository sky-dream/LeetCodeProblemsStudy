#include<iostream>
#include<vector>
#include<deque>
using namespace std;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        deque<int> q;
        for (int i = 0; i < n; i++) {

            while (!q.empty() && i - q.front() >= k)
                q.pop_front();

            while (!q.empty() && nums[i] >= nums[q.back()])
                q.pop_back();

            q.push_back(i);

            if (i >= k - 1)
                ans.push_back(nums[q.front()]);
        }
        return ans;
    }
};

int main(){
    int k = 3;
    vector<int> nums= {9, 3, -1, -3, 5, 3, 6, 7, -3}; //#expect is [9,3,5,5,6,7,7]
    Solution *obj = new Solution();
    vector<int> result = obj->maxSlidingWindow(nums, k);
    cout << "In cpp code, maxSlidingWindow array result  is : [";
    for(const int& x : result){
            cout << x << ", ";
    }
    cout << "]" << endl;
    return 0;
}