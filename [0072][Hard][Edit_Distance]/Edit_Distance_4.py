# leetcode time     cost : 92 ms
# leetcode memory   cost : 16.2 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 2. dp with recursion
class Solution:
   def minDistance(self, s1, s2) -> int:
    memo = dict() # the memory cache
    def dp(i, j):
        if (i, j) in memo: 
            return memo[(i, j)]      
        # base case
        if i == -1: return j + 1
        if j == -1: return i + 1
        
        if s1[i] == s2[j]:
            memo[(i, j)] = dp(i - 1, j - 1)  # do nothing in this case
        else:
            memo[(i, j)] = min(
                dp(i, j - 1) + 1,    # insert
                dp(i - 1, j) + 1,    # delete
                dp(i - 1, j - 1) + 1 # replace
            )
        return memo[(i, j)]
    # the last index of i，j 
    return dp(len(s1) - 1, len(s2) - 1)

def main():
    word1 = "horse"          # expect is 3,
    word2 = "ros"
    obj = Solution()
    result = obj.minDistance(word1, word2)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 