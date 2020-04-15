# leetcode time     cost : 832 ms
# leetcode memory   cost : 17.3 MB
# Time  Complexity: O(rc)
# Space Complexity: O(rc)
# solution 1, BFS
import collections
class Solution:
    def updateMatrix(self, matrix: [[int]]):
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        
        return dist
def main():
    matrix = [[0,0,0],[0,1,0],[0,0,0]]   
    expect = [[0,0,0],[0,1,0],[0,0,0]]
    obj = Solution()
    result = obj.updateMatrix(matrix)
    try:
        assert result == expect
        print("passed, result is follow expectation:",result)
    except AssertionError as aError:
        print('failed, result is wrong',result, aError.__str__())
    
if __name__ =='__main__':
    main()  