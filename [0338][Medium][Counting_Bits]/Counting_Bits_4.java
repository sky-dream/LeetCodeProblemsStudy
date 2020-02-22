// leetcode time     cost : 1 ms
// leetcode memory   cost : 43.1 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// slolution 4, DP and lowest set bit,
// P(i)=P( i&(i-1) ) + 1, use x &= x - 1 to get the lowest set bit,
public class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num + 1];
        for (int i = 1; i <= num; ++i)
          ans[i] = ans[i & (i - 1)] + 1;
        return ans;
    }
}