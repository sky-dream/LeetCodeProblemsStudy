// leetcode time     cost : 2 ms
// leetcode memory   cost : 42.9 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(MN)
// solution 1, DFS
public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        visited[start[0]][start[1]] = false;
        return dfs(maze, start, destination, visited);
    }
    public boolean dfs(int[][] maze, int[] start, int[] destination, boolean[][] visited) {
        int[][] dirs={{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        //since start and dest are not the same, no need check dest at first.

        for (int[] dir: dirs) {
            int x = start[0] + dir[0];
            int y = start[1] + dir[1];
            while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                x += dir[0];
                y += dir[1];
            }
            // backtrack to the point before the blocked point, try another direction
            x= x-dir[0];y = y-dir[1] ; 
            //check dest found or not
            if (x == destination[0] && y == destination[1])
                return true; 
            //if (x,y) not visited, drilled down                         
            if (!visited[x][y]) {
                visited[x][y] =true;
                int[] newStart = {x,y};
                System.out.println("drill down to x: "+x+" ,y: "+y);
                if (dfs(maze, newStart, destination, visited))
                    return true;
            }
        }
        return false;
    }
}