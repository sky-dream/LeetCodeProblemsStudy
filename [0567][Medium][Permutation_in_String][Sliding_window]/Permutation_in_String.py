# leetcode time     cost : 124 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(len(s2))
# Space Complexity: O(m+n)
# solution 1, sliding window, refer to No.76
# just as the same as finding the sub string in s2 that contains all the char in s1.
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        need = collections.Counter(s1)
        window = collections.Counter()
        cnt = 0  # 统计变量，统计window中字母和 need 中字母 频率相同的个数，
        left = right = 0 #滑动窗口[left,right]
        while right < l2:
            window[s2[right]] += 1
            if need[s2[right]] == window[s2[right]]: #对于遍历到的字母，如果出现次数和need Dict相同, 统计变量+1
                cnt += 1              
            if cnt == len(need):         # 如果s2滑动窗口和s1全部字符相同，返回真
                return True             # 当cnt == need中字母的个数的时候，就是全部符合题意，返回真
            right += 1                     #滑动窗口右移
            if right - left + 1 > l1:         # 判断左侧窗口是否要收缩
                if need[s2[left]] == window[s2[left]]:    #判断删除的left字母是否会影响cnt，若是则统计变量就减1
                    cnt -= 1
                window[s2[left]] -= 1                #字典哈希表移除left字符
                if window[s2[left]] == 0:            #由于counter特性，如果value为0，必须删除它
                    del window[s2[left]]
                left += 1                        #最前面的下标右移动
        return False 
    
def main():
    s1, s2,expectRes = "ab" ,"eidbaooo", True
    obj = Solution()
    
    result = obj.checkInclusion(s1, s2)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main()     