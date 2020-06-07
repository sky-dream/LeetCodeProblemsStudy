# leetcode time     cost : 1088 ms
# leetcode memory   cost : 38.2 MB 
# Time  Complexity: O(len_s*len_s)
# Space Complexity: O(len_s*len_s)
# solution 2, using counter dict as prefix sum
class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        n = len(p)
        p = Counter(p)
        dp = [0] * (len(s) + 1)
        dp[0] = Counter()
        res = []
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1].copy()
            dp[i][s[i - 1]] += 1
            if i >= n and dp[i] - dp[i - n] == p: # high time cost when compare 2 dict here
                res.append(i - n)
        return res
    
def main():
    s, p,expectRes = "cbaebabacd" ,"abc", [0, 6]
    obj = Solution()
    
    result = obj.findAnagrams(s, p)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main()     