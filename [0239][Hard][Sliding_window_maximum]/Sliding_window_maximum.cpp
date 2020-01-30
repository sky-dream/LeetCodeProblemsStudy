#include<iostream>
#include<vector>
#include<deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size() ;
        vector<int> result;
        if(n == 0) {
            result.clear() ;
            return result ; 
        }
        deque<pair<int,int>> q ;
        for(int i=0;i<=n-1;++i){
            if( (i>=k) and (q.front().second <= i-k))       //when the window is flowing, left element need to be discarded.
               q.pop_front() ;      //discard the left element at the start of the queue
            while(q.size() > 0 and q.back().first <= nums[i]){      //only keep the max value from the window in the queue.
                q.pop_back();       //discard the right element at the end of the queue
            }
            q.push_back({nums[i] , i});
            if (i >= k-1)
               result.push_back(q.front().first) ; 

        }
        return result ; 
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
}