# -*- coding: utf-8 -*-  
# leetcode time     cost : 64 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
            (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0: 
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)
    
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