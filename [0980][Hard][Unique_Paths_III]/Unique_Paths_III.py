# leetcode time     cost : 84 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(4^R∗C)
# Space  Complexity: O(R∗C)
# solution 1， backtracking with dfs
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: start_r, start_c = r, c
                if val == 2: target_r, target_c = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == target_r and c == target_c:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(start_r, start_c, todo)
        return self.ans

def main():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]      #expect is 2
    obj = Solution()
    res = obj.uniquePathsIII(grid)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   