// leetcode time     cost : 5 ms
// leetcode memory   cost : 39.7 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// solution 1, stack,
import java.util.ArrayDeque;
import java.util.Queue;
class Solution {
    public int calculate(String s) {
        Queue<Character> q = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c != ' ') {
                q.offer(c);
            }
        }

        q.offer(' ');
        return helper(q);
    }

    private int helper(Queue<Character> q) {
        int num = 0;
        int prev = 0, sum = 0;
        char prevOp = '+';

        while (!q.isEmpty()) {
            char c = q.poll();

            if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            } else if (c == '(') {
                num = helper(q);
            } else {
                switch (prevOp) {
                case '+':
                    sum += prev;
                    prev = num;
                    break;
                case '-':
                    sum += prev;
                    prev = -num;
                    break;
                case '*':
                    prev *= num;
                    break;
                case '/':
                    prev /= num;
                    break;
                }

                if (c == ')') break;

                num = 0;
                prevOp = c;
            }
        }

        return sum + prev;
    }
}

public class Basic_Calculator_III {
    public static void main(String args[]) {
        String string_s = "(2+6* 3+5- (3*14/7+2)*5)+3";      //expect is -12  
        Solution Solution_obj = new Solution();
        int result = Solution_obj.calculate(string_s);
        System.out.println("In java code,result is :" + result);
    }
}