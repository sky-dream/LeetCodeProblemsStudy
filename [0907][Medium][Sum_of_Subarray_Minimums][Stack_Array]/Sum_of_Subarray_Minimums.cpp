// Time  Complexity: O(N) 
// Space Complexity: O(N)
// solution 1, 单调栈 Monotone Stack,construct preMinArr[],nextMinArr[]
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
  int sumSubarrayMins(vector<int>& A) {
    stack<pair<int, int>> in_stk_prev, in_stk_next;
    // left is for the distance to previous less element
    // right is for the distance to next less element
    vector<int> left(A.size()), right(A.size());
		
    //initialize
    for(int i = 0; i < A.size(); i++) left[i] =  i + 1;
    for(int i = 0; i < A.size(); i++) right[i] = A.size() - i;
		
    for(int i = 0; i < A.size(); i++){
      // for previous less
      while(!in_stk_prev.empty() && in_stk_prev.top().first > A[i]) 
        in_stk_prev.pop();
      left[i] = in_stk_prev.empty()? i + 1: i - in_stk_prev.top().second;
      in_stk_prev.push({A[i],i});
			
      // for next less
      while(!in_stk_next.empty() && in_stk_next.top().first > A[i]){
        auto x = in_stk_next.top();
        in_stk_next.pop();
        right[x.second] = i - x.second;
      }
      in_stk_next.push({A[i], i});
    }

    int ans = 0, mod = 1e9 +7;
    for(int i = 0; i < A.size(); i++){
      ans = (ans + A[i]*left[i]*right[i])%mod;
    }
    return ans;
  }
};
