// leetcode time     cost : ---
// leetcode memory   cost : --- 
// Time  Complexity: O(2**n)
// Space Complexity: O(n**2)
// slolution 1, brute force recursion
public class Solution {

    public int lengthOfLIS(int[] nums) {
        return lengthofLIS(nums, Integer.MIN_VALUE, 0);
    }

    public int lengthofLIS(int[] nums, int prev, int curpos) {
        if (curpos == nums.length) {
            return 0;
        }
        int taken = 0;
        if (nums[curpos] > prev) {
            taken = 1 + lengthofLIS(nums, nums[curpos], curpos + 1);
        }
        int nottaken = lengthofLIS(nums, prev, curpos + 1);
        return Math.max(taken, nottaken);
    }
}

public class Longest_Increasing_Subsequence {
    public static void main(String args[]) {
        int[] nums = {1,3,6,7,9,4,10,5,6}  ;   // expect is 6
        Solution Solution_obj = new Solution();
        int result = Solution_obj.lengthOfLIS(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}