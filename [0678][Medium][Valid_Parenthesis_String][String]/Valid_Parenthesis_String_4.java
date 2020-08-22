// Time  Complexity: O(n)
// Space Complexity: O(1)
// solution 4, 2 stacks
//https://leetcode-cn.com/problems/valid-parenthesis-string/solution/fen-zhi-tan-xin-shuang-xiang-bian-li-shuang-zhan-j/
class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> left = new Stack<>(), star = new Stack<>(); // index stack
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') left.push(i);
            else if (c == '*') star.push(i);
            else {
                if (!left.isEmpty()) left.pop();
                else if (!star.isEmpty()) star.pop();
                else return false;
            }
        }
    
        while (!left.isEmpty() && !star.isEmpty()) {
            if (left.pop() > star.pop()) return false;
        }
        return left.isEmpty();
    }
    }