# leetcode time     cost : 236 ms
# leetcode memory   cost : 14.7 MB 
# Time  Complexity: O(len(s))
# Space Complexity: O(m+n)
# solution 1, sliding window, refer to No.76
# just as the same as finding the sub string start index in s that contains all the char in p.
import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        l1, l2 = len(p), len(s)
        need = collections.Counter(p)
        window = collections.Counter()
        cnt = 0  # 统计变量，统计window中字母和 need 中字母 频率相同的个数，
        left = right = 0 #滑动窗口[left,right]
        while right < l2:
            window[s[right]] += 1
            if need[s[right]] == window[s[right]]: #对于遍历到的字母，如果出现次数和need Dict相同, 统计变量+1
                cnt += 1                    
            right += 1                     #滑动窗口右移
            if right - left + 1 > l1:         # 判断左侧窗口是否要收缩
                if cnt == len(need):         
                    res.append(left)            
                if need[s[left]] == window[s[left]]:    #判断删除的left字母是否会影响cnt，若是则统计变量就减1
                    cnt -= 1
                window[s[left]] -= 1                #字典哈希表移除left字符
                if window[s[left]] == 0:            #由于counter特性，如果value为0，必须删除它
                    del window[s[left]]
                left += 1                        #最前面的下标右移动
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