// leetcode time     cost : 42 ms
// leetcode memory   cost : 38.7 MB 
// Time  Complexity: O(n**2)
// Space Complexity: O(n)
// slolution 3, DP,
public class Solution {
    public int lengthOfLIS(int[] nums) {
      if (nums.length == 0) {
          return 0;
      }
      int maxLength = 1;
      int[] dp = new int[nums.length+1];
      // init dp[i], dp[i] is the max LISequece length which contains the nums[i] when come to nums[i],
      for (int i = 0; i < nums.length; ++i) 
          dp[i] = 1;
      for (int i = 1; i < nums.length; ++i) {
          for (int j = 0; j < i; ++j) {
              if (nums[j] < nums[i]) {
                  dp[i] = Math.max(dp[i], dp[j] + 1) ;
              }
          }
          maxLength = Math.max(maxLength, dp[i]);
      }
      return maxLength;
  }  
  // generate the subsequence to maintain its max length.

  public int lengthOfLIS_1(int[] nums) {
      if (nums.length == 0) {
          return 0;
      }
      // dp[i] is the longest increasing subsequence when come to nums[i]
      List<Integer> dp = new ArrayList<>();
      dp.add(nums[0]);
      int maxIndex = 0;
      for (int i = 0; i < nums.length; i++) {
            if (dp.get(maxIndex) < nums[i]) {
                dp.add(nums[i]);
                maxIndex++;
                
            }
            else{
                int tmpIndex = 0;
                //time can be saved if use binary search in while since dp is a increasing sequence.
                //refer to solution 4.
                while(dp.get(tmpIndex) < nums[i])
                    tmpIndex++;
                dp.set(tmpIndex,nums[i]);
            }
            //System.out.println("dp is :" + dp);
      }
      return dp.size();
  }
}

public class Longest_Increasing_Subsequence_3 {
    public static void main(String args[]) {
        int[] nums = {1,3,6,7,9,4,10,5,6}  ;   // expect is 6
        Solution Solution_obj = new Solution();
        int result = Solution_obj.lengthOfLIS(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}