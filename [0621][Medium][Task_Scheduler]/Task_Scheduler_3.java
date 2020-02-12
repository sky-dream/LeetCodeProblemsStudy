// solution 3, analysis and design.
// leetcode time     cost : 2 ms
// leetcode memory   cost : 38.3 MB 
// Time  Complexity: O(M)，M is all the task number
// Space Complexity: O(1)
import java.util.Arrays;
public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] map = new int[26];
        for (char c: tasks)
            map[c - 'A']++;
        Arrays.sort(map);
        int max_val = map[25] - 1, idle_slots = max_val * n;
        for (int i = 24; i >= 0 && map[i] > 0; i--) {
            idle_slots -= Math.min(map[i], max_val);
        }
        return idle_slots > 0 ? idle_slots + tasks.length : tasks.length;
    }
}
// solution 3, analysis and design, another version.
/*
The ONLY thing you need to care is the max number of one task!
We set apart each max task with interval n, and we hope to put all other tasks into those intervals. 
If the number of those tasks exceeds the interval space, then we don't need any idle interval at all. 
If not, the interval space plus the max tasks will be the least interval. Be care for the existent of multiple max tasks.
*/ 
public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] storage = new int[26];
        for (char c : tasks) {
            storage[(c - 'A')]++;
        }
        int max = 0;
        int count = 1;
        for (int num : storage) {
            if (num == 0) {
                continue;
            }
            if (max < num) {
                max = num;
                count = 1;
            } else if (max == num) {
                count++;
            }
        }
        int space = (n + 1) * (max - 1) + count;
        return (space < tasks.length) ? tasks.length : space;
    }
}