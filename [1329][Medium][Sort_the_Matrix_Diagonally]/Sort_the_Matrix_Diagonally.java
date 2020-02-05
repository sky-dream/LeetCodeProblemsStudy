// solution 3,
// leetcode time     cost : 11 ms
// leetcode memory   cost : 40.5 MB
// Time  Complexity: O(mn log(min(m,n))
// Space Complexity: O(min(m,n))
class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        for (int i = 0; i < m; i++) {
            // combine sort(i,0) and sort(0,j) loop with 2 nested for loop and "i>0?1:n"
            for (int j = 0; j < (i>0?1:n); j++) {
                Stack<Integer> vals = new Stack<>();
                while (i<m && j<n)
                    vals.add(mat[i++][j++]);
                Collections.sort(vals);
                while (i > 0 && j > 0)
                    mat[--i][--j] = vals.pop();
            }
        }
        return mat;
    }
}