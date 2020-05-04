# leetcode time     cost : 408 ms
# leetcode memory   cost : 21.6 MB
# Time  Complexity: O(N*K),N = len(S),K = len(T)
# Space Complexity: O(N)
# solution 2, DP with next pointer
class Solution(object):
    def minWindow(self, S, T):
        N = len(S)
        next = [None] * N
        last = [-1] * 26
        for i in range(N-1, -1, -1):
            last[ord(S[i]) - ord('a')] = i
            next[i] = tuple(last)
        #window [s, e]
        windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
        for j in range(1, len(T)):
            letter_index = ord(T[j]) - ord('a')
            windows = [[root, next[i+1][letter_index]]
                       for root, i in windows
                       if 0 <= i < N-1 and next[i+1][letter_index] >= 0]

        if not windows: return ""
        i, j = min(windows, key = lambda x: x[1]-x[0])
        return S[i: j+1]

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