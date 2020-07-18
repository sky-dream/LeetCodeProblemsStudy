// leetcode time     cost : 31 ms
// leetcode memory   cost : 38.1 MB
// Time  Complexity: O(n**2)
// Space Complexity: O(n)
// solution 2, 2 pointer，中心扩散法，要注意奇数及偶数长度回文
public class Solution {
    private int lo, maxLen;

    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2)
            return s;
        
        for (int i = 0; i < len-1; i++) {
            extendPalindrome(s, i, i);  //assume odd length, try to extend Palindrome as possible
            extendPalindrome(s, i, i+1); //assume even length.
        }
        return s.substring(this.lo, this.lo + this.maxLen);
    }

    private void extendPalindrome(String s, int j, int k) {
        while (j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        if (this.maxLen < k - j - 1) {
            this.lo = j + 1;
            this.maxLen = k - j - 1;
        }
    }
}