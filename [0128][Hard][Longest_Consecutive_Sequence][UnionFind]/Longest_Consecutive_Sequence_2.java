// solution 2, union find, iteration
// leetcode time     cost : 5 ms
// leetcode memory   cost : 40.6 MB 
// Time  Complexity: O(N)
// Space Complexity: O(N)
// https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/cbing-cha-ji-xie-fa-dai-ma-ji-duan-by-leck/
import java.util.HashMap;
import java.util.Map;
class Solution {
    public int find(int x,Map<Integer,Integer> map) {
        return map.containsKey(x)?find(x+1, map):x;
    }
    public int longestConsecutive(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        int max=0;
        for (int i:nums) {
            if (!map.containsKey(i - 1)) {
                max=Math.max(max,find(i+1 , map)-i);
            }
        }
        return max;
    }
}

public class Longest_Consecutive_Sequence_2 {
    public static void main(String args[]) {
        int nums[] = {100, 4, 200, 1, 3, 2}; // #expect is 4
        Solution Solution_obj = new Solution();
        int result = Solution_obj.longestConsecutive(nums);
        System.out.println("In java code,result is :" + result);
    }
}