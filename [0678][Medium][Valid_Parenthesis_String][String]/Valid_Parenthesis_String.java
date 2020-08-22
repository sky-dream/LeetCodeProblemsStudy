// Time  Complexity: O(3**n)
// Space Complexity: O(1)
// solution 1. DFS.backtracking.
class Solution {
    public boolean checkValidString(String s) {
        return check(s, 0, 0);
    }
    
    private boolean check(String s, int start, int count) {
        if (count < 0) return false;
        for (int i = start; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') count++;
            else if (c == ')') {
                if (count-- == 0) return false;
            } else if (c == '*') {
                return check(s, i + 1, count + 1) ||  // 作为 (
                        check(s, i + 1, count - 1) || // 作为 )，抵消一个左括号
                        check(s, i + 1, count);       // 作为 空
            }
        }
        return count == 0;
    }
}