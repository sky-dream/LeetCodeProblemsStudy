# leetcode time     cost : 64 ms
# leetcode memory   cost : 13.8 MB 
# solution 1, DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        last_memory=[0]*(len(text1)+1)
        memory=[0]*(len(text1)+1)
        for i,t2 in enumerate(text2):
            memory=[0]*(len(text1)+1)
            for j,t1 in enumerate(text1):
                memory[j+1]=max(memory[j],last_memory[j+1],last_memory[j]+1 if t1==t2 else 0 )
            last_memory=memory
        # print(memory)
        return memory[-1]
    
def main():
    text1,text2 = "abcde", "ace"         # expect is 3
    obj = Solution()
    result = obj.longestCommonSubsequence(text1,text2)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 