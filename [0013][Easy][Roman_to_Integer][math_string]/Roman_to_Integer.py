# -*- coding: utf-8 -*-  
# leetcode time     cost : 68 ms
# leetcode memory   cost : 13.7 MB
# solution 1, hash map,
# dict.get(key,default), if key not in the dict, then return the default,
'''
1. 构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
2. 这样一来，遍历整个 ss 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，
   如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

def main():
    inputX,expectRes = "MCMXCIV",1994
    obj = Solution()
    result = obj.romanToInt(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 