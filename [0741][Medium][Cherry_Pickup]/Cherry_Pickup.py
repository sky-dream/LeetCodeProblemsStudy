# leetcode time     cost : 1116 ms
# leetcode memory   cost : 23.6 MB 
# Time  Complexity: O(N*N*N)
# Space Complexity: O(N*N)
# solution 1,dp from top to bottom
# 2 dp process running at the same time
class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or
                    grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1+1, c2+1), dp(r1+1, c1, c2+1),
                           dp(r1, c1+1, c2), dp(r1+1, c1, c2))

            memo[r1][c1][c2] = ans
            return ans

        return max(0, dp(0, 0, 0))


def main():
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]    #expect is 5
    obj = Solution()
    result = obj.cherryPickup(grid)
    print("return result is ",result);

if __name__ =='__main__':
    main() 