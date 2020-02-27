// leetcode time     cost : 3 ms
// leetcode memory   cost : 42 MB 
// Time  Complexity: O(M*N)
// Space Complexity: O(M*N)
// solution 1, DFS,
// https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
public class Solution {
  char[][] g;
  public int numIslands(char[][] grid) {
      int islands = 0;
      g = grid;
      for (int i=0; i<g.length; i++)
          for (int j=0; j<g[i].length; j++)
              islands += sink(i, j);
      return islands;
  }
  int sink(int i, int j) {
      if (i < 0 || i == g.length || j < 0 || j == g[i].length || g[i][j] == '0')
          return 0;
      g[i][j] = '0';
      sink(i+1, j); sink(i-1, j); sink(i, j+1); sink(i, j-1);
      return 1;
  }
}

public class Number_of_Islands_4 {
    public static void main(String args[]) {
        char[][] grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}; // expect is 1,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.numIslands(grid);
        System.out.println("In java code, 1st result is :" + result);
    }
}
