// leetcode time     cost : 7 ms
// leetcode memory   cost : 39.9 MB
// Time  Complexity: O(n)
// Space Complexity: O(n)
// solutioin 3, optimized 2 pointers, hash table
import java.util.Map;
import java.util.HashMap;
class Solution_2 {
    // 定义一个哈希表用来记录上一次某个字符出现的位置，并初始化结果 max 为 0
        public int lengthOfLongestSubstring(String s) {
            Map<Character, Integer> map = new HashMap<>();
            int max = 0;
            // 用快慢指针 i 和 j 扫描一遍字符串，若快指针所对应的字符已经出现过，则慢指针
            for (int i = 0, j = 0; j < s.length(); j++) {
                if (map.containsKey(s.charAt(j))) {
                    i = Math.max(i, map.get(s.charAt(j)) + 1);
                }
                
                map.put(s.charAt(j), j);
                max = Math.max(max, j - i + 1);
            }
            
            return max;
        }
    }