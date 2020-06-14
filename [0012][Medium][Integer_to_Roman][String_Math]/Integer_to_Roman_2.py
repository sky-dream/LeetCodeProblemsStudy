# -*- coding: utf-8 -*-  
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 2
class Solution:
    def intToRoman(self, num: int):
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]
    
def main():
    num = 394
    expect = "CCCXCIV"
    obj = Solution()
    result = obj.intToRoman(num)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main()  