import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    public int[] maxSlidingWindow(int[] a, int k) {
        if (a == null || k <= 0) {
            return new int[0];
        }
        int n = a.length;
        int[] r = new int[n - k + 1];
        int ri = 0;
        // store index
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < a.length; i++) {
            // remove numbers out of range k
            while (!q.isEmpty() && q.peek() < i - k + 1) {
                q.poll();
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
                q.pollLast();
            }
            // q contains index... r contains content
            q.offer(i);
            if (i >= k - 1) {
                r[ri++] = a[q.peek()];
            }
        }
        return r;
    }
}

public class Sliding_window_maximum {
    public static void main(String args[]) {
        int nums[] = { 9, 3, -1, -3, 5, 3, 6, 7, -3 }; // #expect is [9,3,5,5,6,7,7]
        int k = 3;
        Solution Solution_obj = new Solution();
        int result[] = Solution_obj.maxSlidingWindow(nums, k);
        System.out.println("In java code,last return value is :" + Arrays.toString(result));
    }
}