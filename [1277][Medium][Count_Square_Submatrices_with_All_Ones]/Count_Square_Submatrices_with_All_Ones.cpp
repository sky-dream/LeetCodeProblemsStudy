// leetcode time     cost : 88 ms
// leetcode memory   cost : 20.1 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(1)
// solution 1, DP, refer to No.221
class Solution {
public:
    int countSquares(vector<vector<int>>& A) {
        int res = 0;
        for (int i = 0; i < A.size(); ++i)
            for (int j = 0; j < A[0].size(); res += A[i][j++])
                if (A[i][j] && i && j)
                    A[i][j] += min({A[i - 1][j - 1], A[i - 1][j], A[i][j - 1]});
        return res;
    }
};