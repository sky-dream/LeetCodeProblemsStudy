// solution 1, Sliding window.
// leetcode time     cost : 4 ms
// leetcode memory   cost : 39.7 MB
// Time  Complexity: O(M+N)
// Space Complexity: O(M+N)
class Solution {
  public String minWindow(String s, String t) {
      int m = s.length(), n = t.length();
      if (m < n) return "";
      int[] freq = new int[128];
      for (int i = 0; i < n; ++i) 
          freq[t.charAt(i)]++;
      int start = 0, len = m + 1, cnt = 0, left = 0;
      
      for (int i = 0; i < m; ++i) {
          if (--freq[s.charAt(i)] >= 0) 
              ++cnt;
          // while all char in the t found in current window, move left forward,
          while (cnt == n) {
              if (i - left + 1 < len) {
                  start = left;
                  len = i - left + 1;
              }
              if (++freq[s.charAt(left)] > 0) 
                  --cnt;
              ++left;
          }
      }
      return len > m ? "" : s.substring(start, start + len);
  }
}