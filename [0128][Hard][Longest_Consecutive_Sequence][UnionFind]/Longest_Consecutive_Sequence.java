// solution 1, union find, 
// leetcode time     cost : 1040 ms
// leetcode memory   cost : 42.2 MB 
// Time  Complexity: O(N)
// Space Complexity: O(N)
import java.util.HashMap;
import java.util.Map;
class Solution {
    public int find(int x,Map<Integer,Integer> map) {
        return map.containsKey(x)?find(x+1, map):x;
    }
    public int longestConsecutive(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        //make set
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        int max=0;
        //find
        for (int i:nums) {       
            max=Math.max(max,find(i+1 , map)-i);
        }
        return max;
    }
}

public class Longest_Consecutive_Sequence {
    public static void main(String args[]) {
        int nums[] = {100, 4, 200, 1, 3, 2}; // #expect is 4
        Solution Solution_obj = new Solution();
        int result = Solution_obj.longestConsecutive(nums);
        System.out.println("In java code,result is :" + result);
    }
}