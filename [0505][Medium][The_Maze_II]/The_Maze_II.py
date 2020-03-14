# -*- coding: utf-8 -*-  
# leetcode time     cost : 392 ms
# leetcode memory   cost : 13.6 MB
# solution 1, BFS
import collections
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        Distances = [[float('inf')]*n for _ in range(m)]
        Directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')]
        # set init value
        Distances[start[0]][start[1]] = 0
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
                x,y,step = pop_x+dx, pop_y+dy,Distances[pop_x][pop_y]   # 1st step from start is 0
                # not increase step here, then no need decrease step when backtrack from below while
                # if destination is a hole like 499, then while need also check [x,y] != destination
                while isValid(x,y,maze):
                    x,y = x+dx, y+dy
                    step += 1
                # backtrack, try another direction
                x,y = x-dx, y-dy
                # update the distance of (x,y) if this path is shorter
                if step < Distances[x][y]:
                    #print("update point",x,y,",distance to ",step)
                    Distances[x][y] = step
                    if not destinationReached(x,y,destination):
                        queue.append([x,y])
                    else:
                        break
                        print("destination found when change direction",x,y)
        return Distances[destination[0]][destination[1]] if Distances[destination[0]][destination[1]] != float('inf') else -1