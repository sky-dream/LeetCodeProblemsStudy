# solution 1, based on the appearance count of each letter.
# leetcode time     cost : 24 ms
# leetcode memory   cost : 11.9 MB 
# Time  Complexity: O(A(N+logA))，其中 NN 是 SS 的长度，AA 是字母表的大小。
# Space Complexity: O(N)。
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)//2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[(N//2):], A[:(N//2)]
        return "".join(ans)

def main():
    string1 = "aabccddee" #expect is "abcac", or "acabc"
    obj = Solution()
    result = obj.reorganizeString(string1)
    print("return result is "+result);

if __name__ =='__main__':
    main() 