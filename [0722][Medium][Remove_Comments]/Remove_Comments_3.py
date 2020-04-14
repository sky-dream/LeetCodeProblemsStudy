# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# with RE as filter
class Solution:
    def removeComments(self, source: [str]):
        s = re.sub('//.*|/\*(\s|.)*?\*/', '', '\n'.join(source)) 
        return filter(len, s.split('\n'))