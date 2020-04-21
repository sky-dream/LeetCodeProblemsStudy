# -*- coding: utf-8 -*-  
# leetcode time     cost : 148 ms
# leetcode memory   cost : 13.9 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, stack,
class Solution:
    def calculate(self, s: str) -> int:
        def helper(pre, curr, next, sign):
            if sign == '+':
                pre += curr
                curr = next
            elif sign == '-':
                pre += curr
                curr = -next
            elif sign == '*':
                curr *= next
            elif sign == '/':
                curr = int(curr / next)
            return pre, curr, 0

        def cal(s):
            pre, curr, next = 0, 0, 0
            sign = '+'
            i = 0
            while i < len(s):
                if s[i].isnumeric():
                    next = next * 10 + int(s[i])
                elif s[i] == '(':
                    count = 1
                    i += 1
                    j = i
                    while i < len(s):
                        if s[i] == '(':
                            count += 1
                        elif s[i] == ')':
                            count -= 1
                        if count == 0:
                            break
                        i += 1
                    next = cal(s[j:i])
                if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
                    pre, curr, next = helper(pre, curr, next, sign)
                    sign = s[i]
                i += 1
            return pre + curr

        return cal(s)


def main():
    string_s = "(2+6* 3+5- (3*14/7+2)*5)+3"      #expect is -12  
    obj = Solution()
    res = obj.calculate(string_s)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()  