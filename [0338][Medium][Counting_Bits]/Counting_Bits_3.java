// leetcode time     cost : 1 ms
// leetcode memory   cost : 43.3 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// slolution 3, DP and lowest effective bit,
// P(i)=P(i/2) + (i % 2), (i % 2)--->(i & 1)
public class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num + 1];
        for (int i = 1; i <= num; ++i)
          ans[i] = ans[i >> 1] + (i & 1); // x / 2 is x >> 1 and x % 2 is x & 1
        return ans;
    }
}