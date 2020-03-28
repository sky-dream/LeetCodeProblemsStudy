# leetcode time     cost : 136 ms
# leetcode memory   cost : 14.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, DP
# solution 1,set
class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                # delete all posible sufix in the set.
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)

def main():
    words = ["time", "me", "bell"]      #expect is 10
    obj = Solution()
    res = obj.minimumLengthEncoding(words)
    assert res == 10
    
    
if __name__ =='__main__':
    main()   