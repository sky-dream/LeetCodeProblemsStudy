# leetcode time     cost : 788 ms
# leetcode memory   cost : 16.5 MB
# Time  Complexity: O(rc)
# Space Complexity: O(rc)
# solution 3, dp with optimize
class Solution:
    def updateMatrix(self, matrix: [[int]]):
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist

def main():
    intervals = [[0,0,0],[0,1,0],[0,0,0]]   
    expect = [[0,0,0],[0,1,0],[0,0,0]]
    obj = Solution()
    result = obj.updateMatrix(intervals)
    try:
        assert result == expect
        print("passed, result is follow expectation:",result)
    except AssertionError as aError:
        print('failed, result is wrong',result, aError.__str__())
    
if __name__ =='__main__':
    main()   