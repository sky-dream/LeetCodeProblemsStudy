// leetcode time     cost : 2 ms
// leetcode memory   cost : 37.9 MB
class Solution {
    private List<List<Integer>> records;

    public List<Integer> grayCode(int n) {
        records = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            records.add(new ArrayList<>(1 << i));
        }
        // 1. dp初始状态，即把数字0的格雷码先加入dp中
        dp(0).add(0);
        // 2. dp递推过程，通过循环依次计算数字1, 2, 3, ..., n 的格雷码
        for (int num = 1; num <= n; num++) {
            // 数字num的格雷码的总个数2^num
            int count = 1 << num;
            for (int i = 0; i < count; i++) {
                int value;        
                if (i < count / 2) {
                    // 前半部分直接复制num-1的格雷码
                    value = dp(num - 1).get(i);
                } else {
                    // 后半部分通过在首位添加1位1得到
                    int toAdd = 1 << (num - 1);
                    value = dp(num).get(count - 1 - i) + toAdd;
                }
                dp(num).add(value);
            }
        }
        return dp(n);
    }

    /**
    * 返回num的greycode
    */
    private List<Integer> dp(int num) {
        return records.get(num);
    }
}

public class Gray_Code {
    public static void main(String args[]) {
        int num = 2;                     // #expect is [0,1,3,2]
        Solution Solution_obj = new Solution();
        Boolean result = Solution_obj.grayCode(num);
        System.out.println("return value is :" + (result));
    }
}