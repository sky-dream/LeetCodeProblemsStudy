// leetcode time     cost : 2 ms
// leetcode memory   cost : 42.3 MB 
// Time  Complexity: O(M*N)
// Space Complexity: O(M*N)
// solution 1, DFS,
class Solution {
    void dfs(char[][] grid, int r, int c) {
      int nr = grid.length;
      int nc = grid[0].length;
  
      if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
        return;
      }
  
      grid[r][c] = '0';
      dfs(grid, r - 1, c);
      dfs(grid, r + 1, c);
      dfs(grid, r, c - 1);
      dfs(grid, r, c + 1);
    }
  
    public int numIslands(char[][] grid) {
      if (grid == null || grid.length == 0) {
        return 0;
      }
  
      int nr = grid.length;
      int nc = grid[0].length;
      int num_islands = 0;
      for (int r = 0; r < nr; ++r) {
        for (int c = 0; c < nc; ++c) {
          if (grid[r][c] == '1') {
            ++num_islands;
            dfs(grid, r, c);
          }
        }
      }
  
      return num_islands;
    }
  }

  public class Number_of_Islands {
    public static void main(String args[]) {
        char[][] grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}; // expect is 1,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.numIslands(grid);
        System.out.println("In java code,result is :" + result);
    }
}