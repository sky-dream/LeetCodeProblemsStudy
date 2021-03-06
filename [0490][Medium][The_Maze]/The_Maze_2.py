# -*- coding: utf-8 -*-  
# leetcode time     cost : 316 ms
# leetcode memory   cost : 13.6 MB
# Solution 2, BFS
import collections
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m,n = len(maze),len(maze[0])
        Visited = [[0]*n for _ in range(m)]
        Directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')]
        # set init value
        Visited[start[0]][start[1]] = 0
        def isValid(x,y,maze):
            if 0<=x<m and 0<=y<n and maze[x][y] == 0:
                return True
            else:
                return False
        def destinationReached(x,y,destination):
            if x == destination[0] and y == destination[1]:
                return True
            else:
                return False 
        queue = collections.deque()
        queue.append(start)
        while queue:
            pop_x,pop_y = queue.popleft()
            for dx,dy,direction in Directions:
                x,y = pop_x+dx, pop_y+dy  # 1st step from start is 0
                # if destination is a hole like 499, then while need also check [x,y] != destination
                while isValid(x,y,maze) :                    
                    x,y = x+dx, y+dy
                                       
                # backtrack to the point before the blocked point, try another direction
                x,y = x-dx, y-dy
                if destinationReached(x,y,destination):
                    #print("destinationReached",x,y,",Visited[x][y] ",Visited[x][y],",on the direction:",direction)
                    return True
                
                # update the Visited[x][y] to 1 and drill down if Visited[x][y]==0
                if Visited[x][y]==0:
                    Visited[x][y]=1
                    #print("update point",x,y,",Visited[x][y] ",Visited[x][y],",on the direction:",direction)
                    queue.append([x,y])
        return False
