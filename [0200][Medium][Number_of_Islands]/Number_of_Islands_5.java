// leetcode time     cost : 3 ms
// leetcode memory   cost : 42.1 MB 
// Time  Complexity: O(M*N)
// Space Complexity: O(M*N)
// solution 2, BFS,
// // https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
public class Solution {
  public int numIslands(char[][] grid) {
      int islands = 0;
      for (int i=0; i<grid.length; i++)
          for (int j=0; j<grid[i].length; j++)
              islands += sink(grid, i, j);
      return islands;
  }
  int sink(char[][] grid, int i, int j) {
      if (i < 0 || i == grid.length || j < 0 || j == grid[i].length || grid[i][j] == '0')
          return 0;
      grid[i][j] = '0';
      for (int k=0; k<4; k++)
          sink(grid, i+d[k], j+d[k+1]);
      return 1;
  }
  int[] d = {0, 1, 0, -1, 0};
}

public class Number_of_Islands_5 {
    public static void main(String args[]) {
        char[][] grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}; // expect is 1,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.numIslands(grid);
        System.out.println("In java code,result is :" + result);
    }
}
