// solution 1, analysis.
// leetcode time     cost : 0 ms
// leetcode memory   cost : 39.2 MB 
// Time  Complexity: O(1)
// Space Complexity: O(1)
import java.math.*;
class Solution {
    public int integerBreak(int n) {
    int p = n % 3, q = n / 3, r = p + (2 * p + 1) % 5;      //p=0,p&1=0, r=1; p=1,p&1=1, r=4; p=2,p&1=0, r=2;
    return n <= 3 ? n - 1 : (int)(Math.pow(3, q - (p & 1)) * r);
    }
}

public class Integer_Break {
    public static void main(String args[]) {
        int N =2; // #expect is 1
        int result = Solution_obj.integerBreak(2);
        System.out.println("In java code,result is :" + result );
    }
}