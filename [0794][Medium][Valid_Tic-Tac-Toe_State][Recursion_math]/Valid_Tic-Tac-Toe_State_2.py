# -*- coding: utf-8 -*- 
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)

# solution 2, concise code, merge the 2D string into 1-D string
# https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/117716/4-lines-Python
class Solution:
    def validTicTacToe(self, board):
        b = '|'.join(board)
        # "123|456|789"[::5]--->'159'
        x, o = (any(p*3 in b[s::d] for s in range(9) for d in (1, 3, 4, 5)) for p in 'XO')
        m = b.count('X') - b.count('O')
        return (m == 0 and not x) or (m == 1 and not o) # return m == (not o) if m else not x

def main():
    inputX,expectRes = ["XOX", "O O", "XOX"],True
    obj = Solution()
    result = obj.validTicTacToe(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()    