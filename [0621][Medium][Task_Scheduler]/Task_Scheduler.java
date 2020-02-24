// solution 1, sort.
// leetcode time     cost : 11 ms
// leetcode memory   cost : 38.7 MB 
// Time  Complexity: O(time)
// Space Complexity: O(1)
import java.util.Arrays;
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] map = new int[26];
        for (char c: tasks)
            map[c - 'A']++;
        Arrays.sort(map);
        int time = 0;
        while (map[25] > 0) {
            int i = 0;
            //when n interval is reached, reset i, start from the last position map[25] to excute the task char again.
            while (i <= n) {
                //for every cal in the loop, sort the array map, always keep the max number char in the last position map[25],
                //so if last position is 0, it means that all the task char are used up, all the task is finished.                
                if (map[25] == 0)
                    break;
                if (i < 26 && map[25 - i] > 0)
                    map[25 - i]--;
                //increase the cpu interval time counter    
                time++;
                //update the map index to switch to a new task char.
                i++;
            }
            //always keep the max number char in the last position map[25]
            Arrays.sort(map);
        }
        return time;
    }
}