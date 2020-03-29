# leetcode time     cost : 1488 ms
# leetcode memory   cost : 13.8 MB 
# solution 1, DP, check every edge length from max to 1 for every point
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # 矩阵规模
        n, m, s = len(grid), len(grid[0]), 0
        # 四个方向上的前缀和
        L, U = [[[0] * (m + 1) for i in range(n + 1)] for j in range(2)]
        for i in range(n):
            for j in range(m):
                # 矩阵和
                s += grid[i][j]
                # L[i][j] 表示 (i, j) 的左边有多少个 1
                L[i][j + 1] = L[i][j] + grid[i][j]
                # U[i][j] 表示 (i, j) 的上边有多少个 1
                U[i + 1][j] = U[i][j] + grid[i][j]
        if s == 0:
            return 0
        # 四条边上 1 的个数
        edges = [0, 0, 0, 0]
        for e in range(min(n, m), 0, -1):
            for i in range(n - e + 1):
                for j in range(m - e + 1):
                    # 判断上边
                    edges[0] = L[i][j + e] - L[i][j]
                    # 判断下边
                    edges[1] = L[i + e - 1][j + e] - L[i + e - 1][j]
                    # 判断左边
                    edges[2] = U[i + e][j] - U[i][j]
                    # 判断右边
                    edges[3] = U[i + e][j + e - 1] - U[i][j + e - 1]
                    # 判断是否满足
                    if all([edge == e for edge in edges]):
                        return e * e
        return 0
    
def main():
    grid = [[1,1,1],[1,0,1],[1,1,1]]        # expect is 3
    obj = Solution()
    result = obj.largest1BorderedSquare(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 