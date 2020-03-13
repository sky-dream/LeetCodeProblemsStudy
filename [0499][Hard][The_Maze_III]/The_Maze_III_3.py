# -*- coding: utf-8 -*-  
# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.6 MB
# solution 1, BFS
import collections
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:     
        m = len(maze)
        n = len(maze[0])
        queue = collections.deque()
        stepPathDict = {}
        directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')] 
        distance = [[float('inf')]*n for _ in range(m)] 
        string = [["impossible"]*n for _ in range(m)]
        # set init value
        distance[ball[0]][ball[1]] = 0
        string[ball[0]][ball[1]] = ""
        def isValid(x,y,maze,step,path):
            if 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y]== 0:
                return True
            else:
                return False 
        def holeReached(x,y):
            if x == hole[0] and y == hole[1]:
                return True
            else:
                return False 
        def BFS(maze,ball,hole):
            path = ""
            step = 0
            queue.append([ball[0],ball[1],step,path]) 
  
            while queue:
                pop_x,pop_y,pop_step,pop_path = queue.popleft()
                
                #print("poped out: [",pop_x,",",pop_y,",",step,",",path,"]",",after poped,queue:",queue)               
                for dx,dy,letter in directions: 
                    x,y,step,newPath =pop_x+dx, pop_y+dy, distance[pop_x][pop_y],string[pop_x][pop_y]

                    while isValid(x,y,maze,step,newPath) and not holeReached(x-dx,y-dy):                                      
                        x = x+dx                        # 继续前进，模拟小球的滚动过程
                        y = y+dy                        
                        step += 1                       # 记录步数
                    # backtrack to the last valid point, try another direction
                    x = x - dx
                    y = y - dy
                    # step -= 1 , no need back track step, it will be compareed with distance[x][y]
                    # due to need lexicographically smallest way, start with the order d,l,r,u,
                    if distance[x][y] > step or (distance[x][y]==step and newPath+letter<string[x][y]):
                        distance[x][y] = step
                        string[x][y] = newPath + letter
                        print("append new node: ",x,y)
                        if x!=hole[0] or y!=hole[1]:
                            queue.append([x,y,step,newPath])

        BFS(maze,ball,hole)

        # check whether stepPathDict.keys() has elements except 0
        return string[hole[0]][hole[1]]