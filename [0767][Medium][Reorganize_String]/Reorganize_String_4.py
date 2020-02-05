# solution 1, 4 line simple version.
# leetcode time     cost : 24 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(A(N+logA))，其中 NN 是 SS 的长度，AA 是字母表的大小。
# Space Complexity: O(N)。
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = sorted(sorted(S), key=S.count)
        h = len(a) // 2
        print("a[:h]  "+str(a[:h])+", a[h:]  "+str(a[h:]))
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1] != a[-2])
def main():
    string1 = "aabcc" #expect is "abcac", or "acabc"
    obj = Solution()
    result = obj.reorganizeString(string1)
    print("return result is "+result);

if __name__ =='__main__':
    main() 