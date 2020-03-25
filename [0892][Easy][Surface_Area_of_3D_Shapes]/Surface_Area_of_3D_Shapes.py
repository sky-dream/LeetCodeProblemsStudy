# leetcode time     cost : 136 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N**2)
# Space Complexity: O(1)
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
   
def main():
    numbers = [[1,2],[3,4]]       # 34
    obj = Solution()
    res = obj.surfaceArea(numbers)
    print("return value is ",res)
        
    
if __name__ =='__main__':
    main()     