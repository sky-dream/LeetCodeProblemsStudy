// leetcode time     cost : 0 ms
// leetcode memory   cost : 37.3 MB 
// Time  Complexity: O(N*logN)
// Space Complexity: O(N)
// slolution 4, DP and Arrays.binarySearch(),
// link: https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode/ 
import java.util.Arrays;
public class Solution {
  public int lengthOfLIS(int[] nums) {
      // dp[i] is the longest increasing subsequence when come to nums[i]
      int[] dp = new int[nums.length];
      int len = 0;
      for (int num : nums) {
          // i is the index of the least value in dp which bigger than num(insert index for increasing queue) in the dp.
          // i= – (length + 1) if num not found and num is bigger than all value in dp,
          // i= – 1            if num not found and num is smaller than all value in dp,
          int i = Arrays.binarySearch(dp, 0, len, num);
          // if i= – (length + 1),then update the i to len to add the num in the end of dp.
          if (i < 0) {
              i = -(i + 1);
          }
          dp[i] = num;
          if (i == len) {
              len++;
          }
      }
      return len;
  }
}