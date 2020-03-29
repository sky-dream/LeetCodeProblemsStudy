# leetcode time     cost : 680 ms
# leetcode memory   cost : 14.5 MB 
# solution 1, BFS
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        land = [[x,y] for x in range(N) for y in range(N) if grid[x][y]]

        if len(land)==0 or len(land)==N*N:
            return -1

        direction = [(0,-1),(1,0),(0,1),(-1,0)]
        length = -1

        def valid(x,y):
            return -1<x<N and -1<y<N

        while land:
            length+=1
            tem = [] # save the water position in this layer
            for i in land:
                for x,y in direction:
                    newx,newy = i[0]+x,i[1]+y
                    if valid(newx,newy) and grid[newx][newy]==0:
                        grid[newx][newy]=2  # tag it as visited
                        tem.append((newx,newy))
            land = list(set(tem))

        return length