# leetcode time     cost : 64 ms
# leetcode memory   cost : 13.8 MB 
# solution 1, DP
class Solution:
    def minHeightShelves(self, books: [[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [1000000] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            tmp_width, j, h = 0, i, 0
            while j > 0:
                tmp_width += books[j - 1][0]
                if tmp_width > shelf_width:
                    break
                h = max(h, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + h)
                j -= 1
        return dp[-1]
    
def main():
    array,shelf_width = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]] ,4         # expect is 6
    obj = Solution()
    result = obj.minHeightShelves(array,shelf_width)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 