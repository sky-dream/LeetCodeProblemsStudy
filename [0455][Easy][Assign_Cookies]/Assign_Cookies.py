# solution 1 greedy algorithm.
# leetcode time     cost : 160 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(NlogN)
# Space Complexity: O(1)
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
    
def main():
    greedy_i = [1,2,3]
    size_j = [1,2,3]
    obj = Solution()
    res = obj.lemonadeChange(greedy_i,size_j)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     
'''
because you are an awesome parent, you should assign as big cookies as possible. 
So you should assign cookies in reverse order, though the result is the same. 
'''
"""     
        i,j = len(g)-1,len(s)-1
        count = 0
        while (i>=0 and j>=0):
            if g[i] <= s[j]:
                count += 1
                i-=1
                j-=1
            else:
                i -= 1 
"""