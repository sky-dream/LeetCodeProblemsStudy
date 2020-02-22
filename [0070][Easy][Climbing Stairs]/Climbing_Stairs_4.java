// leetcode time     cost : 0 ms
// leetcode memory   cost : 36.1 MB 
// Time  Complexity: O(n)
// Space Complexity: O(1)
// slolution 4, Fibonacci sequence,
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}