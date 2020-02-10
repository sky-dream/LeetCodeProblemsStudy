package java.util;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Comparators;
// solution 2, max heap.
// leetcode time     cost : 49 ms
// leetcode memory   cost : 45.7 MB 
// Time  Complexity: O(time)
// Space Complexity: O(1)
class Solution {
    public String rearrangeString(String s, int k) {
        if(k <= 1)
            return s;
        int[] count = new int[26];
        for(char c: s.toCharArray())
            ++count[c - 'a'];
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                return count[o2] - count[o1] == 0 ? o1 - o2 : count[o2] - count[o1];
            }
        });
        
        for(int i = 0; i < 26; ++i)
            if(count[i] != 0)
            priorityQueue.add(i);
        StringBuilder strBuilder = new StringBuilder();
        for(int i = 0; i < s.length();  i += k) {
            List<Integer> temp = new ArrayList<>();
            for(int j = 0; j < k && i + j < s.length(); ++j) {
                if(priorityQueue.isEmpty())
                    return "";
                int c = priorityQueue.poll();
                temp.add(c);
                --count[c];
                strBuilder.append((char)('a' + c));
            }
            for(int c: temp)
                if(count[c] != 0)
                priorityQueue.add(c); 
        }       
        return strBuilder.toString();
    }
}