// leetcode time     cost : 8 ms
// leetcode memory   cost : 41.4 MB 
// Time  Complexity: O(n**2)
// Space Complexity: O(n)
// solution 2, BFS,
import java.util.LinkedList;
import java.util.Queue;
class Solution {
    public int findCircleNum(int[][] M) {
        int[] visited = new int[M.length];
        int count = 0;
        Queue < Integer > queue = new LinkedList < > ();
        for (int i = 0; i < M.length; i++) {
            if (visited[i] == 0) {
                queue.add(i);
                while (!queue.isEmpty()) {
                    int s = queue.remove();
                    // visited[s] = 1; the same effect as the statement in line 21,
                    for (int j = 0; j < M.length; j++) {
                        if (M[s][j] == 1 && visited[j] == 0)
                            visited[s] = 1;
                            queue.add(j);
                    }
                }
                count++;
            }
        }
        return count;
    }
}

public class Friend_Circles_2 {
    public static void main(String args[]) {
        int[][] M = {{1,1,0},{1,1,0},{0,0,1}}; // expect is 2,
        Solution Solution_obj = new Solution();
        int result = Solution_obj.findCircleNum(M);
        System.out.println("In java code,result is :" + result);
    }
}