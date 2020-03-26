// leetcode time     cost : 95 ms
// leetcode memory   cost : 135.8 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(MN)
// solution 2, DFS with mome and global counter
class Solution {
    int count = 0;
    public int numDistinct(String s, String t) { 
        HashMap<String, Integer> map = new HashMap<>();
        numDistinctHelper(s, 0, t, 0, map);
        return count;
    }

    private void numDistinctHelper(String s, int s_start, String t, int t_start, 
                HashMap<String, Integer> map) {
        if (t_start == t.length()) {
            count++; 
            return;
        }
        if (s_start == s.length()) {
            return;
        }
        String key = s_start + "@" + t_start;
        if (map.containsKey(key)) {
            count += map.get(key);
            return; 
        }
        int count_pre = count;
        //当前字母相等，s_start 后移一个，t_start 后移一个
        if (s.charAt(s_start) == t.charAt(t_start)) {
            numDistinctHelper(s, s_start + 1, t, t_start + 1, map);
        }
        //出来以后，继续尝试不选择当前字母，s_start 后移一个，t_start 不后移
        numDistinctHelper(s, s_start + 1, t, t_start, map);
        
        //将增量存起来
        int count_increment = count - count_pre;
        map.put(key, count_increment); 
    }
}