// leetcode time     cost : 1 ms
// leetcode memory   cost : 42.5 MB 
// Time  Complexity: O(n**2)
// Space Complexity: O(n)
// solution 1, DFS,
class Solution {
    public void dfs(int[][] M, int[] visited, int i) {
        for (int j = 0; j < M.length; j++) {
            if (M[i][j] == 1 && visited[j] == 0) {
                visited[j] = 1;
                dfs(M, visited, j);
            }
        }
    }
    public int findCircleNum(int[][] M) {
        int[] visited = new int[M.length];
        int count = 0;
        for (int i = 0; i < M.length; i++) {
            if (visited[i] == 0) {
                dfs(M, visited, i);
                count++;
            }
        }
        return count;
    }
}

public class Friend_Circles {
    public static void main(String args[]) {
        int[][] M = {{1,1,0},{1,1,0},{0,0,1}}; // expect is 2,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.findCircleNum(M);
        System.out.println("In java code,result is :" + result);
    }
}