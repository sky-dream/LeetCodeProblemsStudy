// leetcode time     cost : 0 ms
// leetcode memory   cost : 37.3 MB 
// Time  Complexity: O(N*logN)
// Space Complexity: O(N)
// slolution 4, DP and Arrays.binarySearch(),
// link: https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode/ 
import java.util.Arrays;
class Solution {
  public int lengthOfLIS(int[] nums) {
      // dp[i] is the longest increasing subsequence when come to nums[i]
      int[] dp = new int[nums.length];
      int len = 0;
      for (int num : nums) {
          // insertIndex is the index of the least value in dp which bigger than num(insert index for increasing queue) in the dp.
          // insertIndex= - (fromIndex + 1) if num not found and num is bigger than all value in dp,
          // insertIndex= – (toIndex + 1)   if num not found and num is smaller than all value in dp,
          int insertIndex = Arrays.binarySearch(dp, 0, len, num);
          // if insertIndex < 0,then update the insertIndex to to the fromIndex or toIndex of array dp[].
          if (insertIndex < 0) {
            insertIndex = -(insertIndex + 1);
          }
          dp[insertIndex] = num;
          if (insertIndex == len) {
              len++;
          }
          //System.out.println("int[] dp value is :" + (Arrays.toString(dp))+",insertIndex: "+insertIndex);
      }
      return len;
  }
}

public class Longest_Increasing_Subsequence_4 {
    public static void main(String args[]) {
        int[] nums = {1,3,6,7,9,4,10,5,6}  ;   // expect is 6
        Solution Solution_obj = new Solution();
        int result = Solution_obj.lengthOfLIS(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}