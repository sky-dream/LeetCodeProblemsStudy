// leetcode time     cost : 8 ms
// leetcode memory   cost : 10.6 MB
// solution 1, DP by iterate from the last 2nd row to the top row.
#include <bits\stdc++.h>
using namespace std;
class Solution {
    public:
        int minimumTotal(vector<vector<int> > &triangle) {
            int n= triangle.size();
            for(int i=n-2 ; i>=0 ; i--){
                for(vector<int>::size_type j=0 ; j<triangle[i].size() ; j++ ){
                    triangle[i][j] = min(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1]);
                }
            }
            return triangle[0][0];
        }
};