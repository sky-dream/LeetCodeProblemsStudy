# leetcode time     cost : max time exceeded
# leetcode memory   cost : --- MB 
# solution 2, recursion
class Solution:
    def longestCommonSubsequence(self,str1, str2) -> int:
        def dp(i, j):
            # 空串的 base case
            if i == -1 or j == -1:
                return 0
            if str1[i] == str2[j]:
                # 这边找到一个 lcs 的元素，继续往前找
                return dp(i - 1, j - 1) + 1
            else:
                # 谁能让 lcs 最长，就听谁的
                return max(dp(i-1, j), dp(i, j-1))
            
        # i 和 j 初始化为最后一个索引
        return dp(len(str1)-1, len(str2)-1)
    
def main():
    text1,text2 = "abcde", "ace"         # expect is 6
    obj = Solution()
    result = obj.longestCommonSubsequence(text1,text2)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 