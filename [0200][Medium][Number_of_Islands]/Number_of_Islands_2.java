// leetcode time     cost : 7 ms
// leetcode memory   cost : 42.2 MB 
// Time  Complexity: O(M*N)
// Space Complexity: O(min(m,n))
// solution 2, BFS,
import java.util.LinkedList;
import java.util.Queue;
class Solution {
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
            grid[r][c] = '0'; // mark as visited
            Queue<Integer> neighbors = new LinkedList<>();
            neighbors.add(r * nc + c);
            while (!neighbors.isEmpty()) {
              int id = neighbors.remove();
              int row = id / nc;
              int col = id % nc;
              if (row - 1 >= 0 && grid[row-1][col] == '1') {
                neighbors.add((row-1) * nc + col);
                grid[row-1][col] = '0';
              }
              if (row + 1 < nr && grid[row+1][col] == '1') {
                neighbors.add((row+1) * nc + col);
                grid[row+1][col] = '0';
              }
              if (col - 1 >= 0 && grid[row][col-1] == '1') {
                neighbors.add(row * nc + col-1);
                grid[row][col-1] = '0';
              }
              if (col + 1 < nc && grid[row][col+1] == '1') {
                neighbors.add(row * nc + col+1);
                grid[row][col+1] = '0';
              }
            }
          }
        }
      }
  
      return num_islands;
    }
}

public class Number_of_Islands_2 {
    public static void main(String args[]) {
        char[][] grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}; // expect is 1,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.numIslands(grid);
        System.out.println("In java code,result is :" + result);
    }
}
