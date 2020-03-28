# leetcode time     cost : 756 ms
# leetcode memory   cost : 14.7 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(1)
# solution 3, DP， refer to LCS, Longest common sequence
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        def get_total_ascii(s):
            return sum( [ord(c) for c in s] )
        
        dp = [ [ 0 for _ in range(len(s2)+1) ] for _ in range(len(s1)+1) ]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return get_total_ascii(s1) + get_total_ascii(s2) - 2*dp[-1][-1]

def main():  
    s1 = "sea" #expect is 231
    s2 = "eat"   
    obj = Solution()
    result = obj.minimumDeleteSum(s1,s2)
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 