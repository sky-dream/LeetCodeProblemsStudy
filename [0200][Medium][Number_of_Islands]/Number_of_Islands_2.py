# leetcode time     cost : 108 ms
# leetcode memory   cost : 14.4 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1. DFS
class Solution:
    #def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                for x,y in zip([i+1, i-1, i, i], [j, j, j+1, j-1]):
                    sink(x,y) 
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

def main():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]  # expect is 1,
    obj = Solution()
    result = obj.numIslands(grid)       
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 