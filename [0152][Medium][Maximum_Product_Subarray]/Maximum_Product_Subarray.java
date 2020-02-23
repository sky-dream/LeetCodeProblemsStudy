// leetcode time     cost : 2 ms
// leetcode memory   cost : 38.6 MB
// solution 1, DP, Save Min value and Max value at each node and the result works out.
import java.math.*;
class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int max = nums[0], min = nums[0], result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int temp = max;
            max = Math.max(Math.max(max * nums[i], min * nums[i]), nums[i]);
            min = Math.min(Math.min(temp * nums[i], min * nums[i]), nums[i]);
            if (max > result) {
                result = max;
            }
        }
        return result;
    }
    public int maxProduct_1(int[] nums) {
        int n = nums.length, res = nums[0], l = 0, r = 0;
        for (int i = 0; i < n; i++) {
            l =  (l == 0 ? 1 : l) * nums[i];
            r =  (r == 0 ? 1 : r) * nums[n - 1 - i];
            res = Math.max(res, Math.max(l, r));
        }
        return res;
    }
}

public class Maximum_Product_Subarray {
    public static void main(String args[]) {
        int[] nums = {2,3,-2,4} ;   // expect is 6
        
        Solution Solution_obj = new Solution();
        int result = Solution_obj.maxProduct(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}