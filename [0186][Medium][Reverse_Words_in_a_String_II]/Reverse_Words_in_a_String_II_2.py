# leetcode time     cost : 68 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2, shift word to tail start from end to start to make the index stable
class Solution:
    def reverseWords(self, s: [str]):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return s
        low = 0
        high = len(s) -1
        # find the 1st ' ' from right to left
        while high > 0 and s[high] != " ":
            high -= 1
        # if only 1 word,just return
        if high == 0:
            return s
        low = high - 1
        while low >= 0:
            if low == 0:
                s.append(" ")
                s.extend(s[low:high])
                del s[low:high+1]
                
            elif s[low] == " ":
                s.extend(s[low:high])
                del s[low:high]
                high = low

            low -= 1
        return s

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