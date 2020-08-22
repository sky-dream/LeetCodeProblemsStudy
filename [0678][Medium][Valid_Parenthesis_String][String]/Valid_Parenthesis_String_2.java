// Time  Complexity: O(n)
// Space Complexity: O(1)
// solution 2. greedy
class Solution {
    public boolean checkValidString(String s) {
        // possible range
        int min = 0, max = 0; // 维护当前左括号的数量范围：[min, max]
        for (char c : s.toCharArray()) {
            if (c == '(') {
                ++min;
                ++max;
            } else if (c == ')') {
                if (min > 0) min--;
                if (max-- == 0) return false;// 左括号不够
            } else {
                if (min > 0) min--; // 可作为右括号，抵消
                ++max; // 可作为左括号
            }
        }
        return min == 0;
    }
}