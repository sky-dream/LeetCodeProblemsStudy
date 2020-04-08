# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def convertToTitle(self, n: int) -> str:
        # 1--26 is one char,A--Z
        char_nums = []
        num_A = ord("A")
        # use 0-25 to represent the A-Z, refer to 0-9,
        while n:
            num = (n-1)%26
            n = (n-1) // 26
            char_nums.append(num)
        ans = ""
        length = len(char_nums)
        for i in range(length-1,-1,-1):
            # num 0 is the char A, then add the offset for B-Z,
            char_ascii = chr(char_nums[i] + num_A)
            ans = ans+char_ascii
        print(char_nums)
        return ans