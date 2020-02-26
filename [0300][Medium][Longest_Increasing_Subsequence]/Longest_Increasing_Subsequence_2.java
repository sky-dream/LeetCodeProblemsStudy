// leetcode time     cost : 173 ms
// leetcode memory   cost : 101.2 MB 
// Time  Complexity: O(n**2)
// Space Complexity: O(n**2)
// slolution 2, recursion with memory,
public class Solution {
    public int lengthOfLIS(int[] nums) {
        int memo[][] = new int[nums.length + 1][nums.length];
        for (int[] l : memo) {
            Arrays.fill(l, -1);
        }
        return lengthofLIS(nums, -1, 0, memo);
    }
    public int lengthofLIS(int[] nums, int previndex, int curpos, int[][] memo) {
        if (curpos == nums.length) {
            return 0;
        }
        
        // directly use the value if memo[previndex + 1][curpos] is calculated before,
        // memo[previndex + 1][curpos] is the max window length 
        // if num[curpos] chosen and second end in window is nums[previndex + 1] when it comes to curpos, 
        if (memo[previndex + 1][curpos] >= 0) {
            return memo[previndex + 1][curpos];
        }
        // for every nums[currpos], the max window come to this position is memo[previndex + 1]=window[]
        // the winidow will be passed to the deeper level for recursion.
        int taken = 0;
        if (previndex < 0 || nums[curpos] > nums[previndex]) {
            taken = 1 + lengthofLIS(nums, curpos, curpos + 1, memo);
        }

        int nottaken = lengthofLIS(nums, previndex, curpos + 1, memo);
        // compare to DP the [curpos] is the outside iterator i, [previndex + 1] is the inside iterator j(0<j<i).
        memo[previndex + 1][curpos] = Math.max(taken, nottaken);
        return memo[previndex + 1][curpos];
    }
}

public class Longest_Increasing_Subsequence_2 {
    public static void main(String args[]) {
        int[] nums = {1,3,6,7,9,4,10,5,6}  ;   // expect is 6
        Solution Solution_obj = new Solution();
        int result = Solution_obj.lengthOfLIS(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}