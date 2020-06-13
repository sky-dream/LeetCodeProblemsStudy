// leetcode time     cost : 7 ms
// leetcode memory   cost : 43.5 MB
class Solution {
    public int numDecodings(String s) {
            if (s == null || s.length() == 0) {
                return 0;
            }
            return DFS(s, 0);
        }
    
        private int DFS(String s, int start) {
            //递归的第一步，应该是加终止条件，避免死循环。
            if (s.length() == start) {
                return 1;
            }
            //以0位开始的数是不存在的
            if (s.charAt(start) == '0') {
                return 0;
            }
            //递归的递推式应该是如果index的后两位小于等于26，  
            int ans1 = DFS(s, start + 1);
            int ans2 = 0;
            if (start < s.length() - 1) {
                int ten = (s.charAt(start) - '0') * 10;
                int one = (s.charAt(start + 1) - '0');
                if (ten + one <= 26) {
                    ans2 = DFS(s, start + 2);
                }
            }
            return ans1 + ans2;
        }
    }

public class Decode_Ways {
    public static void main(String args[]) {
        String word = "172426543102320";                     // #expect is 16
        Solution Solution_obj = new Solution();
        int result = Solution_obj.numDecodings(word);
        System.out.println("return value is :" + (result));
    }
}