# leetcode time     cost : 84 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(R∗C∗2^R∗C)
# Space  Complexity: O(R∗C∗2^R∗C)
# solution 2， dp,
from functools import lru_cache
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def code(r, c):
            return 1 << (r * C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    start_r, start_c = r, c
                if val == 2:
                    target_r, target_c = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == target_r and c == target_c:
                return +(todo == 0)

            ans = 0
            for nr, nc in neighbors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(start_r, start_c, target)

def main():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]      #expect is 2
    obj = Solution()
    res = obj.uniquePathsIII(grid)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   