// leetcode time     cost : 1 ms
// leetcode memory   cost : 36.4 MB 
// Time  Complexity: O(logN)
// Space Complexity: O(logN)
// solution 2, matrix expo
class Solution {
    int MOD = 1_000_000_007;

    public int numTilings(int N) {
        int[][] T = new int[][]{{1,0,0,1},{1,0,1,0},{1,1,0,0},{1,1,1,0}};
        return matrixExpo(T, N)[0][0];
    }

    public int[][] matrixMult(int[][] A, int[][] B) {
        int[][] ans = new int[A.length][A.length];
        for (int i = 0; i < A.length; i++)
            for (int j = 0; j < B[0].length; j++) {
                long entry = 0;
                for (int k = 0; k < B.length; k++)
                    entry += (long) A[i][k] * (long) B[k][j] % MOD;
                ans[i][j] = (int) (entry % MOD);
            }

        return ans;
    }

    public int[][] matrixExpo(int[][] A, int pow) {
        int[][] ans = new int[A.length][A.length];
        for (int i = 0; i < A.length; i++) ans[i][i] = 1;
        if (pow == 0) return ans;
        if (pow == 1) return A;
        if (pow % 2 == 1) return matrixMult(matrixExpo(A, pow-1), A);
        int[][] B = matrixExpo(A, pow / 2);
        return matrixMult(B, B);
    }
}