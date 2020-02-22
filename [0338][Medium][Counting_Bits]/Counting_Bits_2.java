// leetcode time     cost : 2 ms
// leetcode memory   cost : 43.1 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// slolution 2, DP and highest effective bit,
// P(i+b)=P(i)+1, b=2**m > i
public class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num + 1];
        int i = 0, b = 1;
        // [0, b) is calculated
        while (b <= num) {
            // generate [b, 2b) or [b, num) from [0, b)
            while(i < b && i + b <= num){
                ans[i + b] = ans[i] + 1;
                ++i;
            }
            i = 0;   // reset i
            b <<= 1; // b = 2b
        }
        return ans;
    }
}