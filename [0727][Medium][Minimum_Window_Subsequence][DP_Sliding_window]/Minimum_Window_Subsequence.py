# leetcode time     cost : 1532 ms
# leetcode memory   cost : 14.3 MB
# Time  Complexity: O(N*K),N = len(S),K = len(T)
# Space Complexity: O(N)
# solution 1, DP with prefix str
class Solution(object):
    def minWindow(self, S, T):
        cur = [i if x == T[0] else None
               for i, x in enumerate(S)]
        #At time j when considering T[:j+1],
        #the smallest window [s, e] where S[e] == T[j]
        #is represented by cur[e] = s.
        for j in range(1, len(T)):
            last = None
            new = [None] * len(S)
            #Now we would like to calculate the candidate windows
            #"new" for T[:j+1].  'last' is the last window seen.
            for i, u in enumerate(S):
                if last is not None and u == T[j]: new[i] = last
                if cur[i] is not None: last = cur[i]
            cur = new

        #Looking at the window data cur, choose the smallest length
        #window [s, e].
        ans = ( 0, len(S) )
        #print(cur)
        for e, s in enumerate(cur):
            if s is not None and s >= 0 and (e - s) < (ans[1] - ans[0]):
                ans = (s, e)
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""
    
def main():
    S = "abcdebdde"; T = "bde";expectRes = "bcde"
    obj = Solution()
    result = obj.minWindow(S, T)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ", expectRes)
    
if __name__ =='__main__':
    main() 