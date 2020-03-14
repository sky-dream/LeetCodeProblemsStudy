// leetcode time     cost : 6 ms
// leetcode memory   cost : 41.8 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(MN)
// solution 2, BFS
public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        int[][] dirs={{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        Queue < int[] > queue = new LinkedList < > ();
        queue.add(start);
        visited[start[0]][start[1]] = true;
        while (!queue.isEmpty()) {
            int[] popNode = queue.remove();
            if (popNode[0] == destination[0] && popNode[1] == destination[1])
                return true;
            for (int[] dir: dirs) {
                int x = popNode[0] + dir[0];
                int y = popNode[1] + dir[1];
                while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                }
                if (!visited[x - dir[0]][y - dir[1]]) {
                    queue.add(new int[] {x - dir[0], y - dir[1]});
                    visited[x - dir[0]][y - dir[1]] = true;
                }
            }
        }
        return false;
    }
}