// solution 2, PriorityQueue.
// leetcode time     cost : 49 ms
// leetcode memory   cost : 38.9 MB 
// Time  Complexity: O(time)
// Space Complexity: O(1)
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Collections;
class Solution1 {
    public int leastInterval(final char[] tasks, final int n) {
        final int[] map = new int[26];
        for (final char c : tasks)
            map[c - 'A']++;
        // max heap, keep the max value of the char on the top.
        final PriorityQueue<Integer> queue = new PriorityQueue<>(26, Collections.reverseOrder());
        for (final int f : map) {
            if (f > 0)
                queue.add(f);
        }
        int time = 0;
        while (!queue.isEmpty()) {
            int i = 0;
            final List<Integer> temp = new ArrayList<>();
            while (i <= n) {
                if (!queue.isEmpty()) {
                    if (queue.peek() > 1)
                        temp.add(queue.poll() - 1);
                    else
                        queue.poll();
                }
                time++;
                if (queue.isEmpty() && temp.size() == 0)
                    break;
                i++;
            }
            for (final int l : temp)
                queue.add(l);
        }
        return time;
    }
}