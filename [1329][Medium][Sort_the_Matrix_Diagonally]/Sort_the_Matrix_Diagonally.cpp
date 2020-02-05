// solution 3,
// leetcode time     cost : 12 ms
// leetcode memory   cost : 11 MB
// Time  Complexity: O(mn log(min(m,n))
// Space Complexity: O(min(m,n))
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        for (int i = 0; i < m; i++) {
            // combine sort(i,0) and sort(0,j) loop with 2 nested for loop and "i?1:n"
            for (int j = 0; j < (i?1:n); j++) {
                vector<int> vals;
                while (i<m && j<n)
                    vals.push_back( mat[i++][j++] );
                sort(vals.begin(), vals.end());
                while (i && j) {
                    mat[--i][--j] = vals.back();
                    vals.pop_back();
                }
            }
        }
        return mat;
    }
};