# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# with RE as filter
class Solution:
    def removeComments(self, source: [str]):
        s = '\n'.join(source) + '\n' #为最后一行的'//'提供闭区间
        i, n = 1, len(s)
        ans = ''
        while i < n:
            if s[i - 1] + s[i] == '//':
                i = s.find('\n', i) + 1
            elif s[i - 1] + s[i] == '/*':
                i = s.find('*/', i + 1) + 3
            else:
                ans += s[i - 1]
                i += 1
        return filter(len, ans.split('\n'))