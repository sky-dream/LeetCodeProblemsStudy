# leetcode time     cost : 56 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def reverseWords(self, s: [str]):
        """
        Do not return anything, modify str in-place instead.
        """
        i = 0
        for j in range(len(s)): # word_aT word_bT word_c
            if s[j] == ' ':
                self.reverse(s, i, j)
                i = j + 1
        self.reverse(s, i, len(s)) # word_aT word_bT word_cT

        #print("aT bT cT:",s)
        self.reverse(s, 0, len(s)) # word_c word_b word_a
        return s
    
    def reverse(self, s, i, j):
        l, r = i, j - 1  # 因为j对应的是空格字符的索引，要往前推一位
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

def main():
    inputStr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"] 
    expect = ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    obj = Solution()
    result = obj.reverseWords(inputStr)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main() 