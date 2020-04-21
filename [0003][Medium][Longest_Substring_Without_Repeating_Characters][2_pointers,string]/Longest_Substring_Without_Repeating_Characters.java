// leetcode time     cost : 9 ms
// leetcode memory   cost : 39.8 MB
// Time  Complexity: O(n)
// Space Complexity: O(n)
// solutioin 2, 2 pointers, linearly scan
class Solution {
// 定义一个哈希集合 set，初始化结果 max 为 0    
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int max = 0;
        // 用快慢指针 i 和 j 扫描一遍字符串，如果快指针所指向的字符已经出现在哈希集合里，不断地尝试将慢指针所指向的字符从哈希集合里删除
        for (int i = 0, j = 0; j < s.length(); j++) {
            while (set.contains(s.charAt(j))) {
                set.remove(s.charAt(i));
                i++;
            }
            
            // 当快指针的字符加入到哈希集合后，更新一下结果 max
            set.add(s.charAt(j));
            max = Math.max(max, set.size());
        }
        return max;
    }
}