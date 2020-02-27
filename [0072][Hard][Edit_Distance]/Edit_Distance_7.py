# leetcode time     cost : 140 ms
# leetcode memory   cost : 13.6 MB   
# Time  Complexity: O(min(m,n))
# Space Complexity: O(min(m,n))
# solution 1. dp with iteration, compress DP to 1D compare to Edit_Distance_6.py,
class Solution(object):
    # we can implement a rolling 1D DP since only two rows of DP table are actually used. 
    # So space complexity could be reduced to O(min(m,n)):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)  
        # switch word1 and word2 if m < n to ensure n ≤ m to save space for 'curr'.
        if m < n: 
            m, n = n,m
            word1, word2 = word2, word1
        curr = list(range(n+1))
        for i in range(m):
            # curr =  [i+1] + [0] * n to init col 0, the first index for every row.
            # prev is the list of col values of the row before current row.
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                curr[j+1] = prev[j] if word1[i] == word2[j] else min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]

def main():
    word1 = "horse"          # expect is 3,
    word2 = "ros"
    obj = Solution()
    result = obj.minDistance(word1, word2)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 