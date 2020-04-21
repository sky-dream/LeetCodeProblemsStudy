// leetcode time     cost : 6 ms
// leetcode memory   cost : 39.5 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)
// solution 1, stack,
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Stack;
class Solution {
    // 在主函数里调用一个递归函数
    public int calculate(String s) {   
        Queue<Character> queue = new LinkedList<>();
        for (char c : s.toCharArray()) {
            if (c != ' ') queue.offer(c);
        }
        queue.offer('+');
    
        return calculate(queue);
    }

    int calculate(Queue<Character> queue) {
        char sign = '+';
        int num = 0;

        Stack<Integer> stack = new Stack<>();
    
        while (!queue.isEmpty()) {
            char c = queue.poll();

            if (Character.isDigit(c)) {
                num = 10 * num + c - '0';
            } 
            // 遇到一个左括号，开始递归调用，求得括号里的计算结果，将它赋给当前的 num  
            else if (c == '(') {
                num = calculate(queue);
            }
            else {
                if (sign == '+') {
                    stack.push(num);
                } else if (sign == '-') {
                    stack.push(-num);
                } else if (sign == '*') {
                    stack.push(stack.pop() * num);
                } else if (sign == '/') {
                    stack.push(stack.pop() / num);
                }
        
                num = 0;
                sign = c;
    
                // 遇到右括号，就可以结束循环，直接返回当前的总和     
                if (c == ')') {
                    break;
                }
            }
        }
    
        int sum = 0;
        while (!stack.isEmpty()) {
            sum += stack.pop();
        }
        return sum;
    
    }
}

public class Basic_Calculator_III_2 {
    public static void main(String args[]) {
        String string_s = "(2+6* 3+5- (3*14/7+2)*5)+3";      //expect is -12  
        Solution Solution_obj = new Solution();
        int result = Solution_obj.calculate(string_s);
        System.out.println("In java code,result is :" + result);
    }
}