# -*- coding: utf-8 -*-  
# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, stack,
from collections import deque

class Solution:
    # Deal with the operations
    def solve(self, operand: int, sign: str, stack: deque) -> int:
        if sign == '+':
            return operand
        elif sign == '-':
            return -operand
        elif sign == '*':
            return stack.pop() * operand
        elif sign == '/':
            return int(stack.pop() / operand)

    def calculate(self, s: str) -> int:
        stack = deque()

        operand = 0
        sign = '+'

        for c in s:
            if c == ' ':
                # Ignore the space
                continue
            elif c.isdigit():
                operand = operand * 10 + int(c)
            elif c == '(':
                # An integer cannot be just before a '(', so only save the previous operator here
                stack.append(sign)
                sign = '+'
            else:
                # Do the default calculation
                result = self.solve(operand, sign, stack)

                operand = 0

                if c == ')':
                    # Summate all the intergers on the top of a stack until meet an operator, which means
                    # we need to do the corresponding operation with the summation value as an operand
                    while isinstance(stack[-1], int):
                        result += stack.pop()

                    sign = stack.pop()

                    operand = self.solve(result, sign, stack)
                    sign = '+'
                else:
                    # Push the result value to the stack for later summation
                    # Save the operator for calculation in a coming loop
                    sign = c
                    stack.append(result)

        # The calculation doesn't finish here. We always do actual calculation in later loops, so
        # at present we should deal with the operand gotten in the last loop.
        last = self.solve(operand, sign, stack)
        stack.append(last)

        # + and - have the lowest priority
        return sum(stack)

def main():
    string_s = "(2+6* 3+5- (3*14/7+2)*5)+3"      #expect is -12  
    obj = Solution()
    res = obj.calculate(string_s)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 