// leetcode time     cost : 2 ms
// leetcode memory   cost : 43 MB 
// Time  Complexity: O(n*k)
// Space Complexity: O(n)
// slolution 1, num_i &= (num_i -1)
public class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num + 1];
        for (int i = 0; i <= num; ++i)
            ans[i] = popcount(i);
        return ans;
    }
    private int popcount(int x) {
        int count;
        for (count = 0; x != 0; ++count)
          x &= x - 1; //zeroing out the least significant nonzero bit
        return count;
    }
}