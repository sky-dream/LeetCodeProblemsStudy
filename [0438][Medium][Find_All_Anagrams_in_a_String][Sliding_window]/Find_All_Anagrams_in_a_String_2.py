# leetcode time     cost : 108 ms
# leetcode memory   cost : 14.7 MB 
# Time  Complexity: O(len(s))
# Space Complexity: O(m+n)
# solution 1, sliding window with array, refer to No.76
class Solution:
    def findAnagrams(self, s: str, p: str):
        # 记录p, s字母个数
        p_count = [0] * 26
        s_count = [0] * 26
        res = []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            # print(p_count, s_count)
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            # 窗口加一个， 减一个，维护长度为len(p)的长度
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
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