// leetcode time     cost : 104 ms
// leetcode memory   cost : 136.4 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(MN)
// solution 1, recursion and divide
class Solution {
    public int numDistinct(String s, String t) {
        HashMap<String, Integer> map = new HashMap<>();
        return numDistinctHelper(s, 0, t, 0, map);
    }
    
        private int numDistinctHelper(String s, int s_start, String t, int t_start, HashMap<String, Integer> map) {
            //T 是空串，选法就是 1 种
            if (t_start == t.length()) { 
                return 1;
            }
            //S 是空串，选法是 0 种
            if (s_start == s.length()) {
                return 0;
            }
            String key = s_start + "@" + t_start;
            //先判断之前有没有求过这个解
            if (map.containsKey(key)) {
                return map.get(key); 
            }
            int count = 0;
            //当前字母相等
            if (s.charAt(s_start) == t.charAt(t_start)) {
                //从 S 选择当前的字母，此时 S 跳过这个字母, T 也跳过一个字母。
                count = numDistinctHelper(s, s_start + 1, t, t_start + 1, map)
                //S 不选当前的字母，此时 S 跳过这个字母，T 不跳过字母。
                    + numDistinctHelper(s, s_start + 1, t, t_start, map);
            //当前字母不相等  
            }else{ 
                //S 只能不选当前的字母，此时 S 跳过这个字母， T 不跳过字母。
                count = numDistinctHelper(s, s_start + 1, t, t_start, map);
            }
            //将当前解放到 map 中
            map.put(key, count);
            return count; 
        }
    }