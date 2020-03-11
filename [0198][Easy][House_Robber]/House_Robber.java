// leetcode time     cost : 0 ms
// leetcode memory   cost : 36.9 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
// solution 1, DP
class Solution {
    public int rob(int[] num) {
        int prevMax = 0;
        int currMax = 0;
        for (int x : num) {
            int temp = currMax;
            currMax = Math.max(prevMax + x, currMax);
            prevMax = temp;
        }
        return currMax;
    }
}