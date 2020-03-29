# leetcode time     cost : 176 ms
# leetcode memory   cost : 13.9 MB 
# solution 1, DP, take every point as left,up point,check the 4 edges
class Solution:
    def largest1BorderedSquare(self, grid) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        maxLen = 0
        m, n = len(grid), len(grid[0])
        # 遍历每个点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    currLen = maxLen
                    while i + currLen < m and j + currLen < n:
                        flag2 = True
                        # 如果‘左边界‘有0， 那么检查下一个点
                        for a in range(i, i + currLen + 1):
                            if grid[a][j] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果‘上边界‘有0， 那么检查下一个点
                        for b in range(j, j + currLen + 1):
                            if grid[i][b] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果’右边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for a in range(i, i + currLen + 1):
                            if grid[a][j + currLen] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        # 如果’下边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for b in range(j, j + currLen + 1):
                            if grid[i + currLen][b] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        currLen += 1
                        maxLen = currLen
        return maxLen * maxLen
    
def main():
    grid = [[1,1,1],[1,0,1],[1,1,1]]        # expect is 3
    obj = Solution()
    result = obj.largest1BorderedSquare(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 