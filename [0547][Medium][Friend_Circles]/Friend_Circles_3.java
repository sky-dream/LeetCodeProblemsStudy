// leetcode time     cost : 10 ms
// leetcode memory   cost : 42.4 MB 
// Time  Complexity: O(n**3)
// Space Complexity: O(n)
// solution 3, UnionFind,
import java.util.Arrays;
class Solution {
    int find(int parent[], int i) {
        if (parent[i] == -1)
            return i;
        return find(parent, parent[i]);
    }

    void union(int parent[], int x, int y) {
        int xset = find(parent, x);
        int yset = find(parent, y);
        if (xset != yset)
            parent[xset] = yset;
    }
    public int findCircleNum(int[][] M) {
        int[] parent = new int[M.length];
        Arrays.fill(parent, -1);
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M.length; j++) {
                if (M[i][j] == 1 && i != j) {
                    union(parent, i, j);
                }
            }
        }
        int count = 0;
        for (int i = 0; i < parent.length; i++) {
            if (parent[i] == -1)
                count++;
        }
        return count;
    }
}

public class Friend_Circles_3 {
    public static void main(String args[]) {
        int[][] M = {{1,1,0},{1,1,0},{0,0,1}}; // expect is 2,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.findCircleNum(M);
        System.out.println("In java code,result is :" + result);
    }
}