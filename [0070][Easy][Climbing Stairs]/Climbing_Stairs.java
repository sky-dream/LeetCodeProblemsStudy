// leetcode time     cost : time exceeded.
// leetcode memory   cost : ----
// Time  Complexity: O(2**n)
// Space Complexity: O(n)
// slolution 1, brute force recursion,
public class Solution {
    public int climbStairs(int n) {
        climb_Stairs(0, n);
    }
    public int climb_Stairs(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
    }
}