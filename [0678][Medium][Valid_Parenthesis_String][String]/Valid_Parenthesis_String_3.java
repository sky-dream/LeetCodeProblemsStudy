// Time  Complexity: O(n)
// Space Complexity: O(1)
// solution 3. loop both 2 directions
class Solution {
    public boolean checkValidString(String s) {
        // all * for (, valid enough or not
        int l = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != ')') l++;
            else if (l-- == 0) return false;
        }
        if (l == 0) return true; // 必须所有都 (，且刚好够，可提前结束无需再验
    
        // all * for ), valid enough or not
        int r = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c != '(') r++;
            else if (r-- == 0) return false;
        }
        return true;
    }
}