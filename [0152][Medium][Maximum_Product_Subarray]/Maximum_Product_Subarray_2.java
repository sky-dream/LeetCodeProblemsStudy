// leetcode time     cost : 2 ms
// leetcode memory   cost : 38.4 MB
// solution 1, DP, Save Min value and Max value at each node and the result works out.
import java.math.*;
class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        
        int res = nums[0];
        int positive = 1;
        int negative = 1;        
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (x >= 0) {
                positive = Math.max(positive * x, x);
                negative = negative * x;
            } else {
                int tmp = negative;
                negative = Math.min(positive * x, x);
                positive = tmp * x;
            }
            res = Math.max(res,positive);
        }
        return res;
    }
}

public class Maximum_Product_Subarray_2 {
    public static void main(String args[]) {
        int[] nums = {2,3,-2,4} ;   // expect is 6
        
        Solution Solution_obj = new Solution();
        int result = Solution_obj.maxProduct(nums);
        System.out.println("In java code,return value is :" + (result));
    }
}