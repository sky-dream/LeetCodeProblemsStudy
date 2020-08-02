# solution 1, 2 pointers
# Time  Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s)==1:
            return s
        l,r = 0, len(s)-1
        while (l<r):
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
       