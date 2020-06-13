//consuming time: 20 ms,consuming memory: 39.8 MB,
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedList;
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0) return ans;
        List<Integer> list = new ArrayList<>();
        Arrays.sort(nums);
        getSum(nums, 0, target, ans, list, 0);
        return ans;
    }
    private void getSum(int[] nums, int sum, int target, List<List<Integer>> ans, List<Integer> list, int pos){
        if(list.size() == 4 && sum == target && !ans.contains(list)){
            ans.add(new ArrayList<>(list)); return;
        }else if(list.size() == 4) return;
        for(int i = pos; i < nums.length; i++){
            if(nums[i] +  nums[nums.length - 1] * (3 - list.size()) + sum < target) continue;
            if(nums[i] * (4 - list.size()) + sum > target) return;
            list.add(nums[i]);
            getSum(nums, sum + nums[i], target, ans, list, i + 1);
            list.remove(list.size() - 1);
        }
    }
};