// leetcode time     cost : 1 ms
// leetcode memory   cost : 37.9 MB
// solution 2 for space saving,
class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> dp = new ArrayList<>(1 << n);
        dp.add(0);
        for (int num = 1; num <= n; num++) {
            int count = 1 << num;
            int toAdd = 1 << (num - 1);
            for (int i = count / 2; i < count; i++) {
                int value = dp.get(count - 1 - i) + toAdd;
                dp.add(value);
            }
        }
        return dp;
    }
}

public class Gray_Code_2 {
    public static void main(String args[]) {
        int num = 2;                     // #expect is [0,1,3,2]
        Solution Solution_obj = new Solution();
        Boolean result = Solution_obj.grayCode(num);
        System.out.println("return value is :" + (result));
    }
}