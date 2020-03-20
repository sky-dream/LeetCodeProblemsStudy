# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB
# solution 1, Regular Express 
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

'''
^：匹配字符串开头
[\+\-]：代表一个+字符或-字符
?：前面一个字符可有可无
\d：一个数字
+：前面一个字符的一个或多个
\D：一个非数字字符
*：前面一个字符的0个或多个
'''