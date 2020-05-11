# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 2, Regular-Expression
import re
class Solution:
    def isValid(self, code):
        if code == 't':
            return False
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', 'c', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'

def main():
    inputX,expectRes = "<DIV>This is the first line <![CDATA[<div>]]></DIV>",True
    obj = Solution()
    result = obj.isValid(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 